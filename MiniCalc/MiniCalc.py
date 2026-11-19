
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def apply_op(op, a, b):
    """Выбирает арифметическую операцию по ключу op и применяет её к a и b."""
    operations={"add": add,"sub": sub, "mul": mul}
    if op not in operations:
        raise ValueError(f"unknown op: {op}")
    return operations[op](a,b)


# Пример использования:
# apply_op("add", 2, 3)  # 5
