
def password_issues(password):
    """Возвращает список кодов проблем пароля в фиксированном порядке.

    # Пример использования:
    # issues = password_issues("short1A")
    # print(issues)  # ["too_short"]
    """
    answer=[]
    if len(password)<8:
        answer.append("too_short")
    if not any(char.isdigit() for char in password):
        answer.append("no_digit")
    if not any(char.isupper() for char in password):
        answer.append("no_upper")
    if not any(char.islower() for char in password):
        answer.append("no_lower")
    return answer
        
