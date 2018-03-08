# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

import params

logger = logging.getLogger(__name__)

support_search = ["日志"]


def extract_item(item):
    """
    check if item supported, this func just for lack of train data.
    :param item: item in track, eg: "日志"
    :return:
    """
    if item is None:
        return None
    for name in support_search:
        if name in item:
            return name
    return None

class ActionLogDateConsume(Action):
    def name(self):
        return 'action_log_date_consume'

    def run(self, dispatcher, tracker, domain):
        item = tracker.get_slot("item")
        item = extract_item(item)
        if item is None:
            dispatcher.utter_message("你好,请按格式输入想要查询的时间,目前只支持查询某一天的日志")
            dispatcher.utter_message("比如,你可以这样回答：“2018.01.01”")
            return []

        date = tracker.get_slot("date")
        if date is None:
            dispatcher.utter_message("请问要查询哪一天的日志,请按格式输入想要查询的时间,目前只支持查询某一天的日志")
            dispatcher.utter_message("比如,你可以这样回答：“2018.01.01”")
            return []
        # query database here using item and time as key. but you may normalize time format first.
        dispatcher.utter_message("好，请稍等")
        if item == "日志":
            dispatcher.utter_message("您好，该天{}的{}为:厉害!".format(date, item))
        else:
            dispatcher.utter_message("您好,您是要查询日志吗?".format(date))
        return []


class MobilePolicy(KerasPolicy):
    def model_architecture(self, num_features, num_actions, max_history_len):
        """Build a Keras model and return a compiled model."""
        from keras.layers import LSTM, Activation, Masking, Dense
        from keras.models import Sequential

        n_hidden = 32  # size of hidden layer in LSTM
        # Build Model
        batch_shape = (None, max_history_len, num_features)

        model = Sequential()
        model.add(Masking(-1, batch_input_shape=batch_shape))
        model.add(LSTM(n_hidden, batch_input_shape=batch_shape))
        model.add(Dense(input_dim=n_hidden, output_dim=num_actions))
        model.add(Activation("softmax"))

        model.compile(loss="categorical_crossentropy",
                      optimizer="adam",
                      metrics=["accuracy"])

        logger.debug(model.summary())
        return model


def train_dialogue():
    '''
    training dm model

    Returns:

    '''
    domain_file = params.dm_domain_file
    model_path = params.dm_model_path
    training_data_file = params.dm_training_data
    agent = Agent(domain_file, policies=[MemoizationPolicy(), MobilePolicy()])

    agent.train(
        training_data_file,
        max_history=2,
        epochs=params.dm_training_epoch,
        batch_size=params.dm_training_batch_size,
        augmentation_factor=50,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    '''
    training nlu model

    Returns: model dir

    '''
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer

    training_data = load_data(params.nlu_training_data)
    trainer = Trainer(RasaNLUConfig(params.nlu_model_config))
    trainer.train(training_data)
    model_directory = trainer.persist(params.nlu_model_save_dir, project_name=params.nlu_project_name, fixed_model_name=params.nlu_fixed_model_name)

    return model_directory


def run_ivrbot_online():
    '''

    :return:
    '''
    input_channel = ConsoleInputChannel()
    interpreter = RasaNLUInterpreter(params.nlu_interpreter)
    domain_file = params.dm_domain_file
    training_data_file = params.dm_training_data
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpreter)

    agent.train_online(training_data_file,
                       input_channel=input_channel,
                       max_history=2,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


def run(serve_forever=True):
    '''
    start to run bot

    Args:
        serve_forever:

    Returns:

    '''
    agent = Agent.load(params.dm_model_path, interpreter=RasaNLUInterpreter(params.nlu_interpreter))

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == "__main__":
    logging.basicConfig(level="INFO")

    parser = argparse.ArgumentParser(description="starts the bot")

    parser.add_argument(
        "task",
        choices=["train-nlu", "train-dialogue", "run", "online_train"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    elif task == "online_train":
        run_ivrbot_online()
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)
