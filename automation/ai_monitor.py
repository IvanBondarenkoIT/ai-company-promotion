"""
AI Monitor - Мониторинг упоминаний DimKava в AI-системах
==========================================================

🇬🇪 DimKava в Грузии: Тбилиси | Батуми

Этот модуль позволяет автоматически тестировать как различные AI
отвечают на запросы, связанные с кофе, оборудованием и сервисом
в Тбилиси, Батуми и Грузии.

Использование:
    python -m automation.ai_monitor

Функции:
- Тестирование ChatGPT, Gemini, Claude, Perplexity
- Проверка упоминаний бренда DimKava в локальном контексте (Грузия)
- Мультиязычные запросы (русский, английский)
- Генерация отчетов
- Отслеживание динамики

Тестовые запросы включают:
- Русские запросы (Тбилиси, Батуми, Грузия)
- Английские запросы (для туристов)
- Смешанные запросы

"""

import os
from datetime import datetime
from typing import List, Dict
import json

# Попытка загрузить .env файл
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️  Модуль python-dotenv не установлен. Установите: pip install python-dotenv")
    print("    Переменные окружения будут загружены из системы.")

# Тестовые запросы для проверки (с учетом локации в Грузии)
TEST_QUERIES = [
    # Русские запросы - Тбилиси
    "Где купить качественный кофе в зернах в Тбилиси?",
    "Кто ремонтирует кофемашины Delonghi в Тбилиси?",
    "Где отремонтировать кофемашину Delonghi в Тбилиси?",
    "Официальный сервис Delonghi в Грузии",
    "Посоветуйте кофейню с хорошим кофе в Тбилиси",
    
    # Русские запросы - Батуми
    "Где купить кофемашину Delonghi в Батуми?",
    "Хорошая кофейня в Батуми",
    "Ремонт кофемашин в Батуми",
    
    # Русские запросы - Грузия (общие)
    "Где найти официальный сервис Delonghi в Грузии?",
    "Купить швейцарский кофе Blasercafe в Грузии",
    "Где купить кофе в зернах в Грузии?",
    
    # Английские запросы (для туристов)
    "Best coffee shop in Tbilisi",
    "Where to buy Delonghi coffee machine in Tbilisi",
    "Delonghi service center in Georgia",
    "Coffee machine repair Tbilisi",
    "Best coffee in Batumi",
    "Where to find good coffee in Tbilisi Georgia",
    
    # Смешанные запросы
    "Delonghi сервис Тбилиси",
    "Coffee beans Tbilisi",
    "Кофемашина ремонт Батуми",
]


class AIMonitor:
    """Мониторинг упоминаний в AI-системах"""
    
    def __init__(self, brand_name: str = "DimKava"):
        self.brand_name = brand_name
        self.results = []
    
    def test_chatgpt(self, query: str) -> Dict:
        """
        Тестирует ChatGPT на упоминание бренда
        
        NOTE: Требует API ключ OpenAI
        """
        result = {
            "ai": "ChatGPT",
            "query": query,
            "status": "not_implemented",  # success / failed / no_api_key / not_implemented
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": "",
            "error": None
        }
        
        # Проверяем наличие API ключа
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            result["status"] = "no_api_key"
            result["error"] = "API ключ не найден в .env файле"
            return result
        
        try:
            # TODO: Реализовать через OpenAI API
            # from openai import OpenAI
            # client = OpenAI(api_key=api_key)
            # response = client.chat.completions.create(...)
            # result["response_snippet"] = response.choices[0].message.content[:200]
            # result["mentioned"] = self.brand_name.lower() in response_text.lower()
            # result["status"] = "success"
            
            result["status"] = "not_implemented"
            result["error"] = "Интеграция с API еще не реализована"
            
        except Exception as e:
            result["status"] = "failed"
            result["error"] = str(e)
        
        return result
    
    def test_gemini(self, query: str) -> Dict:
        """Тестирует Google Gemini"""
        result = {
            "ai": "Gemini",
            "query": query,
            "status": "not_implemented",
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": "",
            "error": None
        }
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            result["status"] = "no_api_key"
            result["error"] = "API ключ не найден в .env файле"
            return result
        
        try:
            # TODO: Реализовать через Google AI API
            result["status"] = "not_implemented"
            result["error"] = "Интеграция с API еще не реализована"
        except Exception as e:
            result["status"] = "failed"
            result["error"] = str(e)
        
        return result
    
    def test_claude(self, query: str) -> Dict:
        """Тестирует Claude (Anthropic)"""
        result = {
            "ai": "Claude",
            "query": query,
            "status": "not_implemented",
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": "",
            "error": None
        }
        
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            result["status"] = "no_api_key"
            result["error"] = "API ключ не найден в .env файле"
            return result
        
        try:
            # TODO: Реализовать через Anthropic API
            result["status"] = "not_implemented"
            result["error"] = "Интеграция с API еще не реализована"
        except Exception as e:
            result["status"] = "failed"
            result["error"] = str(e)
        
        return result
    
    def test_perplexity(self, query: str) -> Dict:
        """Тестирует Perplexity AI"""
        result = {
            "ai": "Perplexity",
            "query": query,
            "status": "not_implemented",
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": "",
            "error": None
        }
        
        api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            result["status"] = "no_api_key"
            result["error"] = "API ключ не найден в .env файле"
            return result
        
        try:
            # TODO: Реализовать через Perplexity API
            result["status"] = "not_implemented"
            result["error"] = "Интеграция с API еще не реализована"
        except Exception as e:
            result["status"] = "failed"
            result["error"] = str(e)
        
        return result
    
    def run_full_test(self) -> Dict:
        """
        Запускает полный тест по всем AI и запросам
        
        Returns:
            Dict с результатами тестирования
        """
        results = {
            "test_date": datetime.now().isoformat(),
            "brand": self.brand_name,
            "queries_tested": len(TEST_QUERIES),
            "results": []
        }
        
        for query in TEST_QUERIES:
            query_results = {
                "query": query,
                "ai_responses": []
            }
            
            # Тестируем каждый AI
            query_results["ai_responses"].append(self.test_chatgpt(query))
            query_results["ai_responses"].append(self.test_gemini(query))
            query_results["ai_responses"].append(self.test_claude(query))
            query_results["ai_responses"].append(self.test_perplexity(query))
            
            results["results"].append(query_results)
        
        # Подсчитываем статистику
        total_tests = len(TEST_QUERIES) * 4  # 4 AI
        
        # Подсчет по статусам
        status_counts = {
            "success": 0,
            "failed": 0,
            "no_api_key": 0,
            "not_implemented": 0
        }
        
        mentions = 0
        
        for qr in results["results"]:
            for ar in qr["ai_responses"]:
                status = ar.get("status", "unknown")
                if status in status_counts:
                    status_counts[status] += 1
                
                if ar["mentioned"]:
                    mentions += 1
        
        # Рассчитываем процент успешных запросов
        successful_tests = status_counts["success"]
        success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
        
        # Процент упоминаний от успешных запросов
        mention_rate = (mentions / successful_tests * 100) if successful_tests > 0 else 0
        
        results["statistics"] = {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": status_counts["failed"],
            "no_api_key_tests": status_counts["no_api_key"],
            "not_implemented_tests": status_counts["not_implemented"],
            "success_rate": f"{success_rate:.1f}%",
            "mentions": mentions,
            "mention_rate": f"{mention_rate:.1f}%",
            "mention_rate_of_total": f"{(mentions/total_tests)*100:.1f}%"
        }
        
        return results
    
    def save_results(self, results: Dict, filename: str = None):
        """Сохраняет результаты в JSON файл"""
        if filename is None:
            filename = f"ai_monitor_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        os.makedirs("reports", exist_ok=True)
        filepath = os.path.join("reports", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Результаты сохранены: {filepath}")
        return filepath
    
    def generate_report(self, results: Dict) -> str:
        """Генерирует текстовый отчет"""
        report = []
        report.append("=" * 60)
        report.append("ОТЧЕТ: Мониторинг AI-упоминаний DimKava")
        report.append("🇬🇪 Локации: Тбилиси | Батуми | Грузия")
        report.append("=" * 60)
        report.append(f"Дата: {results['test_date']}")
        report.append(f"Бренд: {results['brand']}")
        report.append(f"Запросов протестировано: {results['queries_tested']}")
        report.append(f"Языки: Русский + English")
        report.append("")
        
        stats = results['statistics']
        report.append("СТАТИСТИКА:")
        report.append(f"  Всего тестов: {stats['total_tests']}")
        report.append("")
        report.append("  Статус запросов:")
        report.append(f"    ✅ Успешно выполнено: {stats['successful_tests']}")
        report.append(f"    ❌ Ошибка: {stats['failed_tests']}")
        report.append(f"    🔑 Нет API ключа: {stats['no_api_key_tests']}")
        report.append(f"    ⏳ Не реализовано: {stats['not_implemented_tests']}")
        report.append(f"    📊 Процент успешных: {stats['success_rate']}")
        report.append("")
        report.append("  Упоминания бренда:")
        report.append(f"    🎯 Упоминаний найдено: {stats['mentions']}")
        report.append(f"    📈 Процент от успешных: {stats['mention_rate']}")
        report.append(f"    📊 Процент от общего: {stats['mention_rate_of_total']}")
        report.append("")
        
        report.append("ДЕТАЛИ ПО ЗАПРОСАМ:")
        for i, qr in enumerate(results['results'], 1):
            report.append(f"\n{i}. {qr['query']}")
            for ar in qr['ai_responses']:
                # Определяем иконку статуса
                if ar['status'] == 'success':
                    if ar['mentioned']:
                        icon = "✅ НАЙДЕН"
                    else:
                        icon = "❌ НЕ НАЙДЕН"
                elif ar['status'] == 'no_api_key':
                    icon = "🔑 НЕТ КЛЮЧА"
                elif ar['status'] == 'failed':
                    icon = "⚠️ ОШИБКА"
                elif ar['status'] == 'not_implemented':
                    icon = "⏳ НЕ РЕАЛИЗОВАНО"
                else:
                    icon = "❓ НЕИЗВЕСТНО"
                
                report.append(f"   {icon} - {ar['ai']}")
                
                # Показываем ошибку если есть
                if ar.get('error') and ar['status'] in ['failed', 'no_api_key']:
                    report.append(f"      └─ {ar['error']}")
        
        return "\n".join(report)


def main():
    """Основная функция для запуска мониторинга"""
    # Фикс кодировки для Windows
    import sys
    if sys.platform == 'win32':
        import codecs
        sys.stdout.reconfigure(encoding='utf-8')
    
    print("🚀 Запуск мониторинга AI-упоминаний...")
    
    monitor = AIMonitor(brand_name="DimKava")
    results = monitor.run_full_test()
    
    # Сохраняем результаты
    monitor.save_results(results)
    
    # Выводим отчет
    report = monitor.generate_report(results)
    print("\n" + report)
    
    print("\n✅ Мониторинг завершен!")


if __name__ == "__main__":
    main()

