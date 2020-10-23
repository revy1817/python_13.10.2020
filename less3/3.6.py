def int_function(word):
    words = ""
    cap = word.split()
    for i in range(len(cap)):
        words += (cap[i] + " ").capitalize()
    return words


rus_text_check = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                  "у",
                  "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}

while True:
    user_word = input("Введите слова на латинском языке \n").lower()
    if set(user_word).isdisjoint(rus_text_check) is False:
        break
    else:
        print("Вы ввели слова не на латинском языке, попробуйте еще раз")
print(int_function(user_word))
