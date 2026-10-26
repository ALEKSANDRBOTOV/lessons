import math

def started_hours(minutes):
    """Возвращает количество начатых часов за указанные минуты."""
    if minutes == 0:
        return 0
    return math.ceil(minutes / 60)

def parking_fee(minutes, hour_price, day_cap):
    """Вычисляет общую стоимость парковки в копейках."""
    if minutes <= 15: # правило - меньше 15 минут - бесплатно
        return 0
    
    full_days = minutes // 1440
    remaining_minutes = minutes % 1440 # разбиваем на полные сутки и остаток
    
    total_fee = full_days * day_cap
    
    # Считаем стоимость остатка
    if remaining_minutes > 0:
        remaining_hours = started_hours(remaining_minutes)
        remaining_fee = remaining_hours * hour_price
        total_fee += min(remaining_fee, day_cap) # Применяем суточный потолок к остатку
        
    return total_fee
