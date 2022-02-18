import file_manipulation
import date_manipulation

def main():
    files = file_manipulation.find_file()
    file_lst = open('./mini_project/file.lst', "x")
    if files:
        for f in files:
            date = date_manipulation.month_year(f)
            if date and date != -1:
                data = file_manipulation.get_data(f, date)
                if data != -1:
                    file_lst.write("Data from Summary Rolling MoM tab read for file: {}\n".format(f))
                    file_manipulation.get_data_from_sheet(f, 'VOC Rolling MoM', date)
                    file_lst.write("Data from VOC Rolling MoM tab read for file: {}\n".format(f))

if __name__ == '__main__':
    main()