#Expedia.com to find excel file with multiple tabs
# www.pypi.org

import openpyxl

def read_file():
    path = "./Day 5/expedia_report_monthly_january_2018.xlsx"

    wb = openpyxl.load_workbook(path)

    ws = wb.active

    cell_obj = ws.cell(row = 1, column = 2)

    print(cell_obj.value)


read_file()