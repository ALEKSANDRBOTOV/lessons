VALID_TYPES = {"open", "view_item", "add_to_cart", "checkout", "purchase"}


def parse_events(lines):
    """Готово (из задачи «Разбор потока событий»): строки → события-словари."""
    events = []
    for line in lines:
        user_id, type_, ts = line.split(",")
        events.append({"user_id": user_id, "type": type_, "ts": int(ts)})
    return events


def keep_valid_types(events):
    """Готово: оставляет только события, чей type есть в VALID_TYPES."""
    return [e for e in events if e["type"] in VALID_TYPES]


def event_ts(event):
    """Готово (из задачи «Сортировка событий по времени»): ключ сортировки — ts."""
    return event["ts"]


def sort_by_time(events):
    """Готово: возвращает события, отсортированные по ts по возрастанию (стабильно)."""
    return sorted(events, key=event_ts)


def clean_event_stream(lines):
    """Собирает чистый поток из сырых строк лога — соедините три готовых шага.

    Конвейер ровно в этом порядке:
      1. parse_events(lines)      — разобрать строки в события-словари;
      2. keep_valid_types(...)    — выкинуть события с чужими типами;
      3. sort_by_time(...)        — упорядочить оставшееся по ts.
    Верните результат последнего шага. Все три функции уже готовы выше —
    писать их заново не нужно, только вызвать в правильном порядке.
    """
    return sort_by_time(keep_valid_types(parse_events(lines)))


# Пример использования:
# lines = [
#     "u2,open,2000",
#     "u1,open,1000",
#     "u1,bad_type,1050",
#     "u1,view_item,1100",
# ]
# print(clean_event_stream(lines))
# # [
# #   {"user_id": "u1", "type": "open", "ts": 1000},
# #   {"user_id": "u1", "type": "view_item", "ts": 1100},
# #   {"user_id": "u2", "type": "open", "ts": 2000},
# # ]  # bad_type выкинут, остальное отсортировано по ts
