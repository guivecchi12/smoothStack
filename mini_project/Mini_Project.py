import file_manipulation
import date_manipulation

def main():
    files = file_manipulation.find_file()
    data = []
    for f in files:
        date = date_manipulation.month_year(f)
        data.append(file_manipulation.read_file(f, date))
if __name__ == '__main__':
    main()