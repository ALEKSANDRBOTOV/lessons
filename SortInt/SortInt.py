
def is_sorted(values):
    """Возвращает True, если список не убывает (соседние равные допустимы)."""
    if values==sorted(values):
        return True
    else:
        return False


def merge_sorted(left, right):
    """Сливает два отсортированных списка в один; неотсортированный вход — ValueError."""
    result=[]
    if not is_sorted(left) or not is_sorted(right):
        raise ValueError("inputs must be sorted")
    elif left==None:
        return result.append(right)
    elif right==None:
        return result.append(left)
    return sorted(left+right)

# Пример использования:
# is_sorted([1, 3, 3, 5])             # True
# merge_sorted([1, 4, 7], [2, 4, 8])  # [1, 2, 4, 4, 7, 8]