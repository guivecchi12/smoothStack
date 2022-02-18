import log
import file_manipulation

def month_year(file):
    try:
        date = file.split("expedia_report_monthly_",1)[1].split('_')
        year = date[1].split('.')[0]
        month = date[0].capitalize()
        try:
            int(year)
            if(not year or len(year) != 4 or int(year) < 0):
                log.log("date inputed incorrectly")
                return -1
            else:
                log.log("Date asked for {}".format(month))
                num_month = month_to_num(month)
                if num_month == -1:
                    return -1
                else:
                    return[year, num_month, month]

        except:
            log.log("File year was inputed incorrectly")

    except:
        log.log("Error while looking for data date")


def month_to_num(month):
    if(month == 'January'):
        month_num = 1
    elif(month == 'Febuary'):
        month_num = 2
    elif(month == 'March'):
        month_num = 3
    elif(month == 'April'):
        month_num = 4
    elif(month == 'May'):
        month_num = 5
    elif(month == 'June'):
        month_num = 6
    elif(month == 'July'):
        month_num = 7
    elif(month == 'August'):
        month_num = 8
    elif(month == 'September'):
        month_num = 9
    elif(month == 'October'):
        month_num = 10
    elif(month == 'November'):
        month_num = 11
    elif(month == 'December'):
        month_num = 12
    else:
        log.log("Month was not provided correctly on the file")
        return -1
    return month_num