from math import sqrt, atan2, sin, cos
from .utils import *


def cartesian_to_spherical(x: float, y: float, z: float) -> float:
    """Преобразование декартовых координат в сферические

    Args:
        x (float): координата x.
        y (float): координата y.
        z (float): координата z.

    Returns:
        θ (float): азимутальный угол в градусах.
        ϕ (float): полярный угол в градусах.
    """
    r = sqrt(x**2 + y**2 + z**2)
    teta = 2 * atan2(y, x + sqrt(x**2 + y**2))
    fi = atan2(sqrt(x**2 + y**2), z)

    teta = rad_to_deg(teta)
    fi = rad_to_deg(fi)

    return r, teta, fi


def spherical_to_cartesian(r: float, teta: float, fi: float) -> float:
    """Преобразование сферических координат в декартовые

    Args:
        r (float): радиус.
        θ (float): азимутальный угол в градусах.
        ϕ (float): полярный угол в градусах.

    Returns:
        x (float): координата x.
        y (float): координата y.
        z (float): координата z.
    """
    # Переводим все в радианы
    teta = deg_to_rad(teta)
    fi = deg_to_rad(fi)
    r = deg_to_rad(r)

    x = r * sin(fi) * cos(teta)
    y = r * sin(fi) * sin(teta)
    z = r * cos(fi)

    return x, y, z
