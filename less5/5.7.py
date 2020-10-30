import json
company_result = {}
total_profit_dict = {}
with open("5.7_CompanyInfo.txt", "r", encoding="UTF-8") as company_info:
    lines = company_info.readlines()
    quantity = 0
    total_profit = 0
    for line in lines:
        line_split = line.split()
        key = line_split[0]
        quantity += 1
        profit_company = int(line_split[2]) - int(line_split[3][:-1])
        if profit_company > 0:
            total_profit += profit_company
        company_result[key] = profit_company
    total_profit_dict["average_profit"] = total_profit / quantity
company_info_dict = [company_result, total_profit_dict]
with open("5.7_CompanyInfo.json", "w") as new_file_json:
    json.dump(company_info_dict, new_file_json)
