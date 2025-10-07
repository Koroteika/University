from square import *
from perimetr import *
from text_handler import *

_all_ = ["show"]


def show():
    while True:
        print("Выберите функцию: ")
        print("1. Площадь квадрата")
        print("2. Площадь прямоугольника")
        print("3. Площадь треугольника")
        print("4. Периметр многоугольника")
        print("5. Записать результат в файл")
        try:
            choice = int(input("Введите номер функции (1-5) или 0 для выхода: "))
            match choice:
                case 1:  # Площадь квадрата
                    side = float(input("Введите длину стороны квадрата: "))
                    result = (
                        f"Площадь квадрата со стороной {side} равна {get_qguare(side)}"
                    )

                case 2:  # Площадь прямоугольника
                    length = float(input("Введите длину прямоугольника: "))
                    width = float(input("Введите ширину прямоугольника: "))
                    result = f"Площадь прямоугольника {length}x{width} равна {get_rectangle(length, width)}"

                case 3:  # Площадь треугольника
                    base = float(input("Введите основание треугольника: "))
                    height = float(input("Введите высоту треугольника: "))
                    result = f"Площадь треугольника с основанием {base} и высотой {height} равна {triangle_area(base, height)}"

                case 4:  # Периметр многоугольника
                    sides = input("Введите длины сторон многоугольника через пробел: ")
                    sides = list(map(float, sides.split()))
                    result = f"Периметр многоугольника с сторонами {sides} равен {get_perimetr(*sides)}"

                case 5:  # Записать результат в файл
                    pass

                case 0:  # Выход
                    print("Выход из программы.")
                    break

        except ValueError as ve:
            print(f"Ошибка ввода: {ve}")
            continue
