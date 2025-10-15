from transformations import *
from utils import *
from file_operations import *


def console():
    while True:
        print("Выберите функцию: ")
        print("1. Преобразование декартовых координат в сферические")
        print("2. Преобразование сферических координат в декартовые")
        print("0. Выход из программы")
        try:
            choice = int(input("Введите номер функции (1-2) или 0 для выхода: "))
            match choice:
                case 1:  # Декартовые в сферические
                    x = float(input("Введите координату x: "))
                    y = float(input("Введите координату y: "))
                    z = float(input("Введите координату z: "))
                    r, teta, fi = cartesian_to_spherical(x, y, z)
                    result = f"Сферические координаты (r, θ, ϕ): ({r}, {teta}, {fi})"
                    print(result)
                    write_results_to_file("results.txt", result)

                case 2:  # Сферические в декартовые
                    r = float(input("Введите радиус r: "))
                    teta = float(input("Введите азимутальный угол θ (в градусах): "))
                    fi = float(input("Введите полярный угол ϕ (в градусах): "))
                    x, y, z = spherical_to_cartesian(r, teta, fi)
                    result = f"Декартовы координаты (x, y, z): ({x}, {y}, {z})"
                    print(result)
                    write_results_to_file("results.txt", result)

                case 3:  # Чтение координат из файла
                    filename = input("Введите имя файла для чтения координат: ")
                    coords = read_coordinates_from_file(filename)
                    try:
                        for coord in coords:
                            x, y, z = coord
                            r, teta, fi = cartesian_to_spherical(x, y, z)
                            result = f"Декартовы координаты (x, y, z): ({x}, {y}, {z}) -> Сферические координаты (r, θ, ϕ): ({r}, {teta}, {fi})"
                            print(result)
                            write_results_to_file("results.txt", result)
                    except Exception as e:
                        print(f"Ошибка при обработке координат из файла: {e}")

                case 0:  # Выход
                    print("Выход из программы.")
                    break

                case _:  # Некорректный ввод
                    print("Некорректный ввод. Пожалуйста, введите число от 0 до 2.")

        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число от 0 до 2.")
