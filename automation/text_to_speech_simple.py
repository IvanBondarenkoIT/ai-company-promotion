#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Простой скрипт для конвертации текста в аудио (без разбивки на части)
Использует Google TTS
"""

import sys
from pathlib import Path

# Fix Windows UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def clean_text(text):
    """Очищает текст от форматирования"""
    text = text.replace("═══════════════════════════════════════════════════════════════════", "")
    text = text.replace("───────────────────────────────────────────────────────────────────", "")
    text = text.replace("┌", "").replace("┐", "").replace("└", "").replace("┘", "")
    text = text.replace("├", "").replace("┤", "").replace("│", "")
    text = text.replace("─", " ").replace("═", " ")
    
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if line and not line.startswith("═") and not line.startswith("─"):
            lines.append(line)
    
    return "\n".join(lines)


def main():
    print("🎙️ ПРОСТАЯ КОНВЕРТАЦИЯ ТЕКСТА В АУДИО")
    print("=" * 60)
    print()
    
    try:
        from gtts import gTTS
        
        text_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_ПОЛНАЯ_v2.txt"
        output_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_АУДИО.mp3"
        
        if not text_file.exists():
            print(f"❌ Файл не найден: {text_file}")
            return
        
        print("📖 Читаю файл философии...")
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Очищаем текст
        text = clean_text(text)
        print(f"📝 Текст подготовлен ({len(text)} символов)")
        
        # Google TTS имеет лимит ~5000 символов, берем первую часть
        if len(text) > 5000:
            print("⚠️ Текст длиннее 5000 символов, беру первую часть")
            print("💡 Для полного текста используйте TTSMaker: https://ttsmaker.com/")
            text = text[:5000] + "\n\n[Текст обрезан из-за ограничений сервиса]"
        
        print("🎙️ Создаю аудио файл (требует интернет, может занять 2-5 минут)...")
        print("⏳ Пожалуйста, подождите...")
        
        # Создаем аудио
        tts = gTTS(text=text, lang='ru', slow=False)
        tts.save(str(output_file))
        
        if output_file.exists() and output_file.stat().st_size > 0:
            size_mb = output_file.stat().st_size / 1024 / 1024
            print(f"✅ Аудио файл создан: {output_file}")
            print(f"📊 Размер файла: {size_mb:.2f} MB")
        else:
            print("❌ Файл не создан или пустой")
        
    except ImportError:
        print("❌ Библиотека gtts не установлена")
        print("📦 Установите: pip install gtts")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

