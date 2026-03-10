# colors.py
"""
Модуль с цветами для консольного вывода
"""

# ANSI escape codes
class Colors:
    # Основные цвета
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    
    # Стили
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'
    
    # Фоны
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    
    # Сброс
    RESET = '\033[0m'
    END = RESET


def color(text: str, color_code: str) -> str:
    """Окрашивает текст в указанный цвет"""
    return f"{color_code}{text}{Colors.RESET}"


# Базовые цвета
def red(text: str) -> str:
    """Красный текст"""
    return color(text, Colors.RED)


def green(text: str) -> str:
    """Зеленый текст"""
    return color(text, Colors.GREEN)


def yellow(text: str) -> str:
    """Желтый текст"""
    return color(text, Colors.YELLOW)


def blue(text: str) -> str:
    """Синий текст"""
    return color(text, Colors.BLUE)


def cyan(text: str) -> str:
    """Голубой текст"""
    return color(text, Colors.CYAN)


def magenta(text: str) -> str:
    """Пурпурный текст"""
    return color(text, Colors.MAGENTA)


def gray(text: str) -> str:
    """Серый текст"""
    return color(text, Colors.GRAY)


def white(text: str) -> str:
    """Белый текст"""
    return color(text, Colors.WHITE)


# Стили
def bold(text: str) -> str:
    """Жирный текст"""
    return color(text, Colors.BOLD)


def underline(text: str) -> str:
    """Подчеркнутый текст"""
    return color(text, Colors.UNDERLINE)


def reversed_color(text: str) -> str:
    """Инвертированный текст"""
    return color(text, Colors.REVERSED)


# Комбинированные стили для тестов
def success(text: str) -> str:
    """Успех - зеленый жирный"""
    return color(f"✅ {text}", Colors.GREEN + Colors.BOLD)


def error(text: str) -> str:
    """Ошибка - красный жирный"""
    return color(f"❌ {text}", Colors.RED + Colors.BOLD)


def warning(text: str) -> str:
    """Предупреждение - желтый"""
    return color(f"⚠️ {text}", Colors.YELLOW)


def info(text: str) -> str:
    """Информация - синий"""
    return color(f"ℹ️ {text}", Colors.BLUE)


def header(text: str) -> str:
    """Заголовок - голубой жирный"""
    return color(text, Colors.CYAN + Colors.BOLD)


def step(text: str) -> str:
    """Шаг выполнения - пурпурный"""
    return color(f"▶ {text}", Colors.MAGENTA)


def debug(text: str) -> str:
    """Отладка - белый на синем фоне"""
    return color(text, Colors.WHITE + Colors.BG_BLUE)


# Специальные функции для тестов
def test_passed(text: str) -> str:
    """Тест пройден - зеленый с галочкой"""
    return color(f"✅ {text}", Colors.GREEN)


def test_failed(text: str) -> str:
    """Тест не пройден - красный с крестиком"""
    return color(f"❌ {text}", Colors.RED)


def test_error(text: str) -> str:
    """Ошибка теста - красный с восклицанием"""
    return color(f"💥 {text}", Colors.RED + Colors.BOLD)


def test_running(text: str) -> str:
    """Тест запущен - синий со стрелкой"""
    return color(f"▶ {text}", Colors.BLUE)


def test_skipped(text: str) -> str:
    """Тест пропущен - серый"""
    return color(f"⏭ {text}", Colors.GRAY)


# Вспомогательные функции
def print_separator(char: str = "─", length: int = 60, color_func=None):
    """Печатает цветной разделитель"""
    line = char * length
    if color_func:
        print(color_func(line))
    else:
        print(line)


def print_header(title: str, char: str = "=", length: int = 60):
    """Печатает заголовок в рамке"""
    print()
    print_separator(char, length, cyan)
    print(header(title.center(length)))
    print_separator(char, length, cyan)
    print()


def print_result(status: bool, test_name: str, message: str = ""):
    """Печатает результат теста"""
    if status:
        print(f"  {test_passed(test_name)} {message}")
    else:
        print(f"  {test_failed(test_name)} {message}")


def print_summary(total: int, passed: int, failed: int):
    """Печатает сводку результатов"""
    print()
    print_separator("─", 60, cyan)
    print(header("РЕЗУЛЬТАТЫ:"))
    print(f"  Всего тестов: {bold(str(total))}")
    print(f"  {green('Пройдено:')} {bold(str(passed))}")
    print(f"  {red('Упало:')} {bold(str(failed))}")
    
    if failed == 0:
        print()
        print(success("✨ ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!"))
    else:
        print()
        print(error("🚨 ЕСТЬ НЕУДАВШИЕСЯ ТЕСТЫ!"))
    print_separator("─", 60, cyan)