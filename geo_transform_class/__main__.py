from .consol_interface import ConsoleInterface


def main():
    """Главная функция для запуска консольного интерфейса."""
    interface = ConsoleInterface()
    interface.run()


if __name__ == "__main__":
    main()
