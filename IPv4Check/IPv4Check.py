
def parse_ipv4(value):
    """Разбирает IPv4-адрес в список из четырёх int или выбрасывает ValueError."""
    if not isinstance(value, str):
        raise ValueError("invalid ipv4")
        
    parts = value.split(".")
    
    if len(parts) != 4:
        raise ValueError("invalid ipv4")
        
    answer = []
    for part in parts:
        # Проверяем, что часть состоит строго из цифр (без пробелов, плюсов, минусов и букв)
        if not part.isdigit():
            raise ValueError("invalid ipv4")
            
        num = int(part)
        if num < 0 or num > 255:
            raise ValueError("invalid ipv4")
            
        answer.append(num)
        
    return answer
