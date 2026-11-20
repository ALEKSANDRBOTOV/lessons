
def make_counter(start=0):
    """Создаёт функцию-счётчик, которая помнит своё значение между вызовами."""
    state={"value":start}
    def _count(by=1):
        state["value"]+=by
        return state["value"]
    return _count