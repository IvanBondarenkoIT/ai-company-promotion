# Обновление стратегии AI-поиска (GEO) — DimKava

Отдельная зона работы, чтобы **не смешивать** с исходными материалами в `prompts/` и `docs/analysis/`.

## Зачем эта папка

Исходная стратегия собрана в **ноябре–декабре 2025** (`prompts/ai-promotion-strategy.md`, `SUMMARY_AI_PROMOTION.md`, `START_HERE.md`). Рынок AI-поиска и поведение моделей меняются быстро; нужны:

- систематический **разбор** того, что ещё верно;
- учёт **новых трендов 2026** (AI Overviews, цитирование, zero-click, метрики GEO);
- **новая версия стратегии** с приоритетами и KPI под DimKava сегодня.

## Файлы в этой директории

| Файл | Назначение |
|------|------------|
| `ANALYSIS_PLAN.md` | План анализа: что перечитать, что проверить на сайте/в GMB, какие гипотезы проверить |
| `STRATEGY_DEVELOPMENT_PLAN.md` | План разработки новой стратегии: этапы, артефакты, роли, сроки |
| `CURRENT_STRATEGY_REVIEW.md` | Первичный разбор: сильные стороны старой стратегии, риски устаревания, корректировки, наводящие вопросы |
| `STRATEGY_BRIEF.md` | Краткий бриф v2: цель, языки, роли, факты по сайту/GMB |
| `ROADMAP_90_DAYS.md` | Дорожная карта 90 дней |
| `QUERY_MATRIX.md` | Матрица запросов EN/KA/RU |
| `GEO_MANUAL_TEST_PROTOCOL.md` | Как вести ручные GEO-тесты |
| `GEO_BASELINE_TEST_TRACKER.md` | **Таблицы baseline** (EN 15 + KA 10 + RU 5 запросов) для заполнения |
| `ANSWER_FIRST_KEY_FACTS_TEMPLATES.md` | **Quick answer / Key facts** для страниц Contacts, Service, About, FAQ (EN + KA) |
| `FAQ_EN_FOR_WEBSITE.md` | Готовый текст FAQ на английском для сайта |
| `FAQ_KA_FOR_WEBSITE.md` | Готовый текст FAQ на грузинском для сайта |
| `FAQ_RU_FOR_WEBSITE.md` | Тот же FAQ, перевод с английского (для чтения / опционально на сайт) |
| `FAQ_SCHEMA_JSONLD_EXAMPLE.md` | Пример **FAQPage** JSON-LD + инструкция |
| `GBP_SINGLE_PROFILE_PLAYBOOK.md` | Один профиль GBP: описание, Q&A, посты, ответы на отзывы |

## Исходные «канонические» документы (не дублировать — ссылаться)

- `prompts/ai-promotion-strategy.md` — полная GEO-стратегия
- `prompts/ai-promotion-quickstart.md` — быстрый старт
- `prompts/START_HERE.md` — навигация
- `docs/analysis/SUMMARY_AI_PROMOTION.md` — итоги исследования
- `docs/technical/instructions/GOOGLE_MY_BUSINESS_SETUP.md`
- `docs/technical/instructions/WORDPRESS_FAQ_SETUP.md`
- `docs/brand/company_soul_kit/` — философия и единый тон бренда

После утверждения новой версии имеет смысл добавить ссылку на эту папку в `README.md` корня проекта (отдельным коммитом по решению команды).
