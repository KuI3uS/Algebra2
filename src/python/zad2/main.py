def fibonaci(c):
    if c == 0:
     return 0
    elif c == 1:
     return 1
    b, a = 0, 1
    for i in range(c - 1):
     b, a = a, b + a
    return a
print(fibonaci(70), fibonaci(71), fibonaci(72))