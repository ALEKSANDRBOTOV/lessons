
class HitCounter:
    def __init__(self):
        self._counts = {}

    def hit(self, key):
        self._counts[key] = self._counts.get(key, 0) + 1
        return self._counts[key]

    def count(self, key):
        return self._counts.get(key, 0)

    def total(self):
        return sum(self._counts.values())

    



# Пример использования:
# counter = HitCounter()
# counter.hit("a")     # 1
# counter.hit("a")     # 2
# counter.count("a")   # 2
# counter.total()      # 2