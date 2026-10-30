
def check_digit(number):
    """Считает контрольную цифру по цифрам номера."""
    itog=0
    for cel in str(number):
        itog+=int(cel)
    return itog%10


def order_number(number):
    """Собирает номер заказа для печати в чеке."""
    if len(str(number))<6:
        answer="0"*(6-len(str(number)))
        return (f"№ {answer}{number}-{check_digit(number)}")
    else:
        return (f"№ {number}-{check_digit(number)}")