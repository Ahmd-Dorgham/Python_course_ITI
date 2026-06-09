a = 1
b = 1
while a < 50:
    print(a)
    temp = a
    a = b
    b = temp + b
