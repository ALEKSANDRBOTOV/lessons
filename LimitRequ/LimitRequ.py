def prune_window(timestamps, now, window):
    """Возвращает моменты, которые ещё попадают в окно от now."""
    first=[]
    for t in timestamps:
        if t>(now-window):
            first.append(t)
    return first

def is_allowed(timestamps, now, window, limit):
    """Поместится ли ещё один запрос в момент now, не превысив лимит."""
    cleaned = prune_window(timestamps, now, window)

    return len(cleaned) < limit


def record_request(timestamps, now, window, limit):
    """Обрабатывает запрос: возвращает (разрешён, новая история)."""
    cleaned = prune_window(timestamps, now, window)
    if len(cleaned) < limit:

        return True, cleaned + [now]
    else:
    
        return False, cleaned
