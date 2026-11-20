
def running_max(numbers):
    """Возвращает список рекордов: на позиции i — максимум среди numbers[0..i]."""
    answer=[]
    if len(numbers)==1:
        answer.append(numbers[0])
        return  answer
    for index, i in enumerate(numbers):
        if index==0:
            answer.append(i)
        elif i >=answer[-1]:
            answer.append(i)
        else:
            answer.append(answer[-1])
    return answer



# Пример использования:
# running_max([3, 1, 4, 1, 5])  # [3, 3, 4, 4, 5]
