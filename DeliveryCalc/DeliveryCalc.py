def shipping_cost(weight_grams, zone):
    """Считает стоимость доставки в копейках по весу и зоне, отклоняя тяжёлую посылку."""
    price=0
    if isinstance(weight_grams, bool) or not isinstance(weight_grams, int):
        raise ValueError("weight must be positive")
    if weight_grams < 1:
        raise ValueError("weight must be positive")

    elif weight_grams<=500:
        price=15000
    elif weight_grams<=2000:
        price=25000
    elif weight_grams<=10000:
        price=45000
    if zone=="msk":
        price+=0
    elif zone=="region":
        price+=15000
    elif zone=="remote":
        price+=40000
    else:
        raise ValueError(f"unknown zone: {zone}")
    if weight_grams>10000:
        raise ValueError("package too heavy")
    return price

