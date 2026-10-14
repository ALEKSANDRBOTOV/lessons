def greet_user(name):
    """Собирает строку приветствия по имени пользователя."""
    if name=="" or name.strip()=="":
        name= "гость"
    return (f"Привет, {name.strip()}!")

def is_adult(age):
    """Сообщает, достиг ли возраст совершеннолетия."""
    adult=18
    return (age>=adult)


