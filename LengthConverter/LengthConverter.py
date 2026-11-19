
def convert_unit(value, from_unit, to_unit):
    """Переводит длину из одной единицы (мм/см/м/км) в другую."""
    APPLY_UNIT={"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
    if from_unit not in APPLY_UNIT:
        raise ValueError(f"unknown unit: {from_unit}")
    if to_unit not in APPLY_UNIT:
        raise ValueError(f"unknown unit: {to_unit}")
    meters = value * APPLY_UNIT[from_unit]
    result = meters / APPLY_UNIT[to_unit]
    
    return round(result, 6)


# Пример использования:
# convert_unit(1, "km", "m")  # 1000.0
