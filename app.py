import openpyxl as xl
from openpyxl.chart import BarChart, Reference


def process_workbook(filename):

    wb = xl.load_workbook(filename)
    sheet = wb["Sheet1"]
    col_c = sheet["c"]

    corrected_price_lst = ["corrected_price"]

    for row in col_c:
        if isinstance(row.value, float):
            corrected_price = row.value * 0.9
            corrected_price_lst.append(corrected_price)

    col_d = sheet["d"]

    for value, row in zip(corrected_price_lst, col_d):
        row.value = value

    values = Reference(sheet, min_row=2, max_row=sheet.max_row, min_col=4, max_col=4)

    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, "e2")

    wb.save(filename)


if __name__ == "__main__":
    process_workbook("transactions.xlsx")
