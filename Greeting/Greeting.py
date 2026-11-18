
def build_greeting(name, greeting=None):
    """Собирает приветствие по имени и необязательному обращению."""
    nn=name.strip()
    if greeting is None and len(nn)<1:
        return "Привет, гость!"
    elif greeting is None:
        return f"Здравствуйте, {nn}!"
    elif len(nn)<1:
        return f"{greeting}, гость!"
    else:
        return f"{greeting}, {nn}!"


# Пример использования:
# build_greeting("Аня")          # "Здравствуйте, Аня!"
# build_greeting("Аня", "Хай")   # "Хай, Аня!"