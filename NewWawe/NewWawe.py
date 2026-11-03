
def count_events(events):
    """Считает, сколько раз встретился каждый тип события в логе."""
    answer={}
    for event in events:
        if event in events:
            answer[event]=answer.get(event, 0)+1
    return answer
