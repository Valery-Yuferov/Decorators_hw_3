def decor(old_function):
    def new_function(*args, **kwargs):
        print(f'Вызвана функция {old_function.__name__} с аргументами {args} и {kwargs}')
        result = old_function(*args, **kwargs)
        print(f"Функция вернула {result}")
        return result

    return new_function

