def split_bill(total_kopecks, people):
    """Делит счёт в копейках поровну между плательщиками с раздачей остатка."""
    if people <=0:
        raise ValueError("people must be positive")
    if total_kopecks<0:
        raise ValueError("total must not be negative")
    part=total_kopecks//people
    miss=total_kopecks%people
    receipt=[]
    for ch in range(people):
        if miss!=0:
            receipt.append(part+1)
            miss-=1
        else:
            receipt.append(part)
    return receipt
