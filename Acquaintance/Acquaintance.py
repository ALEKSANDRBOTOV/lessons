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
    """Переводит сумму-строку из банковской выгрузки в целые копейки.

    Если точки в строке нет — вся строка является рублями: умножьте
    на 100. Если точка есть — часть до неё является рублями, две цифры
    после — копейками: верните рубли * 100 + копейки. Работайте только
    со строкой и int: float в деньгах «Копилки» запрещён.
    """
    dot_index = amount_raw.find('.')
    if dot_index==-1 :
        total=int(amount_raw)*100
    else:
        total=int(amount_raw.replace(".",""))        
    return total
