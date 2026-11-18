
def at_or_after(event, start):
    """Истина, если событие случилось НЕ раньше start.

    Граница включительна: событие ровно в момент start считается
    попадающим (ts == start → True). Верните булево по полю "ts".
    """
    if event["ts"]>=start:
        return True
    else:
        return False


def before(event, end):
    """Истина, если событие случилось строго ДО end.

    Граница исключительна: событие ровно в момент end НЕ попадает
    (ts == end → False). Верните булево по полю "ts".
    """
    if event["ts"]<end:
        return True
    else:
        return False


def events_in_window(events, start, end):
    """Возвращает события из полуинтервала [start, end) в исходном порядке.

    Событие попадает в окно, если оно
    at_or_after(start) И before(end)."""
    return [e for e in events if at_or_after(e, start) and before(e, end)]


# Пример использования:
# events = [
#     {"user_id": "u1", "type": "open", "ts": 1000},
#     {"user_id": "u1", "type": "view_item", "ts": 1100},
#     {"user_id": "u1", "type": "add_to_cart", "ts": 1200},
#     {"user_id": "u1", "type": "checkout", "ts": 1300},
# ]
# print(events_in_window(events, 1000, 1300))
# # [
# #   {"user_id": "u1", "type": "open", "ts": 1000},
# #   {"user_id": "u1", "type": "view_item", "ts": 1100},
# #   {"user_id": "u1", "type": "add_to_cart", "ts": 1200},
# # ]  # событие в ts=1300 не вошло — граница end исключается
