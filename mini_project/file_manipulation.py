import os
import log
import openpyxl
import datetime
import shutil

def find_file():
    try:
        path_array = []
        for file in os.listdir('./mini_project/import'):
            if file.startswith("expedia_report_monthly_"):
                path = './mini_project/import/' + file
                log.log("File loaded successfully")
                path_array.append(path)
                src_folder = "/mini_project/file.lst//"
                if os.path.exists(src_folder):
                    shutil.move(path, src_folder)
            else:
                error_file_path = './mini_project/import/' + file
                src_folder = "./mini_project/error_files//"
                if os.path.exists(src_folder):
                    shutil.move(error_file_path, src_folder)

        if len(path_array) > 0:
            return path_array
    except:
        return log.log("Error while loading file")

def read_file(file):
    try:
        if not file:
            log.log("No file found, using the naming convention expedia_report_monthly_MONTH_YEAR.xlsx")
        else:
            try:
                wb = openpyxl.load_workbook(file)
                return wb
            except:
                log.log("Data was not able to load")
    except:
        log.log("Error while reading File")


def find_row(ws, search):
    for x in range(1, ws.max_column + 1):
        for y in range(1, ws.max_row + 1):
            current_cell = ws.cell(row = y, column = x).value
            if isinstance(current_cell, str):
                if search in current_cell:
                    return y
            elif isinstance(current_cell, datetime.date):
                if current_cell.year == search.year and current_cell.month == search.month:
                    return y
    log.log("No row found matching the date/field information")

def find_column(ws, name):
    for x in range(1, ws.max_column + 1):
        for y in range(1, ws.max_row + 1):
            if ws.cell(row = y, column = x).value == name:
                return x
    log.log("No Column found matching the date/field information")
                
def capture_data(ws, my_row):
    calls = ws.cell(row = my_row, column = find_column(ws, 'Calls Offered')).value
    abandon = ws.cell(row = my_row, column = find_column(ws, ' Abandon after 30s')).value
    fcr = ws.cell(row = my_row, column = find_column(ws, 'FCR')).value
    dsat = ws.cell(row = my_row, column = find_column(ws, 'DSAT ')).value
    csat = ws.cell(row = my_row, column = find_column(ws, 'CSAT ')).value

    data = {
       'Calls Offered': calls,
       'Abandon after 30s': "{:.2%}".format(abandon),
       'FCR': "{:.2%}".format(fcr),
       'DSAT': "{:.2%}".format(dsat),
       'CSAT': "{:.2%}".format(csat)
    }
    return data

def get_data(file, date):
    if(date == -1):
        log.log("File naming incorrect")
    else:
        log.log("Date of Data extracted correctly")
        wb = read_file(file)
        data_date = datetime.datetime(int(date[0]), date[1], 1)
        ws = wb.active
        my_row = find_row(ws, data_date)
        data = capture_data(ws, my_row)
        
        data_month = '' + date[2]
        log.log("Data for {}: \n {}".format(data_month, data))
        return data

def get_data_from_sheet(file, sheet, date):
    if(date == -1):
        log.log("File naming incorrect")
    else:
        log.log("Date of Data extracted correctly")
        data_date = datetime.datetime(int(date[0]), date[1], 1)
        wb = read_file(file)
        ws2 = wb[sheet]
        my_col = find_column(ws2, data_date)
    
        # Check Promoters
        my_row = find_row(ws2, 'Promoters')
        promoters = check_score('Promoters', ws2.cell(row = my_row, column = my_col).value)

        # Check Passives
        my_row = find_row(ws2, 'Passives')
        passives = check_score('Passives', ws2.cell(row = my_row, column = my_col).value)
        
        # Check Decractors
        my_row = find_row(ws2, 'Dectractors')
        dectractors = check_score('Dectractors', ws2.cell(row = my_row, column = my_col).value)
        # log.log("In Net Promoters Score: \n\tPromoters: {} \n\tPassives: {} \n\tDectractors: {}".format(promoters, passives, dectractors))


def check_score(category, value):
    print("category {} \n value {}".format(category, value))
    # if category == 'Promoters':
    #     if value > 200:
    #         return 'good'
    #     else:
    #         return 'bad'
    # elif category == 'Passives':
    #     if value > 100:
    #         return 'good'
    #     else:
    #         return 'bad'
    # elif category == 'Dectractors':
    #     if value > 100:
    #         return 'good'
    #     else:
    #         return 'bad'
    # else:
    #     log.log("Could not find the field {}".format(category))

# get_data_from_sheet('./mini_project/import/expedia_report_monthly_january_2018.xlsx', 'VOC Rolling MoM', ['2018', 1, 'January'])
# wb = read_file('./mini_project/import/expedia_report_monthly_january_2018.xlsx')
# ws = wb.active
# date = ['2018', 1, 'January']
# data_date = datetime.datetime(int(date[0]), date[1], 1)
# find_row(ws, data_date)