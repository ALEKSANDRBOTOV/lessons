
def format_kopecks(kopecks):
    if kopecks == 0:
        return "0,00 ₽"
        
    # Определяем знак суммы
    sign = "-" if kopecks < 0 else ""
    
    # Работаем с модулем числа!!!
    abs_kopecks = abs(kopecks)

    rubles = abs_kopecks // 100
    coins = abs_kopecks % 100
    
    # Заменяем стандартную запятую Python на пробел
    formatted_rubles = f"{rubles:,}".replace(",", " ")
    
    return f"{sign}{formatted_rubles},{coins:02d} ₽"
