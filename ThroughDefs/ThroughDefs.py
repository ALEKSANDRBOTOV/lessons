
def apply_all(value, funcs):
    """Прогоняет value через список функций одного аргумента по очереди."""
    for step in funcs:
        next_value = step(value)
        if next_value is None:
            break
        value = next_value
    return value


# Пример использования:
# apply_all(5, [lambda x: x * 2, lambda x: x + 1])  # 11