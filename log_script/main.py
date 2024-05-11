
from pathlib import Path
import sys
from handlers import display_log_counts, load_logs, count_logs_by_level, filter_logs_by_level


def main():
    try:
        file_path = Path(sys.argv[1]) # отримує шлях до файлу з другого аргументу
        logs = load_logs(file_path) # Отримує список логів 
        if logs: # якщо список існує
            counts = count_logs_by_level(logs) # отримує словник з підрахунком логів за кожним рівнем
            display_log_counts(counts) # виводить в консоль табличку з кількістю логів за рівнем
        if len(sys.argv) >= 3: # якщо аргументів більше ніж 2
            level = sys.argv[2].upper() # отримує аргумент запиту рівня
            filter_logs_by_level(logs, level) # виводить список логів за рівнем, що був у запиті
    except IndexError: # Якщо при запуску скрипту не вказані агрументи
        print('Напишіть адресу лог-файлу в якості аргументу в командному рядку\n')

if __name__ == '__main__':
    main()