def get_square(side: float) -> float:
    """Функция принимает длину стороны квадрата и возвращает его площадь."""
    if side < 0:
        raise ValueError("Длина стороны не может быть отрицательной.")
    return side * side


def get_rectangle(length: float, width: float) -> float:
    """Функция принимает длины сторон прямоугольника и возвращает его площадь."""
    if length < 0 or width < 0:
        raise ValueError("Длины сторон не могут быть отрицательными.")
    return length * width


def triangle_area(base: float, height: float) -> float:
    """Функция принимает основание и высоту треугольника и возвращает его площадь."""
    if base < 0 or height < 0:
        raise ValueError("Основание и высота не могут быть отрицательными.")
    return 0.5 * base * height


__all__ = ["get_square", "get_rectangle", "triangle_area"]

if __name__ == "__main__":
    print(get_square(4))  # 16
    print(get_rectangle(5, 10))  # 50
    print(triangle_area(6, 8))  # 24
    print(get_square(-4))  # 0
