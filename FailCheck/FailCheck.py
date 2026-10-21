def route_ticket(text):
    """Выбирает очередь поддержки по первому совпавшему ключевому слову в тексте обращения."""
    if isinstance(text, str)!=True:
        raise ValueError("text must be a string")
    check_text= text.strip().lower()
    if ("срочно") in check_text:
        return ("urgent")
    elif (("оплат") in check_text) or (("счёт") in check_text):
        return ("billing")
    elif (("ошибк") in check_text) or (("не работает")in check_text ):
        return ("tech")
    elif ("пароль") in check_text:
        return ("account")
    else:
        return ("general")
