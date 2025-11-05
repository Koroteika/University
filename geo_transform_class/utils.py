from math import pi


class AngleConverter:
    """Класс для преобразования углов между градусами и радианами."""

    @staticmethod
    def deg_to_rad(degrees: float) -> float:
        """Преобразовать градусы в радианы.

        Args:
            degrees (float): Углы в градусах.

        Returns:
            float: Угол в радианах.
        """
        return degrees * (pi / 180)

    @staticmethod
    def rad_to_deg(radians: float) -> float:
        """Преобразовать радианы в градусы.

        Args:
            radians (float): Угол в радианах.

        Returns:
            float: Угол в градусах.
        """
        return radians * (180 / pi)
