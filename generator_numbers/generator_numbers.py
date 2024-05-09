from typing import Callable
import re

def generator_numbers(text: str):
    for world in text.split(' '):
        pattern = r"\d+\.+\d+"
        match = re.search(pattern, world, re.IGNORECASE)
        if match:
            yield match.group()

def sum_profit(text: str, func: Callable):
    total = 0
    for salary in func(text):
        total += float(salary)
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") # Загальний дохід: 1351.46