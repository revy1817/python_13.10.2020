product_number = int(input("Укажите количество товара(число) которого хотите добавить \n"))
product = []
min_product = 1
while min_product <= product_number:
    product.append(
        (min_product,
         {"Название": input("Введите наименование товара \n"),
          "Цена": int(input("Введите цену на товар \n")),
          "Количество": int(input("Укажите количество(число) \n")),
          "ед.": (input("Укажите еденицу измерения \n"))}))
    min_product += 1
name_list = []
price_list = []
number_list = []
unit_list = []

min_s = 0
while min_s < product_number:
    name_list.append(product[min_s][1].get("Название"))
    price_list.append(product[min_s][1].get("Цена"))
    number_list.append(product[min_s][1].get("Количество"))
    unit_list.append(product[min_s][1].get("ед."))
    min_s += 1
analysis_dict = {"Название": name_list, "Цена": price_list, "Количество": number_list, "Еденица измерения": list(set
    (unit_list))}
print(analysis_dict)
