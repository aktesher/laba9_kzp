class Ship:
    """
    Базовий клас для представлення корабля.
    """

    def __init__(self, name, length, tonnage):
        """
        Ініціалізує новий корабель.

        :param name: Назва корабля
        :param length: Довжина корабля в метрах
        :param tonnage: Вантажопідйомність корабля в тоннах
        """
        self.name = name
        self.length = length
        self.tonnage = tonnage

    def sail(self):
        """
        Симулює рух корабля.
        """
        return f"{self.name} вирушає в море!"

    def get_info(self):
        """
        Повертає інформацію про корабель.
        """
        return f"Корабель '{self.name}': Довжина {self.length} м, Вантажопідйомність {self.tonnage} т."
