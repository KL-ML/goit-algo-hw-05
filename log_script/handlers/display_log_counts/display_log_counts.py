# форматує та виводить результати підрахунку в читабельній формі.
# приймає результати виконання функції count_logs_by_level "counts: dict"
def display_log_counts(counts: dict): 
    info, debag, warning, error = counts
    display_log = f"""Pівень логування | Кількість 
-----------------|----------
INFO             | {counts[info]}
DEBUG            | {counts[debag]}
ERROR            | {counts[warning]}
WARNING          | {counts[error]}
"""
    print(display_log)