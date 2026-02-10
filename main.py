import whisper
import sys
from argostranslate import translate
from pathlib import Path


def transcribe_and_translate(audio_path, target_lang="pt"):
    model = whisper.load_model("base")

    result = model.transcribe(audio_path)
    text = result["text"]
    source_lang = result["language"]

    translated = translate.translate(text, source_lang, target_lang)

    return translated


def save_to_file(text, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    if sys.version_info < (3, 11):
        raise RuntimeError("Este projeto requer Python 3.11 ou superior")

    audio_file = "audio.mp3"
    output_file = "transcript_ptbr.txt"

    translated_text = transcribe_and_translate(audio_file)
    save_to_file(translated_text, output_file)

    print(f"Transcrição traduzida salva em: {output_file}")
