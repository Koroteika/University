from math import sqrt, atan2, sin, cos
from .utils import AngleConverter


class CoordinateConverter:
    """Класс для преобразования координат между декартовой и сферической системами координат."""

    def __init__(self):
        """Инициализация конвертера координат."""
        self.angle_converter = AngleConverter()

    def cartesian_to_spherical(
        self, x: float, y: float, z: float
    ) -> tuple[float, float, float]:
        """Преобразование декартовых координат в сферические.

        Args:
            x (float): координата x.
            y (float): координата y.
            z (float): координата z.

        Returns:
            tuple[float, float, float]: Кортеж (r, θ, ϕ), где:
                r (float): радиус.
                θ (float): азимутальный угол в градусах.
                ϕ (float): полярный угол в градусах.
        """
        r = sqrt(x**2 + y**2 + z**2)
        teta = 2 * atan2(y, x + sqrt(x**2 + y**2))
        fi = atan2(sqrt(x**2 + y**2), z)

        teta = self.angle_converter.rad_to_deg(teta)
        fi = self.angle_converter.rad_to_deg(fi)

        return r, teta, fi

    def spherical_to_cartesian(
        self, r: float, teta: float, fi: float
    ) -> tuple[float, float, float]:
        """Преобразование сферических координат в декартовые.

        Args:
            r (float): радиус.
            teta (float): азимутальный угол в градусах.
            fi (float): полярный угол в градусах.

        Returns:
            tuple[float, float, float]: Кортеж (x, y, z).
        """
        # Переводим все в радианы
        teta = self.angle_converter.deg_to_rad(teta)
        fi = self.angle_converter.deg_to_rad(fi)

        x = r * sin(fi) * cos(teta)
        y = r * sin(fi) * sin(teta)
        z = r * cos(fi)

        return x, y, z
