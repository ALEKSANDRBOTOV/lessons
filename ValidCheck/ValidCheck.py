def validate_form(form):
    """Возвращает список кодов ошибок по невалидным полям формы; пустой список — форма валидна."""
    errors=[]
    if not isinstance(form, dict):
        raise ValueError("form must be a dict")
    email=form.get("email")
    age=form.get("age")
    username=form.get("username")
    if not isinstance(email, str) or email.count("@") != 1 or "" in email.split("@"):
        errors.append("email_invalid")
    if type(age) is not int or not (18 <= age <= 120):
        errors.append("age_invalid")
    if not isinstance(username, str) or not (3 <= len(username) <= 20):
        errors.append("username_invalid")
    else:
            # Этот цикл запустится ТОЛЬКО если username — это строка
        for ch in username:
            if not (ch.isalnum() or ch == "_"):
                errors.append("username_invalid")
                break 
    return errors


# Пример использования:
# validate_form({"email": "a@b.io", "age": 30, "username": "echo_99"})  # []
# validate_form({"email": "bad", "age": 30, "username": "echo"})        # ["email_invalid"]

