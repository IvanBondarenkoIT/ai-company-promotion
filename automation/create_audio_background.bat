@echo off
chcp 65001 >nul
echo 🎙️ Создание аудио файла...
echo ⏳ Это может занять 5-15 минут, пожалуйста, подождите...
echo.
python automation\text_to_speech_fixed.py
echo.
echo ✅ Готово! Проверьте файл: docs\brand\philosophy\ФИЛОСОФИЯ_DIMKAVA_АУДИО.mp3
pause








