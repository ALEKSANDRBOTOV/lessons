
def make_label(text, *, uppercase=False, prefix=""):
    """Собирает подпись из текста с опциональным регистром и префиксом."""
    answer=text.upper() if uppercase else text    
    if prefix!="":
        return prefix + answer
    return answer

def total_cost(price, quantity=1, *, shipping=0, discount_percent=0):
    """Считает итоговую стоимость заказа с учётом количества, доставки и скидки."""
    return round ((price*quantity)*(1-discount_percent/100)+shipping, 2)