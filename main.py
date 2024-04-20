from __future__ import annotations

import argparse
from pydub import AudioSegment


import lib.settings as settings
import lib.util as util
from lib.trans import generate_audio, create_ssml_from_text


def main():
    parser = argparse.ArgumentParser(
        description="argparseを使用したサンプルスクリプトです。"
    )
    parser.add_argument("--filename", type=str, help="ファイル名を入力してください.")
    parser.add_argument(
        "--rm", type=str, help="ファイル名をもとに作成したデータを削除します."
    )

    # 引数の解析
    args = parser.parse_args()
    filename = args.filename

    # TODO: 動画が生成されていたら処理を終える

    txt_data: str | None = util.read_txt_file(filename=filename)
    if txt_data is None:
        return

    # NOTE: resultsディレクトリにファイル名をキーにした、ディレクトリを作成
    result_dir = f"results/{filename.replace('.txt', '')}"
    if not util.check_dir_exists(result_dir):
        util.mkdir(result_dir)

    mp3_filename = f"{result_dir}/audio.mp3"
    # 出力ファイルに書き込み
    if util.check_file_exists(mp3_filename):
        # NOTE: オーディオが作成済みなら音声ファイルを作成しない
        print(f"オーディオコンテンツ: {mp3_filename}は存在します。")
    else:
        narration = create_ssml_from_text(txt_data.strip())
        print(f"{narration=}")
        response = generate_audio(
            txt_data,
            settings.LANG,
            settings.VOICE_TYPE,
        )

        with open(mp3_filename, "wb") as out:
            out.write(response.audio_content)
            print(f"オーディオコンテンツが{mp3_filename}に書き込まれました。")


if __name__ == "__main__":
    main()
