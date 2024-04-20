テキストファイルのテキストを音声（`.mp3`）に変換するプログラム

### commands

```
$ docker-compose build
$ docker-compose up -d
$ docker exec -it myaudio bash
```

```
# python3 main.py --filename hello.txt
```

### `.env`

```
GOOGLE_APPLICATION_CREDENTIALS=YOUR_GCP_SERVICE_ACCOUNT_JSON_FILE_PATH
```
