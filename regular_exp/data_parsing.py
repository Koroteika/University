import re
import requests
import csv

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
html = requests.get(url).text

pattern = r'org-widget-header__title-link[^>]*>(?P<name>[^<]+)</a>.*?org-widget-header__meta--location">\s*(?P<address>[^<]+?)\s*</span>.*?<dt[^>]*>.*?Телефон.*?</dt>\s*<dd[^>]*>(?P<phone>[^<]+?)</dd>.*?<dt[^>]*>.*?Часы\s+работы.*?</dt>\s*<dd[^>]*>(?P<hours>[^<]+?)</dd>'

matches = re.finditer(pattern, html, re.DOTALL)

result = []
for match in matches:
    result.append(
        [
            match.group("name").strip(),
            match.group("address").strip(),
            match.group("phone").strip(),
            match.group("hours").strip(),
        ]
    )

print(result)

# Записываем в CSV
csv_filename = "parsing_data.csv"
with open(csv_filename, "w", newline="", encoding="windows-1251") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(["Название", "Адрес", "Телефон", "Часы работы"])
    writer.writerows(result)

print(f"Данные сохранены в файл: {csv_filename}")
