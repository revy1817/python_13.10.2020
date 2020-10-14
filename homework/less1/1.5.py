company_income = int(input("Укажите выручку компании \n"))
company_less = int(input("Укажите издержки компании \n"))
company_profit = 0
if company_income > company_less:
    print("Компания отработала с прибылью!")
    company_profit = company_income - company_less
    print(f"Выручка компании составила {company_profit}")
elif company_income == company_less:
    print("Компания отработала в 0")
else:
    print("Компания отработала в убыток!")

company_workers = int(input("Укажите количество работников \n"))
profit_to_1_workers = company_profit / company_workers
print(f"Компания в среднем заработала с одного сотруника: {profit_to_1_workers}")
