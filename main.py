from retirement_age import *


def main():
    print('\033[1m' + 'Welcome to the SSA Full Retirement Age Calculator' + '\033[0m')
    again = True
    while again:
        again = input('\nEnter 1 to continue or any other key to quit: ')
        if again == '1':
            pass
        else:
            quit()

        month = input('What is the number of your birth month? ')
        while not check_month(month):
            month = input('What is the number of your birth month? ')
        year = input('What is the number of your birth year? ')
        while not check_year(year):
            year = input('What is the number of your birth year? ')

        retire(year, month)


def check_month(num_m):
    try:
        num_m = int(num_m)                    # is the input a number?
        month_range = range(1, 13, 1)   # is the number a value between 1 - 12
        if num_m in month_range:
            return True
        else:
            raise ValueError            # sends us to our exception error below
    except ValueError:
        print('Invalid entry.')
        return False


def check_year(num_y):
    try:
        num_y = int(num_y)                    # is the input a number?
        year_range = range(1900, 2023, 1)   # is the number a value between 1 - 12
        if num_y in year_range:
            return True
        else:
            raise ValueError            # sends us to our exception error below
    except ValueError:
        print('Invalid entry.')
        return False


# I'm reusing my function from my grade calculation homework
def check_num(num_x):   # check each input for correct data type
    try:
        float(num_x)    # this is also friendly to "int"
        return True
    except ValueError:
        print('Incorrect entry. You must enter a number')
        return False


if __name__ == '__main__':
    main()
