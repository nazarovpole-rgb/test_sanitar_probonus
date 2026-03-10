# run.py
"""
Главный скрипт запуска тестов
"""

import sys
import glob
import importlib.util
from playwright.sync_api import sync_playwright
from colors import *

def find_test_files():
    """Находит все тестовые файлы"""
    test_files = []
    
    # Ищем все .py файлы с 'test' в имени
    for file in glob.glob("*.py"):
        if "test" in file.lower() and file not in ["run.py", "colors.py"]:
            test_files.append(file)
    
    # Сортируем для порядка выполнения
    test_files.sort()
    return test_files


def run_test_file(test_file, page):
    """Запускает один тестовый файл"""
    try:
        # Динамически импортируем модуль
        spec = importlib.util.spec_from_file_location("test_module", test_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Ищем класс с методом run
        test_class = None
        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue
            
            attr = getattr(module, attr_name)
            if (isinstance(attr, type) and 
                hasattr(attr, 'run') and 
                callable(getattr(attr, 'run'))):
                test_class = attr
                break
        
        if not test_class:
            print(test_error(f"Не найден тестовый класс в {test_file}"))
            return False, "Нет тестового класса"
        
        # Запускаем тест
        result = test_class.run(page)
        return result, ""
        
    except Exception as e:
        return False, str(e)


def main():
    """Основная функция"""
    print_header("ЗАПУСК АВТОТЕСТОВ")
    
    # Ищем тестовые файлы
    test_files = find_test_files()
    
    if not test_files:
        print(error("Тестовые файлы не найдены!"))
        print(info("Разместите файлы с 'test' в имени в текущей папке"))
        return False
    
    print(info(f"Найдено тестов: {len(test_files)}"))
    print(gray("Список:"))
    for i, f in enumerate(test_files, 1):
        print(gray(f"  {i:2d}. {f}"))
    
    print_separator(color_func=gray)
    
    # Запускаем браузер
    print(step("Запуск браузера..."))
    
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            page = context.new_page()
            
            print(success("Браузер запущен"))
            print()
            
            # Запускаем тесты
            total = len(test_files)
            passed = 0
            failed = 0
            results = []
            
            for i, test_file in enumerate(test_files, 1):
                print(test_running(f"[{i}/{total}] {test_file}"))
                print_separator(".", 50, gray)
                
                # Запускаем тест
                success_flag, message = run_test_file(test_file, page)
                
                # Записываем результат
                if success_flag:
                    print(test_passed(f"{test_file} - ПРОЙДЕН"))
                    passed += 1
                else:
                    print(test_failed(f"{test_file} - НЕ ПРОЙДЕН"))
                    if message:
                        print(gray(f"   Ошибка: {message[:80]}"))
                    failed += 1
                
                results.append((test_file, success_flag, message))
                print()  # Пустая строка
            
            # Закрываем браузер
            print(step("Закрытие браузера..."))
            context.close()
            browser.close()
            
    except Exception as e:
        print(error(f"Ошибка браузера: {e}"))
        return False
    
    # Выводим результаты
    print_summary(total, passed, failed)
    
    # Показываем упавшие тесты
    if failed > 0:
        print()
        print(warning("Упавшие тесты:"))
        for test_file, success_flag, message in results:
            if not success_flag:
                print(f"  {red('•')} {test_file}")
                if message:
                    print(f"     {gray(message)}")
    
    print()
    return failed == 0


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print()
        print(yellow("Тестирование прервано пользователем"))
        sys.exit(130)
    except Exception as e:
        print(error(f"Критическая ошибка: {e}"))
        sys.exit(1)