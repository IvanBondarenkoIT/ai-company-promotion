# FAQPage — JSON-LD example (dimkava.ge)

Paste into the **head** of the FAQ page (or use Rank Math / Ultimate FAQ / custom HTML block).  
Replace `QUESTION` / `ANSWER` with your published text. Keep answers **short** if possible (better for rich results).

**URLs (adjust to real paths):**
- EN FAQ: `https://dimkava.ge/faq/` (example — use your real slug)
- KA FAQ: `https://dimkava.ge/ge/faq/` (example)

---

## Minimal valid example

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What coffee do you sell?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We sell Blasercafe — premium Swiss coffee. We carry about 15 varieties."
      }
    },
    {
      "@type": "Question",
      "name": "Where is Blasercafe roasted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Blasercafe sold by DimKava is roasted and packed in Switzerland at Blaser."
      }
    },
    {
      "@type": "Question",
      "name": "Do you provide official DeLonghi service in Georgia?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. DimKava provides official DeLonghi service in Georgia. Contact the service phone number listed on our website."
      }
    }
  ]
}
```

Wrap in a script tag:

```html
<script type="application/ld+json">
{ ... JSON above ... }
</script>
```

---

## Notes

- **One FAQPage per language page** — do not mix EN and KA Q&A in the same JSON-LD block.
- **Match visible FAQ** — the JSON-LD must reflect what users see on the page (Google policy).
- After publishing, validate with [Google Rich Results Test](https://search.google.com/test/rich-results) (optional).

**Full Q&A set:** generate JSON from [FAQ_EN_FOR_WEBSITE.md](FAQ_EN_FOR_WEBSITE.md) and [FAQ_KA_FOR_WEBSITE.md](FAQ_KA_FOR_WEBSITE.md) (or export from WordPress plugin).
