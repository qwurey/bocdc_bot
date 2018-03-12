### Function 
Need to do...

### Structure
A bot based on rasa-nlu and rasa-core:

Related:
<br>
https://github.com/RasaHQ/rasa_nlu
<br>
https://github.com/RasaHQ/rasa_core
<br>
https://github.com/crownpku/Rasa_NLU_Chi
<br>

### How to use
1. Using pip:

  ```shell
  pip install rasa_nlu
  pip install rasa_core
  pip install jieba
  ```

2. Download project code:

  ```shell
  git clone git@github.com:qwurey/bocdc_bot.git
  ```

3. Download trained word embedding data.
  For example, I use `https://github.com/crownpku/Rasa_NLU_Chi` trained word embedding data `total_word_feature_extractor_zh.dat`

4. Import word embedding data.

  ```shell
  cd bocdc_bot
  cp total_word_feature_extractor_zh.dat bocdc_bot/data
  ```

5. Train model and run:

  ```shell
  python bot.py train-nlu
  python bot.py train-dialogue
  python bot.py run
  ```

  ​


