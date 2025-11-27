#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для разбивки длинного текста на части для TTS
(если сервис имеет ограничение на длину)
"""

import sys
from pathlib import Path

# Fix Windows UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def split_text(text, max_length=4000):
    """Разбивает текст на части по max_length символов"""
    parts = []
    current_part = ""
    
    # Разбиваем по абзацам
    paragraphs = text.split("\n\n")
    
    for para in paragraphs:
        if len(current_part) + len(para) + 2 <= max_length:
            current_part += para + "\n\n"
        else:
            if current_part:
                parts.append(current_part.strip())
            current_part = para + "\n\n"
    
    if current_part:
        parts.append(current_part.strip())
    
    return parts


def main():
    text_file = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "ФИЛОСОФИЯ_DIMKAVA_ПОЛНАЯ_v2.txt"
    output_dir = Path(__file__).parent.parent / "docs" / "brand" / "philosophy" / "tts_parts"
    
    if not text_file.exists():
        print(f"❌ Файл не найден: {text_file}")
        return
    
    output_dir.mkdir(exist_ok=True)
    
    print("📖 Читаю файл...")
    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Убираем лишние символы форматирования
    text = text.replace("═══════════════════════════════════════════════════════════════════", "")
    text = text.replace("───────────────────────────────────────────────────────────────────", "")
    text = text.replace("┌", "").replace("┐", "").replace("└", "").replace("┘", "")
    text = text.replace("├", "").replace("┤", "").replace("│", "")
    text = text.replace("─", " ").replace("═", " ")
    
    print("✂️ Разбиваю на части...")
    parts = split_text(text, max_length=4000)
    
    print(f"✅ Создано {len(parts)} частей")
    
    for i, part in enumerate(parts, 1):
        output_file = output_dir / f"Часть_{i:02d}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(part)
        print(f"  ✅ {output_file.name} ({len(part)} символов)")
    
    print(f"\n📁 Все части сохранены в: {output_dir}")
    print("💡 Теперь можно конвертировать каждую часть отдельно в TTSMaker")


if __name__ == "__main__":
    main()

