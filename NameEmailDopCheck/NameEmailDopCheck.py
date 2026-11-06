
def clean_name(raw):
    """Нормализует имя; возвращает (None, имя) или ("name is required", None)."""
    words = raw.split()
    cleaned = " ".join(words)
    
    if not cleaned:
        return "name is required", None
    return None, cleaned


def clean_email(raw):
    """Нормализует почту; возвращает (None, email) или ("email is invalid", None)."""
    cleaned = raw.strip().lower()
    
        # Должен быть ровно один символ '@'
    if cleaned.count('@') != 1:
        return "email is invalid", None
        
    parts = cleaned.split('@')
    local_part, domain_part = parts[0], parts[1]
    
        # Непустые части до и после '@', и в доменной части должна быть точка
    if not local_part or not domain_part or '.' not in domain_part:
        return "email is invalid", None
        
    return None, cleaned


def clean_quantity(raw):
    """Разбирает количество; возвращает (None, целое число) или ("quantity must be 1..100", None)."""
    if not raw.isdigit():
        return "quantity must be 1..100", None
        
    value = int(raw)
    # Число должно быть в диапазоне от 1 до 100 включительно
    if not (1 <= value <= 100):
        return "quantity must be 1..100", None
        
    return None, value


def check_order(form):
    """Собирает результат из трёх хелперов: (errors, clean)."""
    errors = []
    clean = {}
    
    # Массив хелперов и соответствующих им ключей для строгого порядка вызова
    validators = [
        ("name", clean_name),
        ("email", clean_email),
        ("quantity", clean_quantity)
    ]
    
    for key, validator in validators:
        error, value = validator(form[key])
        if error:
            errors.append(error)
        else:
            clean[key] = value
            
    return errors, clean


# Пример использования:
# check_order({"name": " Ada ", "email": "Ada@Mail.RU", "quantity": "3"})
# ([], {"name": "Ada", "email": "ada@mail.ru", "quantity": 3})
