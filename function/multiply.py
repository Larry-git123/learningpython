def multiply():
    while True:
        try:
            n = input('Please input integer 1(input q for exit):')
            if n == 'q':
                break
            n1 = int(n)
            n2 = int(input('Please input integer 2:'))
        except (ValueError, NameError, SyntaxError):
            print('Please input valid integers!')
        else:
            print(n1, '*', n2, '=', n1 * n2)

def product(*numbers):
    r = 1
    for i in numbers:
        r = r * i
    return r