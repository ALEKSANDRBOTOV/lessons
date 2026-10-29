
def convert_temperature(value, from_unit, to_unit):
    """Переводит температуру между шкалами c/f/k, отклоняя незнакомую единицу."""
    correct_t=["c", "f", "k"]
    if from_unit not in correct_t:
        raise ValueError(f"unknown unit: {from_unit}")
    if to_unit not in correct_t:
            raise ValueError(f"unknown unit: {to_unit}")
    if from_unit==to_unit:
        return float(value)
    C_in_K=value+273.15
    C_in_F=value*9/5+32
    K_in_F=(value-273.15)*9/5+32
    K_in_C=value-273.15
    F_in_K=(value-32)*5/9+273.15
    F_in_C=(value-32)*5/9
    result=0.0
    if from_unit=="c" and to_unit=="f":
        result=C_in_F
    elif from_unit=="c" and to_unit=="k":
        result=C_in_K
    elif from_unit=="k" and to_unit=="c":
        result=K_in_C
    elif from_unit=="k" and to_unit=="f":
        result=K_in_F
    elif from_unit=="f" and to_unit=="c":
        result=F_in_C
    else:
        result=F_in_K
    return result