
import re


DAY_CODES = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
WINDOW_PATTERN = re.compile(r"^ *([A-Za-z]{3}) +([0-9]{2}):([0-9]{2})-([0-9]{2}):([0-9]{2}) *$")


def _minute_of_day(hour_text: str, minute_text: str) -> int:
    """Преобразует HH и MM в минуты от полуночи после проверки диапазонов."""
    return int(hour_text)*60+int(minute_text)


def parse_release_window(raw: str) -> dict:
    """Разбирает строку окна релиза вида 'tue 09:30-11:00'.

    Примите только трёхбуквенный день, пробелы вокруг всей строки,
    один или больше пробелов между днём и временем и формат HH:MM-HH:MM
    без пробелов вокруг дефиса. День верните в нижнем регистре.
    Ошибки формата, дня и диапазонов времени должны иметь точные сообщения
    из условия.
    """
    # 1. Проверяем общий формат строки регулярным выражением (вместо ненадёжного split())
    match = WINDOW_PATTERN.match(raw)
    if not match:
        raise ValueError("invalid release window")
    
    # Достаем проверенные кусочки строк
    day_raw, sth, stm, eh, em = match.groups()
    
    day = day_raw.lower()
    if day not in DAY_CODES:
        raise ValueError("invalid release window")
    
    if int(sth) > 23 or int(sth) < 0 or int(eh) < 0 or int(eh) > 23 or int(stm) > 59 or int(stm) < 0 or int(em) > 59 or int(em) < 0:
        raise ValueError("invalid release window")

    if _minute_of_day(eh, em) <= _minute_of_day(sth, stm):
        raise ValueError("window end must be after start")

    start_minute = _minute_of_day(sth, stm)
    end_minute = _minute_of_day(eh, em)
    duration = end_minute - start_minute
    

    answer= {"day": day, "start_minute": start_minute, "end_minute": end_minute, "duration": duration}
    return answer


# Пример использования:
# window = parse_release_window("sun 22:15-23:00")
# print(window)  # {'day': 'sun', 'start_minute': 1335, 'end_minute': 1380, 'duration': 45}
