
def make_label(text, *, uppercase=False, prefix=""):
    """Собирает подпись из текста с опциональным регистром и префиксом."""
    answer=text.upper() if uppercase else text    
    if prefix!="":
        return prefix + answer
    return answer