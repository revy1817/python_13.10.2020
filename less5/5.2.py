with open("5.2_TextFile.txt", "r", encoding="UTF-8") as text_file:
    lines = 0
    for line in text_file:
        lines += 1
        print(f"В строке под номером {lines} слов - {len(line.split())}")
print(f"В текстовом файле {lines} - строк")
