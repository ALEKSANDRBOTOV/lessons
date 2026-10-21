def check_password(password):
    """Возвращает список кодов невыполненных правил пароля; пустой список — пароль валиден."""
    special="!@#$%_-"
    ans=[]
    if password!=str(password):
        raise ValueError("password must be a string")
    if len(password)<8:
        ans.append("too_short")
    if not any(char.isdigit() for char in password):
        ans.append("no_digit")
    if not any(char.isupper()for char in password):
        ans.append("no_upper")
    if not any (char in special for char in password):
        ans.append("no_special")
    return ans
