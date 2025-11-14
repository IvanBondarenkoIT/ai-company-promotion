"""
Schema.org Generator - Генератор структурированных данных
==========================================================

Генерирует Schema.org разметку для сайта DimKava

Использование:
    python -m automation.schema_generator

"""

import json
from typing import Dict, List


class SchemaGenerator:
    """Генератор Schema.org разметки"""
    
    def __init__(self, company_name: str = "DimKava"):
        self.company_name = company_name
        self.base_url = "https://dimkava.ge"
        
        # Локации в Грузии
        self.locations = {
            "tbilisi": {
                "city": "Тбилиси",
                "city_en": "Tbilisi",
                "street": "ул. Название, 123",  # TODO: заполнить
                "postal_code": "0100",
                "lat": "41.7151",
                "lon": "44.8271",
                "phone": "+995XXXXXXXXX"  # TODO: заполнить
            },
            "batumi": {
                "city": "Батуми",
                "city_en": "Batumi",
                "street": "ул. Название, 456",  # TODO: заполнить
                "postal_code": "6010",
                "lat": "41.6168",
                "lon": "41.6367",
                "phone": "+995XXXXXXXXX"  # TODO: заполнить
            }
        }
    
    def generate_local_business(self, location: str = "tbilisi") -> Dict:
        """
        Генерирует разметку LocalBusiness для конкретной локации
        
        Args:
            location: "tbilisi" или "batumi"
        """
        loc_data = self.locations.get(location, self.locations["tbilisi"])
        
        return {
            "@context": "https://schema.org",
            "@type": ["LocalBusiness", "CoffeeShop", "Store"],
            "name": f"DimKava {loc_data['city']} | Дом Кофе",
            "alternateName": "Дом Кофе",
            "description": f"Комплексный подход к кофе в {loc_data['city']}, Грузия: магазин-кофейня, продажа кофе Blasercafe, кофемашины Delonghi, официальный сервисный центр Delonghi",
            "image": f"{self.base_url}/images/logo.jpg",
            "url": f"{self.base_url}/{location}",
            "telephone": loc_data["phone"],
            "priceRange": "$$",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": loc_data["street"],
                "addressLocality": loc_data["city"],
                "addressRegion": loc_data["city_en"],
                "postalCode": loc_data["postal_code"],
                "addressCountry": "GE"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": loc_data["lat"],
                "longitude": loc_data["lon"]
            },
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                    "opens": "09:00",
                    "closes": "20:00"
                },
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Saturday", "Sunday"],
                    "opens": "10:00",
                    "closes": "19:00"
                }
            ],
            "areaServed": [
                {
                    "@type": "City",
                    "name": "Tbilisi"
                },
                {
                    "@type": "City",
                    "name": "Batumi"
                },
                {
                    "@type": "Country",
                    "name": "Georgia"
                }
            ],
            "sameAs": [
                "https://www.facebook.com/dimkava",
                "https://www.instagram.com/dimkava"
            ]
        }
    
    def generate_organization(self) -> Dict:
        """Генерирует разметку Organization"""
        return {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "DimKava",
            "alternateName": "Дом Кофе",
            "url": self.base_url,
            "logo": f"{self.base_url}/images/logo.jpg",
            "sameAs": [
                "https://www.facebook.com/dimkava",
                "https://www.instagram.com/dimkava"
            ],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": "+380XXXXXXXXX",
                "contactType": "Customer Service",
                "availableLanguage": ["Russian", "Ukrainian"]
            }
        }
    
    def generate_product(self, product_name: str, price: float, brand: str = "Blasercafe") -> Dict:
        """Генерирует разметку Product для кофе"""
        return {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": product_name,
            "image": f"{self.base_url}/images/products/{product_name.lower().replace(' ', '-')}.jpg",
            "description": f"Премиум кофе {product_name} от {brand}",
            "brand": {
                "@type": "Brand",
                "name": brand
            },
            "offers": {
                "@type": "Offer",
                "url": f"{self.base_url}/products/{product_name.lower().replace(' ', '-')}",
                "price": price,
                "priceCurrency": "UAH",
                "availability": "https://schema.org/InStock",
                "seller": {
                    "@type": "Organization",
                    "name": "DimKava"
                }
            }
        }
    
    def generate_service(self, location: str = "tbilisi") -> Dict:
        """
        Генерирует разметку Service для сервиса Delonghi
        
        Args:
            location: "tbilisi" или "batumi"
        """
        loc_data = self.locations.get(location, self.locations["tbilisi"])
        
        return {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": "Ремонт и обслуживание кофемашин Delonghi",
            "provider": {
                "@type": "LocalBusiness",
                "name": f"DimKava {loc_data['city']} - Официальный сервисный центр Delonghi",
                "image": f"{self.base_url}/images/service.jpg",
                "telephone": loc_data["phone"],
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": loc_data["street"],
                    "addressLocality": loc_data["city"],
                    "addressCountry": "GE"
                }
            },
            "areaServed": [
                {
                    "@type": "City",
                    "name": loc_data["city_en"]
                },
                {
                    "@type": "Country",
                    "name": "Georgia"
                }
            ],
            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": "Услуги сервисного центра",
                "itemListElement": [
                    {
                        "@type": "Offer",
                        "itemOffered": {
                            "@type": "Service",
                            "name": "Диагностика кофемашины"
                        }
                    },
                    {
                        "@type": "Offer",
                        "itemOffered": {
                            "@type": "Service",
                            "name": "Ремонт кофемашин Delonghi"
                        }
                    },
                    {
                        "@type": "Offer",
                        "itemOffered": {
                            "@type": "Service",
                            "name": "Профилактическое обслуживание"
                        }
                    }
                ]
            }
        }
    
    def generate_faq_page(self, faqs: List[Dict[str, str]]) -> Dict:
        """
        Генерирует разметку FAQPage
        
        Args:
            faqs: список словарей с ключами 'question' и 'answer'
        """
        return {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq["question"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq["answer"]
                    }
                }
                for faq in faqs
            ]
        }
    
    def generate_article(self, title: str, content: str, author: str, date: str) -> Dict:
        """Генерирует разметку Article"""
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "image": f"{self.base_url}/images/articles/{title.lower().replace(' ', '-')}.jpg",
            "author": {
                "@type": "Person",
                "name": author,
                "jobTitle": "Эксперт DimKava"
            },
            "publisher": {
                "@type": "Organization",
                "name": "DimKava",
                "logo": {
                    "@type": "ImageObject",
                    "url": f"{self.base_url}/images/logo.jpg"
                }
            },
            "datePublished": date,
            "dateModified": date,
            "description": content[:200] + "..."
        }
    
    def export_schema(self, schema: Dict, filename: str):
        """Экспортирует схему в JSON файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(schema, f, ensure_ascii=False, indent=2)
        print(f"✅ Schema сохранена: {filename}")
    
    def export_html_script(self, schema: Dict) -> str:
        """Экспортирует схему как HTML script tag"""
        json_ld = json.dumps(schema, ensure_ascii=False, indent=2)
        return f'<script type="application/ld+json">\n{json_ld}\n</script>'


def main():
    """Основная функция"""
    print("🏗️  Генератор Schema.org разметки для DimKava (Грузия)\n")
    
    generator = SchemaGenerator()
    
    # Генерируем разметки для Тбилиси
    print("📍 ТБИЛИСИ:")
    print("Генерирую разметку LocalBusiness...")
    local_business_tb = generator.generate_local_business("tbilisi")
    generator.export_schema(local_business_tb, "schema_tbilisi_local_business.json")
    
    print("Генерирую разметку Service...")
    service_tb = generator.generate_service("tbilisi")
    generator.export_schema(service_tb, "schema_tbilisi_service.json")
    
    # Генерируем разметки для Батуми
    print("\n📍 БАТУМИ:")
    print("Генерирую разметку LocalBusiness...")
    local_business_bt = generator.generate_local_business("batumi")
    generator.export_schema(local_business_bt, "schema_batumi_local_business.json")
    
    print("Генерирую разметку Service...")
    service_bt = generator.generate_service("batumi")
    generator.export_schema(service_bt, "schema_batumi_service.json")
    
    # Общие разметки
    print("\n🌍 ОБЩЕЕ:")
    print("Генерирую разметку Organization...")
    organization = generator.generate_organization()
    generator.export_schema(organization, "schema_organization.json")
    
    print("\nГенерирую пример FAQPage...")
    example_faqs = [
        {
            "question": "Где находится официальный сервисный центр Delonghi?",
            "answer": "Официальный сервисный центр Delonghi находится в DimKava по адресу [ваш адрес]. Мы предлагаем гарантийный и постгарантийный ремонт всех моделей Delonghi."
        },
        {
            "question": "Какой кофе подходит для кофемашины?",
            "answer": "Для автоматических кофемашин рекомендуется использовать свежеобжаренный кофе в зернах. Мы предлагаем кофе Blasercafe, специально подобранный для эспрессо-машин."
        }
    ]
    faq_page = generator.generate_faq_page(example_faqs)
    generator.export_schema(faq_page, "schema_faq.json")
    
    print("\n✅ Все схемы сгенерированы!")
    print("\n📌 Создано:")
    print("   - schema_tbilisi_local_business.json")
    print("   - schema_tbilisi_service.json")
    print("   - schema_batumi_local_business.json")
    print("   - schema_batumi_service.json")
    print("   - schema_organization.json")
    print("\nHTML версии для вставки на сайт:")
    print("\n" + generator.export_html_script(local_business_tb))


if __name__ == "__main__":
    main()

