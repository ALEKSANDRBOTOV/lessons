
def join_names(names):
    """Собирает список имён в строку вида «Аня, Боб и Вера»."""
    if not names:
        return ""
    elif len(names)==1:
        answer=names[0]
        return answer
    else:
        for name in names:
            start=(", ").join(names[:-1])
        return (f"{start} и {names[-1]}")