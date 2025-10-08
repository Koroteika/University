def get_perimetr(*args):
    """Функция принимает длины сторон многоугольника и возвращает его периметр."""
    return sum(args)


if __name__ == "__main__":
    print(get_perimetr(10, 20, 30))  # 60
    print(get_perimetr(5, 5, 5, 5))  # 20
    print(get_perimetr(7, 3))  # 10
    print(get_perimetr(0))  # 0
