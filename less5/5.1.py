user_file = open("user_text.txt", "a")
while True:
    user_text = input("Введите текст, для добавленния в файл, для выхода нажмите Enter \n")
    if user_text != "":
        user_file.write(user_text + "\n")
    else:
        user_file.close()
        break
