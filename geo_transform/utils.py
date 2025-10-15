from math import pi


def deg_to_rad(degrees: float) -> float:
    """Преобразовать градусы в радианы.

    Args:
        degrees (float): Угол в градусах.

    Returns:
        radians (float): Угол в радианах.
    """
    return degrees * (pi / 180)


def rad_to_deg(radians: float) -> float:
    """Преобразовать радианы в градусы.

    Args:
        radians (float): Угол в радианах.

    Returns:
        degrees (float): Угол в градусах.
    """

    return radians * (180 / pi)


if __name__ == "__main__":
    a = deg_to_rad(45)
    b = rad_to_deg(0.7853981633974483)
    print(a)
    print(b)
