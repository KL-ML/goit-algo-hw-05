# # отримати всі записи логу для певного рівня логування
def filter_logs_by_level(logs: list, level: str) -> list: # для фільтрації логів за рівнем
    # Перевіряє, чи отриманий аргумент level відповідає одному з чотирьох необхідних
    if level == 'INFO' or level == 'DEBUG' or level == 'ERROR' or level == 'WARNING':
        # Створює список логів за заданим рівнем
        filtered_by_level = [l for l in logs if l['level'] == level]
        print(f"Деталі логів для рівня '{level}':")
        # Виводить список логів в консоль
        for log in filtered_by_level: # Для кожного логу зі списку логів
            log_sting = f"{log['date']} {log['time']} - {log['message']}" # Створює строку
            print(log_sting) # Виводить строку в консоль
        print('') # Додаткова строка після списку логів для відділення
    else: # Якщо переданий level не співпадає із необхідними, виводить повідомлення
        print("Напишіть корректну назву рівня логування для відображення деталей логів.\n")
