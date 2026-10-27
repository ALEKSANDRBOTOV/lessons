
def truncate_text(text, limit):
    if limit < 1:
        raise ValueError("limit must be at least 1")
    if len(text) <= limit:
        return text
        
    new_text = text.split(" ")
    answer = ""
    window_limit = limit - 1
    
    for i, piece in enumerate(new_text):
        separator = "" if i == 0 else " "
        
        # Проверяем, помещается ли текущий кусок (будь то слово или пустая строка от двойного пробела)
        if len(answer + separator + piece) <= window_limit:
            answer += separator + piece
        else:
            # Если элемент не поместился, но это самое первое длинное слово (или перед ним были только пробелы)
            if answer.strip() == "":
                remaining_space = window_limit - len(answer) - len(separator)
                if remaining_space > 0:
                    answer += separator + piece[:remaining_space]
            break
            
    return answer.rstrip() + "…"