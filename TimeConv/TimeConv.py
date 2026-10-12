def format_duration(seconds): # конвертируем въодящее число в запись времени
    if seconds < 0 or not isinstance(seconds, (int, float)) or seconds != int(seconds):
        raise ValueError("invalid duration")
        return (f"{int(seconds)}s")
    s=int(seconds%3600%60)
    m=int(seconds%3600/60)
    h=seconds//3600   
    if h==0 and m!=0 and s!=0:
        return (f"{m}m{s}s")
    elif h!=0 and m!=0 and s==0:
        return (f"{h}h{m}m")
    elif h!=0 and m==0 and s!=0:
        return (f"{h}h{s}s")    
    elif h==0 and m!=0 and s==0:
        return (f"{m}m")
    elif h!=0 and m==0 and s==0:
        return (f"{h}h")
    elif m==0:
        return (f"{s}s")
    elif s==0:
        return (f"{h}h{m}m")
    elif h!=0 and m!=0 and s!=0:
        return (f"{h}h{m}m{s}s")