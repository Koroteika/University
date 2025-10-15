import geo_transform as gt

# Проверка функций
r, theta, phi = gt.cartesian_to_spherical(1, 2, 3)
print("cartesian_to_spherical:", r, theta, phi)

x, y, z = gt.spherical_to_cartesian(5, 45, 60)
print("spherical_to_cartesian:", x, y, z)

# Проверка конвертации углов
print("deg_to_rad(180):", gt.deg_to_rad(180))
print("rad_to_deg(3.14159):", gt.rad_to_deg(3.14159))

# Проверка работы с файлами
gt.write_results_to_file("test_results.txt", "Тестовая запись")
coords = gt.read_coordinates_from_file("input.txt")
print("Координаты из файла:", coords)
