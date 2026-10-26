
def mask_email(email):
    if email.count("@")!=1:
        raise ValueError("invalid email")
    name, dom= email.split("@")
    if len(name)==0 or len(dom)==0:
        raise ValueError("invalid email")
    if len(name)==1:
        return (name[0]+"***"+"@"+dom)
    return(name[0]+"***"+name[-1]+"@"+dom)