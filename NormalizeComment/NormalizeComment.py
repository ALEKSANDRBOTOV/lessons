MAX_HABIT_LENGTH = 32


def normalize_habit(raw):

    text = raw.lower().replace('ё', 'е')

    text = text.replace('—', '-').replace('–', '-')

    clean_chars = []
    for char in text:
        if char.isalnum() or char == '-':
            clean_chars.append(char)
        else:
            clean_chars.append(' ')
    text = "".join(clean_chars)

    tokens = text.split()
    text = " ".join(tokens)

    text = text.strip("- ").strip("- ")

    if not text:
        return None

    if len(text) > MAX_HABIT_LENGTH:
        return None
        
    return text