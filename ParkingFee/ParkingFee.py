
def started_hours(minutes):
    """Сколько часов начато за minutes минут стоянки."""
    hours=0
    if minutes<=15:
        hours=0
    elif minutes>60:
        hours=minutes//60
        if minutes%60!=0:
            hours+=1 # Добавляем час, если новый начался
    else:
        hours+=1
    return hours

def parking_fee(minutes, hour_price, day_cap):
    """Плата за всю стоянку в копейках."""
    summa=started_hours(minutes)*hour_price
    if  summa>day_cap: # устанавливаем максимум суммы за день
        summa=day_cap 
    if started_hours(minutes)>24:
        summa+=(started_hours(minutes)-24)*hour_price    
    return summa