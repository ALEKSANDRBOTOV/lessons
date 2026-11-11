
def is_valid_card(number):
    """Проверяет номер банковской карты алгоритмом Луна."""
    total = 0
    if not number.isdigit():
        return False
    # Разворачиваем строку, чтобы идти справа налево, и нумеруем с 1
    for index, char in enumerate(reversed(number), start=1):
        digit = int(char)
        
        if index % 2 == 1:
            # Нечётная позиция: берём саму цифру
            total += digit
        else:
            # Чётная позиция: удваиваем и складываем цифры (если >= 10, вычитаем 9)
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
            
    return total % 10 == 0

# Пример использования:
# is_valid_card("4539578763621486")  # True
