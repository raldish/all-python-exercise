num = int(input("Enter number: "))
while num > 0:
    if num % 2 == 0:
        print(num, "is even number")
        num = int(input("Enter number: "))
    else:
        print(num, "is odd number")
        num = int(input("Enter number: "))
    if num == 0:
        break
