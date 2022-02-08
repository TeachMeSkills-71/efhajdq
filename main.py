def rec(x):
    a = int(input('ведите число'))
    flag = True
    b = 2
    while b * b <= a:
        if a % b == 0:
            flag = False
            break
    if flag:
        print(f'{a} - число простое ')
    else:
        print(f'{a} - составное число')
    print(x)
    rec(x)
rec(1)

