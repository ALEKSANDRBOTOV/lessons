
def transliterate(text):
    """Заменяет кириллические буквы на латинские по таблице."""
    char_conv = {
        "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", 
        "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", 
        "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", 
        "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", 
        "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya"
    }
    
    result = []
    for char in text:
        if char in char_conv:
            result.append(char_conv[char])
        else:
            result.append(char)
            
    return "".join(result)


def slugify(title):
    """Собирает из заголовка slug, разделяя слова дефисами."""
    lowered_title = title.lower()

    trans_text = transliterate(lowered_title)
    
    cleaned_chars = []
    for char in trans_text:
        if char.isalnum() and char.isascii():
            cleaned_chars.append(char)
        else:
            cleaned_chars.append(" ")
            
    cleaned_text = "".join(cleaned_chars)

    words = cleaned_text.split()

    return "-".join(words)
