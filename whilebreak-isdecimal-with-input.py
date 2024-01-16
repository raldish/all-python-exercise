name = str(input("Enter any value or character/s: "))
size = len(name)
i = 0

while i < size:
    if name[i].isdecimal():
        break;
    print(name[i], end='')
    i = i + 1
