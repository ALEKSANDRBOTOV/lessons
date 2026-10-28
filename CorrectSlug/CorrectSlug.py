
def is_valid_length(slug):
    """Проверяет, что длина слага в допустимых пределах."""
    return 3 <= len(slug) <= 50


def has_valid_chars(slug):
    """Проверяет, что в слаге только разрешённые символы."""
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789-"
    for char in slug:
        if char not in allowed_chars:
            return False
    return True


def has_valid_hyphens(slug):
    """Проверяет, что дефисы расставлены корректно."""
    if slug.startswith("-") or slug.endswith("-") or "--" in slug:
        return False
    return True


def validate_slug(slug):
    """Зовёт три проверки и собирает отчёт {valid, errors}."""
    answer=[]
    valid=bool()
    if len(slug)<3:
        answer.append("too_short")
    elif len(slug)>50:
        answer.append("too_long")
    if not has_valid_chars(slug):
        answer.append("bad_chars")
    if not has_valid_hyphens(slug):
        answer.append("bad_hyphens")
    if not is_valid_length(slug) or not has_valid_chars(slug) or not has_valid_hyphens(slug):
        valid=False
    else:
        valid=True
    
    return {"valid": valid, "errors": answer}