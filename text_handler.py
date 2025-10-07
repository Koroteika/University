def write_file(resutl):
    try:
        with open("result.txt", "w") as file:
            file.write(resutl + "\n")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


def read_file(path):
    try:
        with open(path.replace("//", "/"), mode="r", encoding="utf-8") as file:
            content = file.readlines()
            print(content)
    except FileNotFoundError:
        print(f"Файл по пути {path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return None


if __name__ == "__main__":
    write_file("Hello, World!")
    read_file("result.txt")
