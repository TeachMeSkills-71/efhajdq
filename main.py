while True:
    a = int(input('insert the number a'))
    b = int(input('insert the number b='))
    print('1 - fold a+b')
    print('2 - subtract a-b')
    print('3 - multiplication a*b')
    print('4 - division a/b')
    operation = int(input('choose an operation'))

    if operation == 1:
        print('soma a+b=', a + b)

    if operation == 2:
        print('difference a-b=', a - b)

    if operation == 3:
        print('sets a*b=', a * b)

    if operation == 4:
        print('del a/b=', a / b)
