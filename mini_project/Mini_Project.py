import file_manipulation
import date_manipulation

def main():
    files = file_manipulation.find_file()


    for f in files:
        date = date_manipulation.month_year(f)
        if date and date != -1:
            data = file_manipulation.get_data(f, date)
            if data != -1:
                file_manipulation.get_data_from_sheet(f, 'VOC Rolling MoM', date)
    

if __name__ == '__main__':
    main()