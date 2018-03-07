

'''
nlu related
'''
nlu_training_data = "data/nlu_data.json"
nlu_model_config = "nlu_model_config.json"
nlu_project_name = "bocbot"
nlu_fixed_model_name = "nlu_bocbot"
nlu_model_save_dir = "models/"
nlu_interpreter = nlu_model_save_dir + nlu_project_name + '/' + nlu_fixed_model_name
'''

'''
dm_domain_file = "dm_domain.yml"
dm_model_path = "models/dialogue"
dm_training_data = "data/dm_story.md"
dm_training_epoch = 200
dm_training_batch_size = 16