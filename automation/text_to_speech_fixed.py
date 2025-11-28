#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Улучшенный скрипт для конвертации текста в аудио
Разбивает длинный текст на части и объединяет результат
"""

import sys
from pathlib import Path
import time

# Fix Windows UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def clean_text(text):
    """Очищает текст от форматирования"""
    # Убираем декоративные символы
    text = text.replace("═══════════════════════════════════════════════════════════════════", "")
    text = text.replace("───────────────────────────────────────────────────────────────────", "")
    text = text.replace("┌", "").replace("┐", "").replace("└", "").replace("┘", "")
    text = text.replace("├", "").replace("┤", "").replace("│", "")
    text = text.replace("─", " ").replace("═", " ")
    
    # Оставляем только текст
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        if line and not line.startswith("═") and not line.startswith("─"):
            lines.append(line)
    
    return "\n".join(lines)


def split_text_into_chunks(text, max_chars=4500):
    """
    Разбивает текст на части по max_chars символов
    Старается разбивать по абзацам
    """
    chunks = []
    current_chunk = ""
    
    # Разбиваем по двойным переносам строк (абзацы)
    paragraphs = text.split("\n\n")
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
            
        # Если параграф сам по себе больше лимита, разбиваем по предложениям
        if len(para) > max_chars:
            sentences = para.split(". ")
            for sentence in sentences:
                if len(current_chunk) + len(sentence) + 2 <= max_chars:
                    current_chunk += sentence + ". "
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = sentence + ". "
        else:
            # Проверяем, поместится ли параграф
            if len(current_chunk) + len(para) + 2 <= max_chars:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks


def create_audio_with_gtts_chunks(text_file, output_file):
    """
    Создает аудио через Google TTS, разбивая текст на части
    """
    try:
        from gtts import gTTS
        from pydub import AudioSegment
        import os
        
        print("📖 Читаю файл философии...")
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Очищаем текст
        text = clean_text(text)
        print(f"📝 Текст подготовлен ({len(text)} символов)")
        
        # Разбиваем на части
        chunks = split_text_into_chunks(text, max_chars=4500)
        print(f"✂️ Текст разбит на {len(chunks)} частей")
        
        # Создаем временную папку
        temp_dir = output_file.parent / "temp_audio"
        temp_dir.mkdir(exist_ok=True)
        
        audio_files = []
        
        # Создаем аудио для каждой части
        for i, chunk in enumerate(chunks, 1):
            print(f"🎙️ Создаю часть {i}/{len(chunks)}...")
            temp_file = temp_dir / f"part_{i:03d}.mp3"
            
            try:
                tts = gTTS(text=chunk, lang='ru', slow=False)
                tts.save(str(temp_file))
                
                # Проверяем, что файл создан и не пустой
                if temp_file.exists() and temp_file.stat().st_size > 0:
                    audio_files.append(str(temp_file))
                    print(f"  ✅ Часть {i} создана ({temp_file.stat().st_size / 1024:.1f} KB)")
                else:
                    print(f"  ❌ Часть {i} не создана или пустая")
                    return False
                    
                # Небольшая задержка между запросами
                time.sleep(1)
                
            except Exception as e:
                print(f"  ❌ Ошибка при создании части {i}: {e}")
                return False
        
        # Объединяем все части
        if len(audio_files) == 0:
            print("❌ Не создано ни одной части")
            return False
        
        print("🔗 Объединяю части в один файл...")
        
        if len(audio_files) == 1:
            # Если только одна часть, просто копируем
            import shutil
            shutil.copy(audio_files[0], output_file)
        else:
            # Объединяем несколько файлов
            combined = AudioSegment.empty()
            for audio_file in audio_files:
                audio = AudioSegment.from_mp3(audio_file)
                combined += audio
                # Небольшая пауза между частями
                combined += AudioSegment.silent(duration=500)  # 0.5 секунды тишины
            
            combined.export(str(output_file), format="mp3")
        
        # Удаляем временные файлы
        print("🧹 Удаляю временные файлы...")
        for audio_file in audio_files:
            try:
                os.remove(audio_file)
            except:
                pass
        try:
            temp_dir.rmdir()
        except:
            pass
        
        if output_file.exists() and output_file.stat().st_size > 0:
            size_mb = output_file.stat().st_size / 1024 / 1024
            print(f"✅ Аудио файл создан: {output_file}")
            print(f"📊 Размер файла: {size_mb:.2f} MB")
            return True
        else:
            print("❌ Финальный файл не создан или пустой")
            return False
        
    except ImportError as e:
        print(f"❌ Не установлена необходимая библиотека: {e}")
        print("📦 Установите: pip install gtts pydub")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


def create_audio_simple_gtts(text_file, output_file):
    """
    Простой вариант без объединения (если pydub не установлен)
    """
    try:
        from gtts import gTTS
        
        print("📖 Читаю файл философии...")
        with open(text_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Очищаем текст
        text = clean_text(text)
        print(f"📝 Текст подготовлен ({len(text)} символов)")
        
        # Если текст слишком длинный, берем первую часть
        if len(text) > 5000:
            print("⚠️ Текст слишком длинный, беру первую часть (5000 символов)")
            text = text[:5000] + "..."
        
        print("🎙️ Создаю аудио файл (это может занять несколько минут)...")
        
        # Создаем аудио (русский язык)
        tts = gTTS(text=text, lang='ru', slow=False)
        tts.save(str(output_file))
        
        if output_file.exists() and output_file.stat().st_size > 0:
            size_mb = output_file.stat().st_size / 1024 / 1024
            print(f"✅ Аудио файл создан: {output_file}")
            print(f"📊 Размер файла: {size_mb:.2f} MB")
            return True
        else:
            print("❌ Файл не создан или пустой")
            return False
        
    except ImportError:
        print("❌ Библиотека gtts не установлена")
        print("📦 Установите: pip install gtts")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("🎙️ КОНВЕРТАЦИЯ ТЕКСТА В АУДИО (УЛУЧШЕННАЯ ВЕРСИЯ)")
    print("=" * 60)
    print()
    
    # Пути к файлам
    text_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_ПОЛНАЯ_v2.txt"
    output_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_АУДИО.mp3"
    
    if not text_file.exists():
        print(f"❌ Файл не найден: {text_file}")
        return
    
    # Пробуем создать с объединением частей
    print("Попытка 1: Google TTS с разбивкой на части (рекомендуется)")
    if create_audio_with_gtts_chunks(text_file, output_file):
        return
    
    print()
    print("Попытка 2: Google TTS (простой вариант)")
    if create_audio_simple_gtts(text_file, output_file):
        return
    
    print()
    print("❌ Не удалось создать аудио автоматически")
    print("📋 Используйте онлайн сервис TTSMaker: https://ttsmaker.com/")


if __name__ == "__main__":
    main()

