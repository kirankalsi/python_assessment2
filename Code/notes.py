def eight(input,  a):
    length = len(input)
    nums_away = (a - 1) / 2
    middle = (length // 2) + 1
    start = middle - nums_away
    string_list = list(input)
    for i in range(a):
        string_list.pop(int(start) - 1)
    return "".join(string_list)


print(eight("Hello", 3))
print(eight("Chocolate", 3))
print(eight("Chocolate", 1))
#print(nine("tripping", "gin"))