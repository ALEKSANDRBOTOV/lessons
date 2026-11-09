
def time_duration(start, end):
    """Возвращает разницу в минутах между двумя временами 'HH:MM' в рамках одного дня."""        
    if len(start) != 5 or start[2] != ':' or len(end) != 5 or end[2] != ':':
        raise ValueError("invalid time format")
    
    # Разделяем на часы и минуты
    start_hours_str = start[:2]
    start_minutes_str = start[3:]
    end_hours_str=end[:2]
    end_minutes_str=end[3:]
        
    s_hours = int(start_hours_str)
    e_hours= int(end_hours_str)
    s_minutes = int(start_minutes_str)
    e_minutes= int(end_minutes_str)
    
    # Валидируем диапазоны для часов и минут
    if not (0 <= s_hours <= 23 and 0 <= s_minutes <= 59 and 0 <= e_hours <= 23 and 0 <= e_minutes <= 59):
        raise ValueError("invalid time format")
    if e_hours<s_hours:
        raise ValueError("end must not be before start")
    answer= (s_hours-e_hours)*60+(s_minutes-e_minutes)

        
    # Возвращаем общее количество минут от полуночи
    return abs(answer)