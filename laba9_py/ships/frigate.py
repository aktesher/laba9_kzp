from .ship import Ship

class Frigate(Ship):
    """
    Похідний клас для представлення фрегата, який є типом корабля.
    """

    def __init__(self, name, length, tonnage, weapons):
        """
        Ініціалізує новий фрегат.

        :param name: Назва фрегата
        :param length: Довжина фрегата в метрах
        :param tonnage: Вантажопідйомність фрегата в тоннах
        :param weapons: Кількість артилерійських установок
        """
        super().__init__(name, length, tonnage)
        self.weapons = weapons

    def attack(self):
        """
        Симулює атаку фрегата.
        """
        return f"{self.name} атакує з {self.weapons} артилерійськими установками!"

    def get_info(self):
        """
        Повертає інформацію про фрегат.
        """
        base_info = super().get_info()
        return f"{base_info}, Артилерійські установки: {self.weapons}"
