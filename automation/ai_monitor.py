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
        # TODO: Реализовать через OpenAI API
        return {
            "ai": "ChatGPT",
            "query": query,
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": ""
        }
    
    def test_gemini(self, query: str) -> Dict:
        """Тестирует Google Gemini"""
        # TODO: Реализовать через Google AI API
        return {
            "ai": "Gemini",
            "query": query,
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": ""
        }
    
    def test_claude(self, query: str) -> Dict:
        """Тестирует Claude (Anthropic)"""
        # TODO: Реализовать через Anthropic API
        return {
            "ai": "Claude",
            "query": query,
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": ""
        }
    
    def test_perplexity(self, query: str) -> Dict:
        """Тестирует Perplexity AI"""
        # TODO: Реализовать через Perplexity API
        return {
            "ai": "Perplexity",
            "query": query,
            "mentioned": False,
            "timestamp": datetime.now().isoformat(),
            "response_snippet": ""
        }
    
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
        mentions = sum(
            1 for qr in results["results"] 
            for ar in qr["ai_responses"] 
            if ar["mentioned"]
        )
        
        results["statistics"] = {
            "total_tests": total_tests,
            "mentions": mentions,
            "mention_rate": f"{(mentions/total_tests)*100:.1f}%"
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
        report.append(f"  Упоминаний: {stats['mentions']}")
        report.append(f"  Процент упоминаний: {stats['mention_rate']}")
        report.append("")
        
        report.append("ДЕТАЛИ ПО ЗАПРОСАМ:")
        for i, qr in enumerate(results['results'], 1):
            report.append(f"\n{i}. {qr['query']}")
            for ar in qr['ai_responses']:
                status = "✅" if ar['mentioned'] else "❌"
                report.append(f"   {status} {ar['ai']}")
        
        return "\n".join(report)


def main():
    """Основная функция для запуска мониторинга"""
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

