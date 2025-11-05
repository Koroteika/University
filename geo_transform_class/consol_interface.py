from .transformations import CoordinateConverter
from .file_operations import FileManager


class ConsoleInterface:
    """Класс для консольного интерфейса взаимодействия с пакетом."""

    def __init__(self):
        """Инициализация консольного интерфейса."""
        self.coordinate_converter = CoordinateConverter()
        self.file_manager = FileManager()

    def run(self) -> None:
        """Запуск консольного интерфейса."""
        while True:
            print("\n" + "=" * 50)
            print("Выберите функцию:")
            print("1. Преобразование декартовых координат в сферические")
            print("2. Преобразование сферических координат в декартовые")
            print("3. Преобразование координат из файла")
            print("4. Изменить файл для записи результатов")
            print("0. Выход из программы")
            print("=" * 50)

            try:
                choice = input("Введите номер функции (0-4): ").strip()

                match choice:
                    case "1":  # Декартовые в сферические
                        self._handle_cartesian_to_spherical()

                    case "2":  # Сферические в декартовые
                        self._handle_spherical_to_cartesian()

                    case "3":  # Чтение координат из файла
                        self._handle_file_conversion()

                    case "4":  # Изменить файл для записи результатов
                        self._handle_change_output_file()

                    case "0":  # Выход
                        print("Выход из программы.")
                        break

                    case _:  # Некорректный ввод
                        print("Некорректный ввод. Пожалуйста, введите число от 0 до 4.")

            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число от 0 до 4.")
            except KeyboardInterrupt:
                print("\n\nВыход из программы.")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")

    def _handle_cartesian_to_spherical(self) -> None:
        """Обработка преобразования декартовых координат в сферические."""
        try:
            x = float(input("Введите координату x: "))
            y = float(input("Введите координату y: "))
            z = float(input("Введите координату z: "))

            r, teta, fi = self.coordinate_converter.cartesian_to_spherical(x, y, z)
            result = f"Декартовы координаты (x, y, z): ({x}, {y}, {z}) -> Сферические координаты (r, θ, ϕ): ({r:.6f}, {teta:.6f}, {fi:.6f})"
            print(result)
            self.file_manager.write_results_to_file(result)

        except ValueError:
            print("Ошибка: введите корректные числовые значения.")

    def _handle_spherical_to_cartesian(self) -> None:
        """Обработка преобразования сферических координат в декартовые."""
        try:
            r = float(input("Введите радиус r: "))
            teta = float(input("Введите азимутальный угол θ (в градусах): "))
            fi = float(input("Введите полярный угол ϕ (в градусах): "))

            x, y, z = self.coordinate_converter.spherical_to_cartesian(r, teta, fi)
            result = f"Сферические координаты (r, θ, ϕ): ({r}, {teta}, {fi}) -> Декартовы координаты (x, y, z): ({x:.6f}, {y:.6f}, {z:.6f})"
            print(result)
            self.file_manager.write_results_to_file(result)

        except ValueError:
            print("Ошибка: введите корректные числовые значения.")

    def _handle_file_conversion(self) -> None:
        """Обработка преобразования координат из файла."""
        try:
            filename = input("Введите имя файла для чтения координат: ").strip()
            if not filename:
                print("Ошибка: имя файла не может быть пустым.")
                return

            coords = self.file_manager.read_coordinates_from_file(filename)

            if not coords:
                print("Файл не содержит корректных координат.")
                return

            print(f"\nНайдено {len(coords)} наборов координат:")
            for idx, coord in enumerate(coords, start=1):
                try:
                    x, y, z = coord
                    r, teta, fi = self.coordinate_converter.cartesian_to_spherical(
                        x, y, z
                    )
                    result = f"Набор {idx}: Декартовы координаты (x, y, z): ({x}, {y}, {z}) -> Сферические координаты (r, θ, ϕ): ({r:.6f}, {teta:.6f}, {fi:.6f})"
                    print(result)
                    self.file_manager.write_results_to_file(result)
                except Exception as e:
                    print(f"Ошибка при обработке набора {idx}: {e}")

        except Exception as e:
            print(f"Ошибка при обработке координат из файла: {e}")

    def _handle_change_output_file(self) -> None:
        """Обработка изменения файла для записи результатов."""
        filename = input(
            f"Введите имя файла для записи результатов (текущий: {self.file_manager.default_output_file}): "
        ).strip()
        if filename:
            self.file_manager.set_default_output_file(filename)
            print(f"Файл для записи результатов изменен на: {filename}")
        else:
            print("Имя файла не было изменено.")


def console():
    """Функция для обратной совместимости."""
    interface = ConsoleInterface()
    interface.run()


if __name__ == "__main__":
    console()
