def split_half(s):
    half = (len(s) + 1) // 2
    return s[:half], s[half:]

f1, b1 = split_half("abcd")
f2, b2 = split_half("xyz")
print(f1)
print(b1)
print(f2)
print(b2)
print("Result:", f1 + f2 + b1 + b2)