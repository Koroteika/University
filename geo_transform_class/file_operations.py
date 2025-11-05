def write_results_to_file(filename: str, data: str):
    """Запись результатов в файл."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(data + "\n")


def read_coordinates_from_file(filename: str):
    """Чтение координат из файла."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return []

    coords = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            try:
                coords.append(tuple(map(float, parts)))
            except ValueError:
                print(f"Пропущена строка (не числа): {line.strip()}")
    return coords
