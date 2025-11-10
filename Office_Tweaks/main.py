import argparse
from console_interface import ConsoleInterface


def main():
    parser = argparse.ArgumentParser(
        description="Утилита для работы с офисными файлами: конвертация PDF/DOCX, сжатие изображений, удаление файлов",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:

Конвертация PDF в DOCX:
  python main.py --pdf2docx "C:\\path\\to\\file.pdf"
  python main.py --pdf2docx all --workdir "C:\\path\\to\\folder"

Конвертация DOCX в PDF:
  python main.py --docx2pdf "C:\\path\\to\\file.docx"
  python main.py --docx2pdf all --workdir "C:\\path\\to\\folder"

Сжатие изображений:
  python main.py --compress-images "C:\\path\\to\\image.jpg" --quality 80
  python main.py --compress-images all --workdir "C:\\path\\to\\folder" --quality 75

Удаление файлов:
  python main.py --delete --delete-mode startswith --delete-pattern "temp_" --delete-dir "C:\\path\\to\\folder"
  python main.py --delete --delete-mode extension --delete-pattern "tmp" --delete-dir "C:\\path\\to\\folder"
  python main.py --delete --delete-mode contains --delete-pattern "old" --delete-dir "C:\\path\\to\\folder"
  python main.py --delete --delete-mode endswith --delete-pattern ".bak" --delete-dir "C:\\path\\to\\folder"

Интерактивный режим:
  python main.py
  python main.py --interactive
  python main.py -i
        """,
    )

    # Конвертация PDF в DOCX
    parser.add_argument(
        "--pdf2docx",
        help='Преобразовать PDF в Word (docx). Укажите путь к файлу или "all" для всех файлов в папке',
    )

    # Конвертация DOCX в PDF
    parser.add_argument(
        "--docx2pdf",
        help='Преобразовать Word (docx) в PDF. Укажите путь к файлу или "all" для всех файлов в папке',
    )

    # Сжатие изображений
    parser.add_argument(
        "--compress-images",
        help='Сжать изображение. Укажите путь к файлу или "all" для всех изображений в папке',
    )

    # Качество сжатия изображений
    parser.add_argument(
        "--quality",
        type=int,
        default=75,
        choices=range(1, 101),
        metavar="[1-100]",
        help="Степень сжатия изображений от 1 до 100 (по умолчанию: 75)",
    )

    # Рабочая папка (используется только при обработке всех файлов)
    parser.add_argument(
        "--workdir",
        help="Указание рабочей папки (используется только при обработке всех файлов с 'all')",
    )

    # Удаление файлов
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Удалить файлы из указанной папки",
    )

    parser.add_argument(
        "--delete-mode",
        choices=["startswith", "endswith", "contains", "extension"],
        help="Режим удаления файлов",
    )

    parser.add_argument(
        "--delete-pattern",
        help="Подстрока/расширение для удаления файлов",
    )

    parser.add_argument(
        "--delete-dir",
        help="Папка для удаления файлов",
    )

    # Интерактивный режим
    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Запуск в интерактивном режиме (по умолчанию, если не указаны другие аргументы)",
    )

    args = parser.parse_args()

    interface = ConsoleInterface()

    # Проверка наличия аргументов командной строки
    has_args = any(
        [
            args.pdf2docx,
            args.docx2pdf,
            args.compress_images,
            args.delete,
            args.interactive,
        ]
    )

    # Обработка конвертации PDF в DOCX
    if args.pdf2docx:
        if args.pdf2docx.lower() == "all":
            if not args.workdir:
                parser.error("Для обработки всех файлов требуется указать --workdir")
            interface.convert_pdf_to_word(all_files=True, workdir=args.workdir)
        else:
            if args.workdir:
                print(
                    "Предупреждение: --workdir игнорируется при обработке одного файла"
                )
            interface.convert_pdf_to_word(file_path=args.pdf2docx)
        return

    # Обработка конвертации DOCX в PDF
    if args.docx2pdf:
        if args.docx2pdf.lower() == "all":
            if not args.workdir:
                parser.error("Для обработки всех файлов требуется указать --workdir")
            interface.convert_word_to_pdf(all_files=True, workdir=args.workdir)
        else:
            if args.workdir:
                print(
                    "Предупреждение: --workdir игнорируется при обработке одного файла"
                )
            interface.convert_word_to_pdf(file_path=args.docx2pdf)
        return

    # Обработка сжатия изображений
    if args.compress_images:
        if args.compress_images.lower() == "all":
            if not args.workdir:
                parser.error("Для обработки всех файлов требуется указать --workdir")
            interface.compress_images(
                all_files=True, quality=args.quality, workdir=args.workdir
            )
        else:
            if args.workdir:
                print(
                    "Предупреждение: --workdir игнорируется при обработке одного файла"
                )
            interface.compress_images(
                file_path=args.compress_images, quality=args.quality
            )
        return

    # Обработка удаления файлов
    if args.delete:
        if not args.delete_mode:
            parser.error("Для --delete требуется указать --delete-mode")
        if not args.delete_dir:
            parser.error("Для --delete требуется указать --delete-dir")

        mode_map = {
            "startswith": 1,
            "endswith": 2,
            "contains": 3,
            "extension": 4,
        }

        if not args.delete_pattern:
            parser.error(
                f"Для режима '{args.delete_mode}' требуется указать --delete-pattern"
            )

        interface.delete_files(
            mode=mode_map[args.delete_mode],
            pattern=args.delete_pattern,
            workdir=args.delete_dir,
        )
        return

    # Если аргументы не переданы или указан интерактивный режим, запускаем интерактивный режим
    if not has_args or args.interactive:
        interface.run()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
