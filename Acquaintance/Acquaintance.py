def greet_user(name):
    """Собирает строку приветствия по имени пользователя."""
    if name=="" or name.strip()=="":
        name= "гость"
    return (f"Привет, {name.strip()}!")

def is_adult(age):
    """Сообщает, достиг ли возраст совершеннолетия."""
    adult=18
    return (age>=adult)

def parse_amount_field(amount_raw):
    """Переводит сумму-строку из банковской выгрузки в целые копейки."""
    dot_index = amount_raw.find('.')
    if dot_index==-1 :
        total=int(amount_raw)*100
    else:
        total=int(amount_raw.replace(".",""))        
    return total
