
def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} Б"
    elif size_bytes < 1024 ** 2:
        unit = "КБ"
        value = size_bytes / 1024
    elif size_bytes < 1024 ** 3:
        unit = "МБ"
        value = size_bytes / (1024 ** 2)
    else:
        unit = "ГБ"
        value = size_bytes / (1024 ** 3)

    truncated_value = (value * 10 // 1) / 10

    if truncated_value == int(truncated_value):
        formatted_num = str(int(truncated_value))
    else:
        formatted_num = str(truncated_value).replace(".", ",")
        
    return f"{formatted_num} {unit}"
