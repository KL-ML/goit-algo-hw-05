# # проходить по всім записам і підраховує кількість записів для кожного рівня логування.
def count_logs_by_level(logs: list) -> dict: # для підрахунку записів за рівнем логування
    # Отримує список логів за кожним рівнем
    info = [l for l in logs if l['level'] == 'INFO'] 
    debag = [l for l in logs if l['level'] == 'DEBUG']
    warning = [l for l in logs if l['level'] == 'WARNING']
    error = [l for l in logs if l['level'] == 'ERROR']
    # Створює словник з кількістю логів кожного рівня
    counts = {'INFO': len(info), 'DEBUG': len(debag), 'WARNING': len(warning), 'ERROR': len(error)}
    
    return counts