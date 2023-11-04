from time import time


def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(args)
        finish_time = time()
        
        print(f"Час виконання функції: {start_time-finish_time}")

        print(f"Викликана функція {func.__name__} з аргументами {args}")
        try:
            result = func(*args, **kwargs)
            print("результат: {result}")
            return result
        except:
            print("Функція не має результату!")
    return wrapper