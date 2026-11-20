
def add_capped(items, item, limit):
    """Возвращает новую ленту с добавленным item, не длиннее limit последних записей."""
    answer=(items+[item])
    if limit>=len(answer):
        return answer
    else:
        return answer[len(answer)-limit:]


# Пример использования:
# add_capped(["a", "b", "c"], "d", 3)  # ["b", "c", "d"]