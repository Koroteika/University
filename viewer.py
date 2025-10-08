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
        print("5. Периметр многоугольника из файла")
        try:
            choice = int(input("Введите номер функции (1-5) или 0 для выхода: "))
            match choice:
                case 1:  # Площадь квадрата
                    side = float(input("Введите длину стороны квадрата: "))
                    result = (
                        f"Площадь квадрата со стороной {side} равна {get_qguare(side)}"
                    )
                    print(result)
                    write_file(result)

                case 2:  # Площадь прямоугольника
                    length = float(input("Введите длину прямоугольника: "))
                    width = float(input("Введите ширину прямоугольника: "))
                    result = f"Площадь прямоугольника {length}x{width} равна {get_rectangle(length, width)}"
                    print(result)
                    write_file(result)

                case 3:  # Площадь треугольника
                    base = float(input("Введите основание треугольника: "))
                    height = float(input("Введите высоту треугольника: "))
                    result = f"Площадь треугольника с основанием {base} и высотой {height} равна {triangle_area(base, height)}"
                    print(result)
                    write_file(result)

                case 4:  # Периметр многоугольника
                    sides = input("Введите длины сторон многоугольника через пробел: ")
                    sides = list(map(float, sides.split()))
                    result = f"Периметр многоугольника с сторонами {sides} равен {get_perimetr(*sides)}"
                    print(result)
                    write_file(result)

                case 5:  # Записать результат в файл
                    path = input("Введите путь к файлу с длинами сторон: ")
                    input_list = read_file(path)
                    if input_list:
                        for i, lengths in enumerate(input_list, start=1):
                            result = f"Периметр многоугольника {i} с сторонами {lengths} равен {get_perimetr(*lengths)}"
                            print(result)
                            write_file(result)

                case 0:  # Выход
                    print("Выход из программы.")
                    break

        except ValueError as ve:
            print(f"Ошибка ввода: {ve}")
            continue


if __name__ == "__main__":
    show()
