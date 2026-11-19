
def has_digit(text):
    """Сообщает, есть ли в строке хотя бы одна цифра."""
    return any(i.isdigit() for i in text )


def has_upper(text):
    """Сообщает, есть ли в строке хотя бы одна заглавная буква."""
    return any(i.isupper() for i in text )


def is_long_enough(text):
    """Сообщает, достаточно ли длинна строка."""
    return len(text)>=8


def password_strength(password):
    """Складывает выполненные требования в балл и переводит балл в метку."""
    digit= has_digit(password)
    upper= has_upper(password)
    long= is_long_enough(password)
    s=sum([digit+ upper+ long])
    if s<=1:
        return "weak"
    elif s==2:
        return "medium"
    else:
        return "strong"


# Пример использования:
# password_strength("Abcdefg1")  # "strong"
