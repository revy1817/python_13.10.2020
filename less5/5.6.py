dict_curses = {}
with open("5.6_InfoFile.txt", "r", encoding="UTF-8") as info_file:
    lines = info_file.readlines()
    for line in lines:
        line_split = line.split()
        hours = 0
        key = line_split[0][:-1]
        for el in line_split[1:]:
            el_split = el.split("(")
            try:
                hours += int(el_split[0])
            except ValueError:
                pass
        dict_curses[key] = hours
print(dict_curses)
