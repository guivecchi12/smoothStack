import os
import log
import openpyxl
import datetime

def find_file():
    try:
        path_array = []
        for file in os.listdir('./mini_project'):
            if file.startswith("expedia_report_monthly_"):
                path = './mini_project/' + file
                log.log("File loaded successfully")
                path_array.append(path)
        if len(path_array) > 0:
            return path_array
    except:
        return log.log("Error while loading file")

def read_file(file, date):
    try:
        if not file:
            log.log("No file found, using the naming convention expedia_report_monthly_MONTH_YEAR.xlsx")
        else:
            if(date == -1):
                log.log("File naming incorrect")
            else:
                log.log("Date of Data extracted correctly")
                data_date = datetime.datetime(int(date[0]), date[1], 1)
                try:
                    wb = openpyxl.load_workbook(file)
                    ws = wb.active
                    my_row = find_row(ws, data_date)
                    data = capture_data(ws, my_row)
                    
                    data_month = '' + date[2]
                    log.log("Data for {}: \n {}".format(data_month, data))

                    return data
                except:
                    log.log("Data was not able to load")
    except:
        log.log("Error while reading File")

def find_row(ws, date):
    for col in ws.iter_cols(min_row=0, max_row=ws.max_row + 1):
        for cell in col:
            if isinstance(cell.value, datetime.date) and cell.value.year == date.year and cell.value.month == date.month:
                log.log("Column and Row of data found")
                return cell.row
                
def capture_data(ws, my_row):
    calls = ws.cell(row = my_row, column = find_column(ws, 'Calls Offered')).value
    abandon = ws.cell(row = my_row, column = find_column(ws, ' Abandon after 30s')).value
    fcr = ws.cell(row = my_row, column = find_column(ws, 'FCR')).value
    dsat = ws.cell(row = my_row, column = find_column(ws, 'DSAT ')).value
    csat = ws.cell(row = my_row, column = find_column(ws, 'CSAT ')).value

    data = {
       'Calls Offered': calls,
       'Abandon after 30s': abandon,
       'FCR': fcr,
       'DSAT': dsat,
       'CSAT': csat
    }
    return data

def find_column(ws, name):
    for x in range(1, ws.max_column + 1):
        for y in range(1, ws.max_row + 1):
            if ws.cell(row = y, column = x).value == name:
                return x
