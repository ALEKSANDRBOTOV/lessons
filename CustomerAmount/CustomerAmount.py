
def summarize_orders(orders):
    """Сворачивает заказы в словарь «клиент → {orders, total}»."""
    report={}
    for order in orders:
        amount=order["amount"]
        if amount<=0:
            continue
        customer=order["customer"]

        if customer not in report:
            report[customer]={"orders": 0, "total": 0}
        report[customer]["orders"]+=1
        report[customer]["total"]+=amount
    return report


# Пример использования:
# summarize_orders([{"customer": "ann", "amount": 100}, {"customer": "ann", "amount": 200}])
# {"ann": {"orders": 2, "total": 300}}