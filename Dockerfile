FROM python:3.9.7

WORKDIR /project

RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0

# 画像・動画を扱うために必要なライブラリをインストール
RUN apt-get -y update && apt-get -y install ffmpeg imagemagick

RUN pip3 install \
    "moviepy" \
    "google-cloud-texttospeech" \
    "pydub"