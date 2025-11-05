from typing import List, Tuple


class FileManager:
    """Класс для работы с файлами для чтения и записи координат."""

    def __init__(self, default_output_file: str = "results.txt"):
        """Инициализация менеджера файлов.

        Args:
            default_output_file (str): Имя файла по умолчанию для записи результатов.
        """
        self.default_output_file = default_output_file

    def write_results_to_file(self, data: str, filename: str = None) -> None:
        """Запись результатов в файл.

        Args:
            data (str): Данные для записи.
            filename (str, optional): Имя файла. Если не указано, используется файл по умолчанию.
        """
        if filename is None:
            filename = self.default_output_file

        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(data + "\n")
        except IOError as e:
            print(f"Ошибка при записи в файл '{filename}': {e}")

    def read_coordinates_from_file(
        self, filename: str
    ) -> List[Tuple[float, float, float]]:
        """Чтение координат из файла.

        Args:
            filename (str): Имя файла для чтения.

        Returns:
            List[Tuple[float, float, float]]: Список кортежей координат (x, y, z).
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден.")
            return []

        coords = []
        for line_num, line in enumerate(lines, start=1):
            parts = line.strip().split()
            if len(parts) == 3:
                try:
                    coords.append(tuple(map(float, parts)))
                except ValueError:
                    print(f"Пропущена строка {line_num} (не числа): {line.strip()}")
            elif line.strip():  # Игнорируем пустые строки
                print(
                    f"Пропущена строка {line_num} (неверное количество значений): {line.strip()}"
                )

        return coords

    def set_default_output_file(self, filename: str) -> None:
        """Установить файл по умолчанию для записи результатов.

        Args:
            filename (str): Имя файла.
        """
        self.default_output_file = filename
