words = []
with open("5.4_TextFile.txt", "r", encoding="UTF-8") as text_file:
    for line in text_file:
        word = line.split()
        trash_word = word[0]
        word.remove(trash_word)
        words.append(word)

with open("5.4_NewFile.txt", 'w', encoding="UTF-8") as new_file:
    russian_words = [["Один", *words[0]], ["Два", *words[1]], ["Три", *words[2]], ["Четыре", *words[3]]]
    for el in range(len(russian_words)):
        new_file.write(f"{russian_words[el][0]} {russian_words[el][1]} {russian_words[el][2]} \n")
