
def vat_amount(price_kopecks, rate_percent):
    """Возвращает сумму НДС в копейках, уже входящую в price_kopecks."""
    if rate_percent<0:
        raise ValueError("rate must not be negative")
    if price_kopecks<0:
        raise ValueError("price must not be negative")
    answer=price_kopecks/(rate_percent+100)*rate_percent
    return int(answer+0.5) # округление. не будет работать с отрицательными числами - math.floor
