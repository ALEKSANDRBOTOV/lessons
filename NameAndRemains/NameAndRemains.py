
def split_name(full_name):
    """Разбивает полное имя на первое слово и остаток."""
    parts=full_name.split()
    if not parts:
        return "", ""
    return parts[0], " ".join(parts[1:])
    
    


# Пример использования:
# split_name("Анна Каренина")  # ("Анна", "Каренина")