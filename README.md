# Cheemsbot from Rasa

## Requirement:
- python 3.8 and python virtual enviroment

```shell
python -m venv venv
venv/Scripts/activate or source venv/bin/activate
pip install -r requirements.txt
```
I've used pretrained word vector of fasttext So you need to download pretrained word vector from fasttext
```
mkdir vi_feature
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.vi.300.bin.gz -P vi_feature
gunzip cc.vi.300.bin.gz
```
----------------------------------------------------------------------------------------------------
## Train cheemsbot:
 
```shell
rasa train
```

## Init fake store's db
```
python init_db.py
```

## Run cheemsbot:
 
```shell
docker compose up
rasa run actions --auto-reload
```
 
```shell
rasa run shell
```

```
rasa run  --cors "*" --enable-api
```
----------------------------------------------------------------------------------------------------
