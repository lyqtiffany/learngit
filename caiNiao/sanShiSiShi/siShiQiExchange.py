def exchange(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x = 12
    y = 65
    x, y = exchange(x, y)
    print('x value is %d'%x, 'y value change to %d'%y)