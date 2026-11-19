
def line_subtotal(items):
    """Считает сумму позиций заказа."""
    return sum(price * quantity for price, quantity in items)


def tax_amount(subtotal, rate_percent):
    """Считает налог от суммы по ставке в процентах."""
    return round(subtotal*rate_percent/100, 2)


def summarize_order(items, rate_percent):
    """Собирает словарь итогов заказа: subtotal, tax, total."""
    subtotal=line_subtotal(items)
    tax=tax_amount(subtotal, rate_percent)
    total=subtotal+tax
    return {"subtotal": subtotal, "tax": tax, "total": round(total,2)}