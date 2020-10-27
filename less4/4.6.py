import itertools
import sys

user_start_number, user_max_number, user_text, user_text_repeat = sys.argv
try:
    user_start_number = int(user_start_number)
    user_max_number = int(user_max_number)
except ValueError:
    print("Вы ввели не число!")

for el in itertools.count(user_start_number):
    if el > user_max_number:
        break
    else:
        print(el)

try:
    user_text_repeat = int(user_text_repeat)
except ValueError:
    print("Вы ввели не число!")

count = 0
for itm in itertools.cycle(user_text):
    if count > user_text_repeat:
        break
    else:
        print(itm)
        count += 1
