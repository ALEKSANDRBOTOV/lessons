
def type_with_backspace(keystrokes):
    """Собирает итоговый текст редактора из нажатий."""
    answer=[]
    for index, char in enumerate(keystrokes):
        if char!="<-":
            answer.append(char)
        elif char=="<-":
            if len(answer)==0:
                continue
            else:
                answer.pop()
    return "".join(answer)

# Пример использования:
# print(type_with_backspace(["h", "e", "l", "<-", "l", "o"]))  # "helo"
