name = str(input("Enter any value or character/s: "))
size = len(name)
i = -1

while i < size -1:
    i = i + 1
    if not name[i].isdecimal():
        continue
    print(name[i], end='')
