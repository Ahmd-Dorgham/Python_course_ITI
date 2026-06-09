list1 = [1, 2, 3, 4]
list2 = [1, 1, 2, 3, 4, 4, 5, 6, 7]

def check_unique(lst):
    unique_list = []
    for item in lst:
        if item in unique_list:
            return False
        unique_list.append(item)
    return True

print(check_unique(list1))
print(check_unique(list2))