
def average_rating(counts):
    """Возвращает среднюю оценку, обрезанную до одного знака после запятой."""
    sum_bal=(counts[0]*1+ counts[1]*2+counts[2]*3+counts[3]*4+counts[4]*5)
    count_bal=(counts[0]+counts[1]+counts[2]+counts[3]+counts[4])
    if count_bal==0:
        count_bal=0.0
        return count_bal
    answer=sum_bal/count_bal
    return int(answer*10)/10 # округляем в меньшую сторону