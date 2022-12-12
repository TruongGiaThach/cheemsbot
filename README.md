# Cheemsbot from Rasa

## Requirement:x
- python 3.8

```shell
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

----------------------------------------------------------------------------------------------------
## Setting:
- Open file: `custom\vi_tokenize.py` change path url to stopwords file 'PATH_STOP_WORD'

- Copy 3 file from directory 'custom' overwrite to rasa directory of you:
    ### Examples:
        C:\Users\Admin\anaconda3\Lib\site-packages\rasa\nlu\utils\hugging_face\registry.py
        C:\Users\Admin\anaconda3\Lib\site-packages\rasa\engine\recipes\default_components.py
        C:\Users\Admin\anaconda3\Lib\site-packages\rasa\nlu\tokenizers\vi_tokenize.py

- You can also copy the file contents slack-custom.py overwrite file slack.py in rasa directory
----------------------------------------------------------------------------------------------------
## Train:
 
```shell
rasa train
```

## Run:
 
```shell
rasa run actions
```
 
```shell
rasa run shell
```

----------------------------------------------------------------------------------------------------
