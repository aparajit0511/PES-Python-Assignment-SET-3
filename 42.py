def fibonaci(num):

    a = 0
    b = 1
    c = 0

    for _ in range(2,num):
        c = a + b
        b = a
        a = c

    return c



print(fibonaci(int(input())))