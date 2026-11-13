
class GiftCard:
    """Подарочная карта кофейни: код и баланс в копейках."""
    def __init__(self, code, kopecks):
        self.code = code
        self.kopecks = kopecks

    def label(self):
        rubles = self.kopecks // 100
        kop = self.kopecks % 100
        return f"Карта {self.code}: {rubles},{kop:02d} ₽"

    def balance(self):
        return self.kopecks

class HousePlant:
    """Растение из напоминалки полива: имя и интервал в днях."""

    def __init__(self, name, water_every_days):
        self.name=name
        self.water_every_days=water_every_days

    def needs_water(self, x):
        if x>=self.water_every_days:
            return True
        else:
            return False


    def schedule_line(self):
        return f"{self.name}: полив раз в {self.water_every_days} дн."

class ParkingSpot:
    """Парковочное место бизнес-центра: номер и признак «крытое»."""

    def __init__(self,number,is_covered):
        self.number=number
        self.is_covered=is_covered

    def fee_kopecks(self, base_kopecks):
            if self.is_covered:
                dop=base_kopecks * 25 // 100
                return base_kopecks+dop
            return base_kopecks

    def title(self):
        return f"Место {self.number}"

class Recipe:
    """Рецепт из кулинарного блокнота с базовой раскладкой."""

    def __init__(self,name,base_servings,grams_per_serving):
        self.name=name
        self.base_servings=base_servings
        self.grams_per_serving=grams_per_serving

    def grams_for(self,serving):
        if 0:
            return 0
        else:
            return self.grams_per_serving*serving

    def card(self):
        return f"{self.name} · базово {self.base_servings} порц."


# Пример использования:
# recipe = Recipe("Плов", 4, 350)
# print(recipe.grams_for(6))  # 2100
# print(recipe.card())  # Плов · базово 4 порц.

class TrainTicket:
    """Билет на поезд: пассажир, место вида «12A», цена в копейках."""

    def __init__(self, passenger, seat, price_kopecks):
        self.passenger=passenger
        self.seat=seat
        self.price_kopecks=price_kopecks

    def price_label(self):
        rub=self.price_kopecks//100
        kop=self.price_kopecks%100
        return f"{rub},{kop:02d} ₽"

    def is_window(self):
        if self.seat[-1] in ("A", "D"):
            return True
        else:
            return False

    def summary(self):
        if self.is_window():
            return f"{self.passenger}, место {self.seat}, у окна"
        else:
            return f"{self.passenger}, место {self.seat}"