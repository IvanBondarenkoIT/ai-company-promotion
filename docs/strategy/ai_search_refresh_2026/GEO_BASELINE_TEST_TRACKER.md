# GEO Baseline — трекер ручных тестов (DimKava)

**Назначение:** зафиксировать **baseline** до/после изменений на сайте и в GBP.  
**Протокол оценки:** [GEO_MANUAL_TEST_PROTOCOL.md](GEO_MANUAL_TEST_PROTOCOL.md)

## Как заполнять

1. Выберите **2–3 движка** на каждый прогон (рекомендуется: Perplexity + ChatGPT + Google/Gemini).
2. Для каждой строки: выполните запрос **на языке колонки** (EN / KA / RU).
3. Оценки:
   - **Presence:** `Y` = упомянут DimKava / Dim Kava, `N` = нет.
   - **Citation:** `Y` = есть ссылка или явная цитата `dimkava.ge` / Google Business, `N` = нет, `?` = косвенно.
   - **Accuracy (0–2):** 0 = фактические ошибки (город, сервис, бренды), 1 = частично верно, 2 = верно.
   - **Fidelity (0–2):** 0 = нет смысла бренда (полный цикл, наслаждение, сервис), 1 = частично, 2 = отражает.

4. После заполнения посчитайте:
   - **Presence rate** = (число Y в Presence) / (число ячеек с тестом)
   - **Citation rate** = (число Y в Citation) / (число ячеек)

**Дата baseline (заполнить):** _______________

---

## Таблица A — EN (15 запросов)

| # | Запрос | Engine 1 | Presence | Citation | Acc | Fid | Engine 2 | Presence | Citation | Acc | Fid | Комментарий |
|---|--------|----------|----------|----------|-----|-----|----------|----------|----------|-----|-----|-------------|
| 1 | DeLonghi service center in Tbilisi | | | | | | | | | | | |
| 2 | DeLonghi service center in Batumi | | | | | | | | | | | |
| 3 | coffee machine repair Tbilisi DeLonghi | | | | | | | | | | | |
| 4 | coffee machine repair Batumi | | | | | | | | | | | |
| 5 | official DeLonghi service in Georgia | | | | | | | | | | | |
| 6 | where to buy coffee beans in Tbilisi | | | | | | | | | | | |
| 7 | premium coffee beans Tbilisi | | | | | | | | | | | |
| 8 | Swiss coffee Blasercafe Georgia | | | | | | | | | | | |
| 9 | Blasercafe coffee beans Tbilisi | | | | | | | | | | | |
| 10 | coffee beans shop Batumi | | | | | | | | | | | |
| 11 | coffee tasting Tbilisi espresso | | | | | | | | | | | |
| 12 | degustation coffee Tbilisi | | | | | | | | | | | |
| 13 | coffee shop Batumi with coffee beans | | | | | | | | | | | |
| 14 | DimKava Tbilisi | | | | | | | | | | | |
| 15 | DimKava Batumi | | | | | | | | | | | |

---

## Таблица B — KA (10 запросов)

| # | Запрос | Engine 1 | Presence | Citation | Acc | Fid | Комментарий |
|---|--------|----------|----------|----------|-----|-----|-------------|
| 1 | DeLonghi-ის ოფიციალური სერვისი საქართველოში | | | | | | |
| 2 | DeLonghi-ის სერვის ცენტრი თბილისში | | | | | | |
| 3 | ყავის აპარატის შეკეთება ბათუმში | | | | | | |
| 4 | სად ვიყიდო მარცვლოვანი ყავა თბილისში | | | | | | |
| 5 | პრემიუმ ყავა ბათუმში სად ვიყიდო | | | | | | |
| 6 | Blasercafe ყავა საქართველოში | | | | | | |
| 7 | DimKava თბილისი | | | | | | |
| 8 | DimKava ბათუმი | | | | | | |
| 9 | ყავის დეგუსტაცია თბილისში | | | | | | |
| 10 | ყავის აპარატი DeLonghi თბილისი | | | | | | |

---

## Таблица C — RU (5 запросов, минимум)

| # | Запрос | Engine 1 | Presence | Citation | Acc | Fid | Комментарий |
|---|--------|----------|----------|----------|-----|-----|-------------|
| 1 | официальный сервис Delonghi в Грузии | | | | | | |
| 2 | ремонт кофемашин Delonghi Тбилиси | | | | | | |
| 3 | где купить кофе в зернах Тбилиси | | | | | | |
| 4 | DimKava Тбилиси | | | | | | |
| 5 | DimKava Батуми | | | | | | |

---

## Сводка после прогона

| Метрика | Значение |
|---------|----------|
| Presence rate (все запросы) | ___ % |
| Citation rate | ___ % |
| Средняя Accuracy | ___ |
| Средняя Fidelity | ___ |

**Следующий повтор (через 4 недели после изменений):** дата _______________
