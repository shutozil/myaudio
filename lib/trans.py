from google.cloud import texttospeech

import lib.settings as settings

client = texttospeech.TextToSpeechClient()


def generate_audio(
    ssml: str,
    lang: str = settings.LANG,
    voice_name: str = settings.VOICE_TYPE,
    speak_rate: float = settings.SPEAKING_RATE,
    pitch: float = settings.PTICH,
):
    """
    テキストから音声を生成する関数です。

    Args:
        ssml (str): SSML形式のテキスト
        lang (str, optional): 言語コード. デフォルトは settings.LANG.
        voice_name (str, optional): 音声の種類. デフォルトは settings.VOICE_TYPE.
        speak_rate (float, optional): 話速. デフォルトは settings.SPEAKING_RATE.
        pitch (float, optional): 音の高さ. デフォルトは settings.PTICH.

    Returns:
        response: 音声合成の結果を含むレスポンスオブジェクト
    """
    # テキストの設定
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

    # 音声の設定
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang,
        name=voice_name,
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    # オーディオ設定
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speak_rate,
        pitch=pitch,
    )

    # テキストから音声を合成
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response


def create_ssml_from_text(text: str, break_time: str = settings.SSLM_BREAK_TIME) -> str:
    """
    Google Text-to-Speechを使用して音声を生成するためのSSMLを生成します。

    Args:
        text (str): 音声に変換する入力テキスト。
        break_time (str, optional): 各SSMLパート間の休止時間。デフォルトは settings.SSLM_BREAK_TIME。

    Returns:
        str: 生成されたSSML文字列です。
    """
    ssml_parts: list[str] = _prepare_ssml(text)
    ssml_with_breaks = f"<break time='{break_time}'/>".join(ssml_parts)

    ssml = f"<speak>{ssml_with_breaks}</speak>"
    return ssml


def _prepare_ssml(text: str) -> list[str]:
    """SSMLに変換する前に実行する前処理

    NOTE: リプレースする値を増やす場合は、オーバーライドすること

    """

    return text.replace("\n\n", "\n").split("\n")
