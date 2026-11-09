
def format_duration(seconds):
    """Форматирует длительность в секундах как строку M:SS или H:MM:SS."""
    if seconds<0:
        raise ValueError("seconds must be non-negative")
    elif seconds<3600:
        M=seconds//60
        S=seconds%60
        return (f"{M}:{S:02d}")
    else:
        H=seconds//3600
        M=seconds%3600//60
        S=seconds%3600%60
        return (f"{H}:{M:02d}:{S:02d}")


# Пример использования:
# format_duration(75)    # "1:15"
# format_duration(3661)  # "1:01:01"
# format_duration(0)     # "0:00"
