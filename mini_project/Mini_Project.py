import file_manipulation
import date_manipulation

def main():
    files = file_manipulation.find_file()
    data = []
    for f in files:
        date = date_manipulation.month_year(f)
        data.append(file_manipulation.get_data(f, date))

    # Part 2
    data_from_sheet = []
    for f in files:
        date = date_manipulation.month_year(f)
        data_from_sheet.append(file_manipulation.get_data_from_sheet(f, 'VOC Rolling MoM', date))
    print(data_from_sheet)
    

if __name__ == '__main__':
    main()