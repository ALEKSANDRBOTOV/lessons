
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

def keep_where(items, predicate):
    """Возвращает элементы items, для которых predicate(элемент) истинно."""
    answer=[]
    for i in items:
        if predicate(i):
            answer.append(i)
    return answer


# Пример использования:
# keep_where([1, 2, 3, 4], lambda x: x % 2 == 0)  # [2, 4]

def clean_text(text):
    """Нормализует текст: схлопывает пробелы и переводит в нижний регистр."""
    return " ".join(text.lower().split())


def word_count(text):
    """Считает число слов в очищенном тексте."""
    return len(clean_text(text).split())


def summarize(text):
    """Собирает словарь превью: clean (очищенный текст) и words (число слов)."""
    cleaned = clean_text(text)
    return {"clean": cleaned, "words": word_count(cleaned)}


# Пример использования:
# summarize("  Hello   World ")  # {"clean": "hello world", "words": 2}
