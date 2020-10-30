with open("5.3_TextFile.txt", "r", encoding="UTF-8") as worker_salary:
    salary = 0
    worker = 0
    for line in worker_salary:
        worker += 1
        words = line.split()
        for el in words:
            try:
                el = float(el)
                if el > 20000:
                    salary += el
                else:
                    salary += el
                    print(f"У сотрудника {words[0]} зарплата менее 15000!!!")
            except ValueError:
                pass
print(f"Средняя зарплата в компании составляет {round(salary/worker)}")
