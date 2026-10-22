def apply_discount(price_kopecks, percent, max_discount_kopecks):
    """Считает цену со скидкой в копейках: процент вниз, ограниченный потолком."""
    if not 0<=percent<=100:
        raise ValueError("percent out of range")
    if price_kopecks<0:
        raise ValueError("price must not be negative")
    discount=price_kopecks*percent//100
    final_discount=min(discount, max_discount_kopecks)
    answer=price_kopecks-final_discount
    return answer
