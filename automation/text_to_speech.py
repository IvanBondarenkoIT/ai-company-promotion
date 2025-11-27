#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для конвертации текста в аудио (Text-to-Speech)
Создает аудио файл из текста философии для прослушивания
"""

import sys
from pathlib import Path

# Fix Windows UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

async def create_audio_async(text, output_file, voice="ru-RU-SvetlanaNeural"):
    """Асинхронная функция для создания аудио"""
    import edge_tts
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(output_file))


def create_audio_with_edge_tts():
    """
    Использует Microsoft Edge TTS (бесплатно, хорошее качество)
    Требует: pip install edge-tts
    """
    try:
        import asyncio
        import edge_tts
        
        # Читаем файл философии
        text_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_ПОЛНАЯ_v2.txt"
        output_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_АУДИО.mp3"
        
        if not text_file.exists():
            print(f"❌ Файл не найден: {text_file}")
            return False
        
        print("📖 Читаю файл философии...")
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Убираем лишние символы форматирования
        text = text.replace("═══════════════════════════════════════════════════════════════════", "")
        text = text.replace("───────────────────────────────────────────────────────────────────", "")
        text = text.replace("┌", "").replace("┐", "").replace("└", "").replace("┘", "")
        text = text.replace("├", "").replace("┤", "").replace("│", "")
        text = text.replace("─", " ").replace("═", " ")
        # Оставляем только текст
        lines = [line.strip() for line in text.split("\n") if line.strip() and not line.strip().startswith("═")]
        text = "\n".join(lines)
        
        print(f"📝 Текст подготовлен ({len(text)} символов)")
        print("🎙️ Создаю аудио файл (это может занять несколько минут)...")
        
        # Используем русский голос
        voice = "ru-RU-SvetlanaNeural"  # Женский голос
        # Альтернативы: "ru-RU-DmitryNeural" (мужской)
        
        # Создаем аудио (асинхронно)
        asyncio.run(create_audio_async(text, output_file, voice))
        
        if output_file.exists():
            print(f"✅ Аудио файл создан: {output_file}")
            print(f"📊 Размер файла: {output_file.stat().st_size / 1024 / 1024:.2f} MB")
            return True
        else:
            print("❌ Файл не был создан")
            return False
        
    except ImportError:
        print("❌ Библиотека edge-tts не установлена")
        print("📦 Установите: pip install edge-tts")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


def create_audio_with_gtts():
    """
    Использует Google Text-to-Speech (бесплатно, требует интернет)
    Требует: pip install gtts
    """
    try:
        from gtts import gTTS
        
        # Читаем файл
        text_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_ПОЛНАЯ_v2.txt"
        output_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_АУДИО.mp3"
        
        if not text_file.exists():
            print(f"❌ Файл не найден: {text_file}")
            return False
        
        print("📖 Читаю файл философии...")
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Убираем лишние символы
        text = text.replace("═══════════════════════════════════════════════════════════════════", "")
        text = text.replace("───────────────────────────────────────────────────────────────────", "")
        lines = [line.strip() for line in text.split("\n") if line.strip() and not line.strip().startswith("═")]
        text = "\n".join(lines)
        
        print(f"📝 Текст подготовлен ({len(text)} символов)")
        print("🎙️ Создаю аудио файл через Google TTS...")
        
        # Создаем аудио (русский язык)
        tts = gTTS(text=text, lang='ru', slow=False)
        tts.save(str(output_file))
        
        print(f"✅ Аудио файл создан: {output_file}")
        return True
        
    except ImportError:
        print("❌ Библиотека gtts не установлена")
        print("📦 Установите: pip install gtts")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


def main():
    print("🎙️ КОНВЕРТАЦИЯ ТЕКСТА В АУДИО")
    print("=" * 60)
    print()
    
    # Пробуем edge-tts (лучшее качество, бесплатно)
    print("Попытка 1: Microsoft Edge TTS (рекомендуется)")
    if create_audio_with_edge_tts():
        return
    
    print()
    print("Попытка 2: Google Text-to-Speech")
    if create_audio_with_gtts():
        return
    
    print()
    print("❌ Не удалось создать аудио автоматически")
    print("📋 См. инструкцию по использованию онлайн сервисов ниже")


if __name__ == "__main__":
    main()

