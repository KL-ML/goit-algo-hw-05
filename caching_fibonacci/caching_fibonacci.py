
def caching_fibonacci(): # ФУНКЦІЯ caching_fibonacci
    cache = {} # Створення порожнього словника для кешу
    def fibonacci(n): # ФУНКЦІЯ fibonacci(n)
        if n <= 1:
            return n # Якщо n <= 1, повернути n
        if n in cache: # Якщо n у cache, повернути cache[n]
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n] # Повернути cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610