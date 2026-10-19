def grade_score(score): """Переводит балл 0–100 в буквенную оценку A–F, отклоняя балл вне диапазона."""
    if score>100 or score<0:
        raise ValueError("score out of range")
    if isinstance(score, int):
        if isinstance(score, bool):
            raise ValueError("score must be an integer")
    if score>= 90:
        return "A"
    elif score>=80:
        return "B"
    elif score >=70:
        return"C"
    elif score >=60:
        return "D"
    else:
        return "F"
