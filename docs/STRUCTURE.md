# 📁 СТРУКТУРА ПРОЕКТА AI-COMPANY-PROMOTION

**Версия:** 2.0  
**Дата обновления:** 27 ноября 2025  
**Принцип:** Best practices для проектов документации и автоматизации

---

## 🎯 ПРИНЦИПЫ ОРГАНИЗАЦИИ

1. **Разделение по назначению** (executive, technical, brand)
2. **Хронология** (changelog, daily updates)
3. **Типы контента** (prompts, instructions, analysis)
4. **Версионирование** (по датам и версиям)
5. **Легкая навигация** (README в каждой папке)

---

## 📂 ПОЛНАЯ СТРУКТУРА

```
ai-company-promotion/
│
├── 📄 README.md                          ← Главная точка входа
├── 📄 requirements.txt                   ← Python зависимости
├── 📄 .gitignore                         ← Git настройки
│
├── 📁 automation/                       ← Python скрипты
│   ├── __init__.py
│   ├── ai_monitor.py                    ← Мониторинг упоминаний в AI
│   ├── content_generator.py             ← Генератор контента
│   ├── schema_generator.py              ← Генератор Schema.org
│   ├── transcribe_audio.py              ← Транскрибация аудио
│   └── README.md
│
├── 📁 config/                            ← Конфигурация
│   └── config.example.env               ← Шаблон .env
│
├── 📁 data/                              ← Данные проекта
│   └── input/                            ← Входные данные
│       ├── Alexandr voice/               ← Голосовые записи директора
│       └── *.docx, *.m4a                ← Документы и аудио
│
├── 📁 docs/                              ← ВСЯ ДОКУМЕНТАЦИЯ
│   │
│   ├── 📁 brand/                         ← БРЕНД И ИДЕНТИЧНОСТЬ
│   │   ├── philosophy/                   ← Философия компании
│   │   │   ├── ФИЛОСОФИЯ_DIMKAVA_ОТ_АЛЕКСАНДРА.txt
│   │   │   └── СПРАВКА_ФИЛОСОФИЯ.md
│   │   ├── identity/                    ← Идентичность для AI
│   │   │   └── DIMKAVA_IDENTITY_PROMPT.md
│   │   └── README.md
│   │
│   ├── 📁 executive/                     ← ДЛЯ РУКОВОДСТВА
│   │   ├── presentations/                ← Презентации
│   │   ├── reports/                      ← Отчеты для директора
│   │   │   ├── ДЛЯ_ДИРЕКТОРА.md
│   │   │   └── записка_директору.txt
│   │   ├── planning/                     ← Планирование
│   │   │   ├── miro_board_plan.md
│   │   │   ├── miro_import.csv
│   │   │   ├── jira_import_block1_v2.csv
│   │   │   └── restructured_tasks.md
│   │   ├── team/                         ← Команда и задачи
│   │   │   ├── job_descriptions.md
│   │   │   ├── team_tasks_readable.txt
│   │   │   └── technical_instructions.md
│   │   └── README.md
│   │
│   ├── 📁 technical/                     ← ТЕХНИЧЕСКАЯ ДОКУМЕНТАЦИЯ
│   │   ├── instructions/                 ← Инструкции
│   │   │   ├── ИНСТРУКЦИЯ_API_КЛЮЧИ.md
│   │   │   ├── КАК_ИСПОЛЬЗОВАТЬ.md
│   │   │   ├── ОБНОВЛЕНИЕ_ПРОЕКТА.md
│   │   │   └── ТРАНСКРИБАЦИЯ_АУДИО.md
│   │   ├── api/                          ← API документация
│   │   └── README.md
│   │
│   ├── 📁 analysis/                       ← АНАЛИТИКА И ОТЧЕТЫ
│   │   ├── ANALYSIS.md
│   │   ├── LOCATION_UPDATE.md
│   │   ├── SUMMARY_AI_PROMOTION.md
│   │   └── README.md
│   │
│   ├── 📁 changelog/                      ← ИСТОРИЯ ИЗМЕНЕНИЙ
│   │   ├── 2025-11-27/                   ← Изменения за сегодня
│   │   │   ├── philosophy_analysis.md    ← Анализ философии
│   │   │   └── README.md
│   │   └── README.md
│   │
│   ├── 📁 transcriptions/                  ← ТРАНСКРИПЦИИ
│   │   └── README.md
│   │
│   └── 📁 strategy/                       ← СТРАТЕГИИ (если нужны отдельно)
│       └── README.md
│
├── 📁 prompts/                            ← AI ПРОМПТЫ И СТРАТЕГИЯ
│   ├── START_HERE.md                     ← Точка входа
│   ├── ai-promotion-strategy.md          ← Полная стратегия
│   ├── ai-promotion-quickstart.md
│   ├── ai-promotion-question.md
│   ├── ai-tools-recommendations.md
│   ├── LOCATION_STRATEGY_GEORGIA.md
│   ├── DIMKAVA_IDENTITY_PROMPT.md        ← (будет перемещен в docs/brand/)
│   │
│   ├── 📁 answers/                       ← Ответы от AI
│   │   ├── chatgpt-answer.md
│   │   ├── gemini-answer.md
│   │   ├── claude-answer.md
│   │   ├── perplexity-answer.md
│   │   ├── mistral-answer.md
│   │   ├── duck-ai-answer.md
│   │   ├── cursor-answer.md
│   │   └── README.md
│   │
│   ├── 📁 platform-specific/             ← Промпты для конкретных AI
│   │   ├── chatgpt_prompt.md
│   │   ├── gemini_prompt.md
│   │   ├── claude_prompt.md
│   │   ├── mistral_prompt.md
│   │   └── deepseek_prompt.md
│   │
│   └── README.md
│
├── 📁 reports/                            ← ОТЧЕТЫ АВТОМАТИЗАЦИИ
│   └── ai_monitor_*.json                 ← JSON отчеты мониторинга
│
├── 📁 templates/                           ← ШАБЛОНЫ
│   └── articles/                         ← Шаблоны статей (на будущее)
│
└── 📁 venv/                               ← Python виртуальное окружение
```

---

## 📋 ОПИСАНИЕ ПАПОК

### `docs/brand/` - БРЕНД И ИДЕНТИЧНОСТЬ
**Назначение:** Вся информация о философии, ценностях, идентичности DimKava

**Структура:**
- `philosophy/` - Философия компании (слова Александра)
- `identity/` - Идентичность для AI (промпты)

**Кто использует:** Все (маркетинг, HR, IT, руководство)

---

### `docs/executive/` - ДЛЯ РУКОВОДСТВА
**Назначение:** Документы для директора и менеджмента

**Структура:**
- `presentations/` - Презентации
- `reports/` - Отчеты и записки
- `planning/` - Планирование (Miro, Jira)
- `team/` - Команда и задачи

**Кто использует:** Директор, менеджмент

---

### `docs/technical/` - ТЕХНИЧЕСКАЯ ДОКУМЕНТАЦИЯ
**Назначение:** Инструкции, API, технические гайды

**Структура:**
- `instructions/` - Пошаговые инструкции
- `api/` - API документация

**Кто использует:** IT, разработчики, технические специалисты

---

### `docs/analysis/` - АНАЛИТИКА
**Назначение:** Анализ, отчеты, сводки

**Кто использует:** Все для понимания текущего состояния

---

### `docs/changelog/` - ИСТОРИЯ ИЗМЕНЕНИЙ
**Назначение:** Хронология изменений по датам

**Структура:**
- `YYYY-MM-DD/` - Папки по датам
- Каждая папка содержит изменения за день

**Кто использует:** Все для отслеживания прогресса

---

### `docs/transcriptions/` - ТРАНСКРИПЦИИ
**Назначение:** Расшифровки аудио (голосовые записи, интервью)

**Кто использует:** Все для работы с исходными материалами

---

### `prompts/` - AI ПРОМПТЫ
**Назначение:** Стратегия продвижения, промпты для AI

**Структура:**
- Основные файлы стратегии
- `answers/` - Ответы от разных AI
- `platform-specific/` - Промпты для конкретных платформ

**Кто использует:** Все кто работает с AI

---

## 🎯 BEST PRACTICES

### 1. **README в каждой папке**
Каждая папка должна иметь README.md с описанием содержимого

### 2. **Версионирование**
- Файлы с датами: `YYYY-MM-DD_description.md`
- Версии в названиях: `_v2`, `_v3`

### 3. **Именование файлов**
- Английские названия для технических файлов
- Кириллица для бизнес-документов (если команда русскоязычная)
- Без пробелов, используйте `_` или `-`

### 4. **Разделение по ролям**
- `executive/` - для руководства
- `technical/` - для технических специалистов
- `brand/` - для всех (философия)

### 5. **Хронология**
- `changelog/` - для истории изменений
- Датированные папки для больших обновлений

---

## 📖 НАВИГАЦИЯ

**Хочу начать работу:**
→ `prompts/START_HERE.md`

**Нужна философия компании:**
→ `docs/brand/philosophy/ФИЛОСОФИЯ_DIMKAVA_ОТ_АЛЕКСАНДРА.txt`

**Показать директору:**
→ `docs/executive/reports/ДЛЯ_ДИРЕКТОРА.md`

**Настроить API:**
→ `docs/technical/instructions/ИНСТРУКЦИЯ_API_КЛЮЧИ.md`

**Что изменилось сегодня:**
→ `docs/changelog/2025-11-27/`

**Запустить мониторинг:**
→ `python automation/ai_monitor.py`

---

*Структура обновлена: 27 ноября 2025*

