def first_failure(statuses):
    error=-1
    for number, result in enumerate(statuses): # Enumerat помогает работать с индексами массива
        if result=="ok":
            continue
        else :
            error=number
            break
    return error
