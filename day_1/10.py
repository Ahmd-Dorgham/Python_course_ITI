text = input("Write something: ")
l = 0
d = 0
for c in text:
    if c.isalpha():
        l = l + 1
    elif c.isdigit():
        d = d + 1
print("Letters: " + str(l))
print("Digits: " + str(d))