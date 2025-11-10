import os


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
        print("\nТекущий каталог: ", os.getcwd(), "\n")
        for key, value in self.commands.items():
            print(f"{key}. {value}")

    def run(self):
        "Запуск консольного интерфейса"
        while True:
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

    def change_directory(self):
        "Сменить рабочий каталог"
        pass

    def convert_pdf_to_word(self):
        "Преобразовать PDF в Word (docx)"
        pass

    def convert_word_to_pdf(self):
        "Преобразовать Word (docx) в PDF"
        pass

    def compress_images(self):
        "Произвести сжатие изображений"
        pass

    def delete_files(self):
        "Удалить группу файлов"
        pass
