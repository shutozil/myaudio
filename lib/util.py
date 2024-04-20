from __future__ import annotations
import os

# import shutil

# from datetime import datetime, timezone, timedelta

# JST = timezone(timedelta(hours=9))


def check_file_exists(file_path: str) -> bool:
    # 指定されたパスのファイルが存在するかどうかをチェック
    return os.path.isfile(file_path)


def check_dir_exists(path: str) -> bool:
    return os.path.isdir(path)


def mkdir(directory_name: str) -> None:
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def read_txt_file(filename: str) -> str | None:
    """
    テキストファイルを読み込みます。

    Args:
        filename (str): 読み込むファイルの名前。

    Returns:
        str | None: テキストファイルの内容。ファイルが存在しない場合はNoneを返します。
    """
    filepath = f"data/{filename}"

    if not filename.endswith(".txt"):
        print("ファイル名が正しくありません。")
        return

    if not check_file_exists(filepath):
        print(f"{filepath} は存在しません。")
        return

    with open(filepath, "r") as f:
        txt_data = f.read()

    return txt_data
