name = str(input("Enter character or value: "))
size = len(name)
i = -1
while i < size - 1:
    i += 1
    if not name[i].isalpha():
        continue
    print(name[i], end="")
