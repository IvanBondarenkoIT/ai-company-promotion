import os
import sys
from pathlib import Path
import whisper

# Fix Windows UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def transcribe_files():
    # Setup paths
    base_dir = Path(__file__).parent.parent
    input_dir = base_dir / "data" / "input"
    output_dir = base_dir / "docs" / "transcriptions"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Загрузка модели Whisper (это может занять некоторое время при первом запуске)...")
    # Load the Whisper model (base is a good balance between speed and quality)
    model = whisper.load_model("base")
    
    # Supported audio extensions
    audio_extensions = {'.m4a', '.mp3', '.wav', '.ogg', '.webm'}
    
    # Find audio files
    audio_files = [f for f in input_dir.iterdir() if f.suffix.lower() in audio_extensions]
    
    if not audio_files:
        print(f"⚠️ Аудиофайлы не найдены в {input_dir}")
        return

    print(f"✅ Найдено {len(audio_files)} аудиофайлов для расшифровки.\n")

    for i, audio_file in enumerate(audio_files, 1):
        try:
            print(f"[{i}/{len(audio_files)}] Расшифровка {audio_file.name}...")
            
            # Transcribe the audio file
            result = model.transcribe(str(audio_file), language="ru", fp16=False)
            
            # Save transcription
            output_filename = audio_file.stem + ".txt"
            output_path = output_dir / output_filename
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])
                
            print(f"✅ Сохранено в {output_path}\n")
            
        except Exception as e:
            print(f"❌ Ошибка при расшифровке {audio_file.name}: {e}\n")

    print("🎉 Расшифровка завершена!")

if __name__ == "__main__":
    transcribe_files()

