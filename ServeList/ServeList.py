
from collections import deque


def serve_print_queue(events: list) -> list:
    """Проиграйте события очереди печати и верните имена выданных документов."""
    queue = deque()
    answer = []

    for event in events:
        if event.startswith("add:"):
            # Добавляем документ в конец очереди ожидания
            doc_name = event[4:]
            queue.append(doc_name)
        elif event == "serve":
            # Если в очереди есть документы, выдаём самый первый (слева)
            if queue:
                answer.append(queue.popleft())

    return answer
