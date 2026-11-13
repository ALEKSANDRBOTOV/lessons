
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