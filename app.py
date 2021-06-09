import openpyxl as xl

wb = xl.load_workbook("transactions.xlsx")
sheet = wb["Sheet1"]
col_c = sheet["c"]  # cell = sheet["c1"] will give just a cell,

corrected_price_lst = ["corrected_price"]

for row in col_c:
    if isinstance(row.value, float):
        corrected_price = row.value * 0.9
        corrected_price_lst.append(corrected_price)

print(corrected_price_lst)

col_d = sheet["d"]

for value, row in zip(corrected_price_lst, col_d):
    row.value = value

print("=" * 10)
for row in col_d:
    print(row.value)

wb.save("transactions2.xlsx")
