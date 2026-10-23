def run_ledger(operations, cap_kopecks):
    """Прогоняет ленту операций по балансу в копейках с потолком и защитой от минуса."""
    balance=0
    if cap_kopecks<=0:
        raise ValueError("cap must be positive")
    
    for op, amount in operations:
        if amount<0:
            raise ValueError("amount must not be negative")
        if "deposit" == op:
            balance+=amount
            if balance>cap_kopecks:
                balance=cap_kopecks
        elif "withdraw" == op:
            if balance<amount:
                raise ValueError("insufficient balance")
            else:
                balance-=amount
        elif "fee" == op:
            if (balance-amount)<0:
                balance=0
            else:
                balance-=amount
        else:
            raise ValueError(f"unknown op: {op}")
    return balance

