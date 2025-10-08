def write_file(resutl: str):
    try:
        with open("result.txt", "a", encoding="utf-8") as file:
            file.write(resutl + "\n")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


def read_file(path):
    try:
        with open(path.replace("\\", "/"), "r", encoding="utf-8") as file:
            content = file.readlines()
            content = [[float(num) for num in line.split()] for line in content]
        return content
    except (IOError, ValueError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


if __name__ == "__main__":
    write_file("Hello, World!")
    read_file("result.txt")
