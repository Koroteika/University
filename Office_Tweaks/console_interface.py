import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image


class ConsoleInterface:
    """Консольный интерфейс и логика программы"""

    def __init__(self):
        self.commands = {
            0: "Сменить рабочий каталог",
            1: "Преобразовать PDF в Word (docx)",
            2: "Преобразовать Word (docx) в PDF",
            3: "Произвести сжатие изображений",
            4: "Удалить группу файлов",
            5: "Выход",
        }

    def show_commands(self):
        "Показать доступные команды"
        for key, value in self.commands.items():
            print(f"{key}. {value}")

    def change_directory(self):
        "Сменить рабочий каталог"
        print("Введите путь к новому рабочему каталогу: ")
        new_directory = input()
        if os.path.exists(new_directory):
            os.chdir(new_directory)
            print("Рабочий каталог успешно изменен на:", new_directory)
        else:
            print("Некорректный путь к рабочему каталогу")

    def convert_pdf_to_word(self, file_path=None, all_files=False, workdir=None):
        "Преобразовать PDF в Word (docx)"
        original_dir = os.getcwd()

        if workdir:
            if not os.path.exists(workdir):
                print(f"Директория {workdir} не найдена")
                return
            os.chdir(workdir)

        if file_path:
            # Прямое указание файла
            if not os.path.exists(file_path):
                print(f"Файл {file_path} не найден")
                if workdir:
                    os.chdir(original_dir)
                return
            if not file_path.endswith(".pdf"):
                print("Файл должен иметь расширение .pdf")
                if workdir:
                    os.chdir(original_dir)
                return
            converter = Converter(file_path)
            converter.convert(file_path.replace(".pdf", ".docx"))
            converter.close()
            print(f"Файл успешно преобразован в Word (docx): {file_path}")
            if workdir:
                os.chdir(original_dir)
            return

        if all_files:
            pdf_files = [
                file for file in os.listdir(os.getcwd()) if file.endswith(".pdf")
            ]
            if not pdf_files:
                print("Файлы с расширением .pdf не найдены")
                if workdir:
                    os.chdir(original_dir)
                return
            for file in pdf_files:
                converter = Converter(file)
                converter.convert(file.replace(".pdf", ".docx"))
                converter.close()
            print("Файлы успешно преобразованы в Word (docx)")
            if workdir:
                os.chdir(original_dir)
            return

        pdf_files = [file for file in os.listdir(os.getcwd()) if file.endswith(".pdf")]

        if not pdf_files:
            print("Файлы с расширением .pdf не найдены")
            return

        print("Список файлов с расширением .pdf:")
        for index, file in enumerate(pdf_files, 1):
            print(f"{index}. {file}")

        file_number = int(
            input(
                "Введите номер файла для преобразования (0 для преобразования всех файлов): "
            )
        )

        if file_number == 0:
            for file in pdf_files:
                converter = Converter(file)
                converter.convert(file.replace(".pdf", ".docx"))
                converter.close()
            print("Файлы успешно преобразованы в Word (docx)")
        elif 1 <= file_number <= len(pdf_files):
            file_name = pdf_files[file_number - 1]
            converter = Converter(file_name)
            converter.convert(file_name.replace(".pdf", ".docx"))
            converter.close()
            print("Файл успешно преобразован в Word (docx):", file_name)
        else:
            print("Некорректный номер файла")

    def convert_word_to_pdf(self, file_path=None, all_files=False, workdir=None):
        "Преобразовать Word (docx) в PDF"
        original_dir = os.getcwd()

        if workdir:
            if not os.path.exists(workdir):
                print(f"Директория {workdir} не найдена")
                return
            os.chdir(workdir)

        if file_path:
            # Прямое указание файла
            if not os.path.exists(file_path):
                print(f"Файл {file_path} не найден")
                if workdir:
                    os.chdir(original_dir)
                return
            if not file_path.endswith(".docx"):
                print("Файл должен иметь расширение .docx")
                if workdir:
                    os.chdir(original_dir)
                return
            convert(file_path)
            print(f"Файл успешно преобразован в PDF: {file_path}")
            if workdir:
                os.chdir(original_dir)
            return

        if all_files:
            docx_files = [
                file for file in os.listdir(os.getcwd()) if file.endswith(".docx")
            ]
            if not docx_files:
                print("Файлы с расширением .docx не найдены")
                if workdir:
                    os.chdir(original_dir)
                return
            for file in docx_files:
                convert(file)
            print("Файлы успешно преобразованы в PDF")
            if workdir:
                os.chdir(original_dir)
            return

        docx_files = [
            file for file in os.listdir(os.getcwd()) if file.endswith(".docx")
        ]

        if not docx_files:
            print("Файлы с расширением .docx не найдены")
            return

        print("Список файлов с расширением .docx:")
        for index, file in enumerate(docx_files, 1):
            print(f"{index}. {file}")

        file_number = int(
            input(
                "Введите номер файла для преобразования (0 для преобразования всех файлов): "
            )
        )

        if file_number == 0:
            for file in docx_files:
                convert(file)
            print("Файлы успешно преобразованы в PDF")
        elif 1 <= file_number <= len(docx_files):
            file_name = docx_files[file_number - 1]
            convert(file_name)
            print("Файл успешно преобразован в PDF:", file_name)
        else:
            print("Некорректный номер файла")

    def compress_images(
        self, file_path=None, quality=None, all_files=False, workdir=None
    ):
        "Произвести сжатие изображений"
        original_dir = os.getcwd()

        if workdir:
            if not os.path.exists(workdir):
                print(f"Директория {workdir} не найдена")
                return
            os.chdir(workdir)

        if file_path and quality is not None and not all_files:
            # Прямое указание файла и качества
            if not os.path.exists(file_path):
                print(f"Файл {file_path} не найден")
                if workdir:
                    os.chdir(original_dir)
                return
            if not (
                file_path.endswith(".jpg")
                or file_path.endswith(".jpeg")
                or file_path.endswith(".png")
            ):
                print("Файл должен быть изображением (.jpg, .jpeg, .png)")
                if workdir:
                    os.chdir(original_dir)
                return
            if not (0 <= quality <= 100):
                print("Качество должно быть в диапазоне от 0 до 100")
                if workdir:
                    os.chdir(original_dir)
                return

            name, ext = os.path.splitext(file_path)
            compressed_name = f"{name}_compressed{ext}"

            try:
                image = Image.open(file_path)
                if ext.lower() in [".jpg", ".jpeg"]:
                    image.save(compressed_name, "JPEG", optimize=True, quality=quality)
                elif ext.lower() == ".png":
                    compress_level = 9 - int(quality / 100 * 9)
                    image.save(
                        compressed_name,
                        "PNG",
                        optimize=True,
                        compress_level=compress_level,
                    )
                else:
                    image.save(compressed_name, optimize=True, quality=quality)
                print(f"Изображение успешно сжато. Сохранено как: {compressed_name}")
            except Exception as e:
                print(f"Ошибка при сжатии изображения: {e}")
            if workdir:
                os.chdir(original_dir)
            return

        if all_files:
            # Обработка всех изображений
            image_files = [
                file
                for file in os.listdir(os.getcwd())
                if file.endswith(".jpg")
                or file.endswith(".jpeg")
                or file.endswith(".png")
            ]
            if not image_files:
                print("Изображения не найдены")
                if workdir:
                    os.chdir(original_dir)
                return

            if quality is None:
                quality = 75

            for file_name in image_files:
                name, ext = os.path.splitext(file_name)
                compressed_name = f"{name}_compressed{ext}"
                try:
                    image = Image.open(file_name)
                    if ext.lower() in [".jpg", ".jpeg"]:
                        image.save(
                            compressed_name, "JPEG", optimize=True, quality=quality
                        )
                    elif ext.lower() == ".png":
                        compress_level = 9 - int(quality / 100 * 9)
                        image.save(
                            compressed_name,
                            "PNG",
                            optimize=True,
                            compress_level=compress_level,
                        )
                    else:
                        image.save(compressed_name, optimize=True, quality=quality)
                    print(
                        f"Изображение {file_name} успешно сжато. Сохранено как: {compressed_name}"
                    )
                except Exception as e:
                    print(f"Ошибка при сжатии изображения {file_name}: {e}")
            if workdir:
                os.chdir(original_dir)
            return

        image_files = [
            file
            for file in os.listdir(os.getcwd())
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")
        ]
        if not image_files:
            print("Изображения не найдены")
            return
        print("Список изображений:")
        for index, file in enumerate(image_files, 1):
            print(f"{index}. {file}")
        print("Введите 0 для отмены")
        file_number = int(input("Введите номер файла для сжатия: "))

        if file_number == 0:
            return

        if not (1 <= file_number <= len(image_files)):
            print("Некорректный номер файла")
            return

        quality = int(input("Введите качество сжатия (0-100): "))
        if not (0 <= quality <= 100):
            print("Качество должно быть в диапазоне от 0 до 100")
            return

        file_name = image_files[file_number - 1]

        # Создаем имя для сжатой копии
        name, ext = os.path.splitext(file_name)
        compressed_name = f"{name}_compressed{ext}"

        try:
            image = Image.open(file_name)

            # Определяем формат для сохранения
            if ext.lower() in [".jpg", ".jpeg"]:
                image.save(compressed_name, "JPEG", optimize=True, quality=quality)
            elif ext.lower() == ".png":
                # Для PNG используем compress_level вместо quality
                # compress_level от 0 до 9, где 9 - максимальное сжатие
                compress_level = 9 - int(quality / 100 * 9)
                image.save(
                    compressed_name, "PNG", optimize=True, compress_level=compress_level
                )
            else:
                image.save(compressed_name, optimize=True, quality=quality)

            print(f"Изображение успешно сжато. Сохранено как: {compressed_name}")
        except Exception as e:
            print(f"Ошибка при сжатии изображения: {e}")

    def delete_files(self, mode=None, pattern=None, workdir=None):
        "Удалить группу файлов"
        original_dir = os.getcwd()

        if workdir:
            if not os.path.exists(workdir):
                print(f"Директория {workdir} не найдена")
                return
            os.chdir(workdir)

        if mode is not None:
            # Прямое указание режима и паттерна
            deleted_count = 0
            try:
                if mode == 1:  # starts_with
                    if pattern is None:
                        print("Для режима 'starts_with' требуется указать pattern")
                        if workdir:
                            os.chdir(original_dir)
                        return
                    for file in os.listdir(os.getcwd()):
                        if file.startswith(pattern):
                            os.remove(file)
                            print(f"Файл {file} успешно удален")
                            deleted_count += 1
                elif mode == 2:  # ends_with
                    if pattern is None:
                        print("Для режима 'ends_with' требуется указать pattern")
                        if workdir:
                            os.chdir(original_dir)
                        return
                    for file in os.listdir(os.getcwd()):
                        if file.endswith(pattern):
                            os.remove(file)
                            print(f"Файл {file} успешно удален")
                            deleted_count += 1
                elif mode == 3:  # contains
                    if pattern is None:
                        print("Для режима 'contains' требуется указать pattern")
                        if workdir:
                            os.chdir(original_dir)
                        return
                    for file in os.listdir(os.getcwd()):
                        if pattern in file:
                            os.remove(file)
                            print(f"Файл {file} успешно удален")
                            deleted_count += 1
                elif mode == 4:  # extension
                    if pattern is None:
                        print("Для режима 'extension' требуется указать pattern")
                        if workdir:
                            os.chdir(original_dir)
                        return
                    for file in os.listdir(os.getcwd()):
                        if file.endswith(f".{pattern}"):
                            os.remove(file)
                            print(f"Файл {file} успешно удален")
                            deleted_count += 1
                else:
                    print("Некорректный режим удаления")
                    if workdir:
                        os.chdir(original_dir)
                    return
                print(f"Удалено файлов: {deleted_count}")
            except Exception as e:
                print(f"Ошибка при удалении файлов: {e}")
            if workdir:
                os.chdir(original_dir)
            return

        print("Выберите режим удаления:")
        print("1. Удалить все файлы начинающиеся на определенную подстроку")
        print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
        print("3. Удалить все файлы содержащие определенную подстроку")
        print("4. Удалить все файлы с определенным расширением")
        print("5. Удалить все файлы")
        print("0. Выход")

        mode = int(input("Введите номер режима удаления: "))
        if mode == 0:
            return
        if mode == 1:
            substring = input("Введите подстроку для удаления: ")
            for file in os.listdir(os.getcwd()):
                if file.startswith(substring):
                    os.remove(file)
                    print(f"Файл {file} успешно удален")
        elif mode == 2:
            substring = input("Введите подстроку для удаления: ")
            for file in os.listdir(os.getcwd()):
                if file.endswith(substring):
                    os.remove(file)
                    print(f"Файл {file} успешно удален")
        elif mode == 3:
            substring = input("Введите подстроку для удаления: ")
            for file in os.listdir(os.getcwd()):
                if substring in file:
                    os.remove(file)
                    print(f"Файл {file} успешно удален")
        elif mode == 4:
            extension = input("Введите расширение для удаления: ")
            for file in os.listdir(os.getcwd()):
                if file.endswith(f".{extension}"):
                    os.remove(file)
                    print(f"Файл {file} успешно удален")
        elif mode == 5:
            for file in os.listdir(os.getcwd()):
                os.remove(file)
                print(f"Файл {file} успешно удален")
        else:
            print("Некорректный режим удаления")

    def run(self):
        "Запуск консольного интерфейса"
        while True:
            print("\nТекущий каталог:", os.getcwd(), "\n")
            self.show_commands()
            command = int(input("\nВведите номер команды: "))
            match command:
                case 0:
                    self.change_directory()
                case 1:
                    self.convert_pdf_to_word()
                case 2:
                    self.convert_word_to_pdf()
                case 3:
                    self.compress_images()
                case 4:
                    self.delete_files()
                case 5:
                    print("Выход из программы")
                    break
