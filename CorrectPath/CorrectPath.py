
def join_path(*parts):
    """Склеивает части пути в один путь с ведущим слэшем."""
    answer=[]
    for part in parts:
        if len(part)<1:
            continue
        else:
            answer.append(part)
    new_answer=["/"]
    for i in answer:
        if len(i.strip("/"))<1:
            continue
        else:
            new_answer.append(i.strip("/"))
    return new_answer[0]+"/".join(new_answer[1:])


# Пример использования:
# join_path("api", "v1", "users")  # "/api/v1/users"
