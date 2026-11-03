
def invert_roles(user_roles):
    """Переворачивает «пользователь → роль» в «роль → список пользователей»."""
    answer={}
    for user, role in user_roles.items():
        if role not in answer:
            answer[role]=[]
        answer[role].append(user)
    return answer