from ships.ship import Ship
from ships.frigate import Frigate

def display_menu():
    """
    Відображає меню взаємодії з користувачем.
    """
    print("\n=== Меню ===")
    print("1. Створити корабель")
    print("2. Створити фрегат")
    print("3. Показати інформацію про корабель")
    print("4. Показати інформацію про фрегат")
    print("5. Вийти")

def main():
    """
    Точка входу в програму.
    """
    ship = None
    frigate = None

    while True:
        display_menu()
        choice = input("Оберіть пункт меню (1-5): ")

        if choice == "1":
            name = input("Введіть назву корабля: ")
            length = float(input("Введіть довжину корабля: "))
            tonnage = float(input("Введіть вантажопідйомність корабля: "))
            ship = Ship(name, length, tonnage)
            print(f"Корабель '{name}' створено.")

        elif choice == "2":
            name = input("Введіть назву фрегата: ")
            length = float(input("Введіть довжину фрегата: "))
            tonnage = float(input("Введіть вантажопідйомність фрегата: "))            
            weapons = input("Введіть тип озброєння фрегата: ")
            frigate = Frigate(name, length, tonnage, weapons)
            print(f"Фрегат '{name}' створено.")

        elif choice == "3":
            if ship:
                print("\nІнформація про корабель:")
                print(ship.get_info())
            else:
                print("Корабель ще не створено.")

        elif choice == "4":
            if frigate:
                print("\nІнформація про фрегат:")
                print(frigate.get_info())
            else:
                print("Фрегат ще не створено.")

        elif choice == "5":
            print("Вихід із програми.")
            break

        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
