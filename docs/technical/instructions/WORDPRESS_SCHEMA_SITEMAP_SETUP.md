# WordPress Schema + Sitemap (DimKava)

## Что уже подготовлено

- Готовый sitemap: `data/output/seo/sitemap_dimkava.xml`
- Готовая JSON-LD schema: `data/output/seo/schema_dimkava_homepage.jsonld`

## Важно перед публикацией

- Публичные sitemap URL сейчас отдают 500:
  - `https://dimkava.ge/wp-sitemap.xml`
  - `https://dimkava.ge/ge/wp-sitemap.xml`
  - `https://dimkava.ge/en/wp-sitemap.xml`
- Поэтому используйте файл `sitemap_dimkava.xml` как временный рабочий вариант.

## Как внедрить schema в WordPress

1. Откройте `data/output/seo/schema_dimkava_homepage.jsonld`.
2. Обновите плейсхолдер:
   - `TODO: [Tbilisi address]`
3. Оберните JSON содержимое в:
   `<script type="application/ld+json"> ... </script>`
4. Вставьте на сайт:
   - через SEO-плагин в Header/Homepage schema, или
   - через плагин вставки кода в `<head>`.

## Как внедрить sitemap

1. Загрузите `data/output/seo/sitemap_dimkava.xml` в корень сайта как `sitemap.xml`.
2. Проверьте доступ:
   - `https://dimkava.ge/sitemap.xml`
3. Убедитесь, что в `robots.txt` есть строка:
   - `Sitemap: https://dimkava.ge/sitemap.xml`
4. Отправьте sitemap в Google Search Console.

## Что добавить после восстановления автогенерации sitemap

- Когда `wp-sitemap.xml` перестанет отдавать 500, можно:
  - либо оставить `sitemap.xml` как индекс-обертку,
  - либо полностью перейти обратно на WordPress sitemap.

