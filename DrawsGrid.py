def draws_grid():
    # This function draws a grid when is called.
    symbol_one = '+'
    symbol_two = '-' * 4
    symbol_three = '|'

    for i in range(12):

        if i == 0 or i == 5 or i == 10:

            print(symbol_one, symbol_two, symbol_one, symbol_two, symbol_one)

        elif i in [1, 2, 3, 4, 6, 7, 8, 9]:

            # elif not (i==0 or i==5 or i==10):
            print(symbol_three, ' ' * 4, symbol_three, ' ' * 4, symbol_three)


if __name__ == '__main__':
    draws_grid()
