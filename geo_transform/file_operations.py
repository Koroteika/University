def write_results_to_file(filename: str, data: str):
    """Запись результатов в файл."""
    with open(filename, "w") as file:
        file.write(data)


def read_coordinates_from_file(filename: str):
    """Чтение координат из файла."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    coords = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            coords.append(tuple(map(float, parts)))
    return coords
