# # відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line, 
# # зберігаючи результати в список.
# # скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. 
# # Використовуйте блоки try/except для обробки виняткових ситуацій.

import re
from ..parse_log_line.parse_log_line import parse_log_line

def load_logs(file_path: str) -> list: # для завантаження логів з файлу
    lines = [] # Інізіалізуємо пустий список
    try:
        with open(file_path, "r", encoding="utf-8") as file: # відкриває лог-файл
            while True: # Цикл, що працює поки є строки в файлі
                line = file.readline() # Читає строки по одній
                if not line: # Якщо строки немає
                    break # вихід з циклу
                pattern = r"\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}\s\w+\s\w+" 
                # 2024-01-22 08:30:01 INFO User logged in successfully.
                match = re.search(pattern, line, re.IGNORECASE) # порівнює строку з паттерном
                if match: # Якщо строка збігається з патерном
                    lines.append(parse_log_line(line)) # Додає лог до списку
            return lines # повертає список логів
    except IsADirectoryError: # Якщо шлях вказує на директрію а не файл
        print("Не вдалося знайти файл.\n")
    except FileNotFoundError: # Якщо шлях до файлу невірний або пошкоджений
        print("Не вдалося знайти файл.\n")

    