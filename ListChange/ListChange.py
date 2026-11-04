
def limit_for(plans, plan, limit):
    """Возвращает значение лимита для тарифа, запасное значение или ноль."""
    if limit in plans.get(plan, {}):
        return plans[plan][limit]
        
    return plans.get("default", {}).get(limit, 0)




# Пример использования:
# limit_for({"default": {"seats": 1}, "team": {"seats": 10}}, "team", "seats")
# # 10
