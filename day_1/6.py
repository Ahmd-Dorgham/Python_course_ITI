depth = int(input("pyramid depth: "))
for r in range(1, depth + 1):
    print("*" * r)
for r in range(depth - 1, 0, -1):
    print("*" * r)