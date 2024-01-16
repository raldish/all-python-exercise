print("Odd/Even checker")
while True:

    num = float(input("Please provide a whole number! :> "))
    dnum = int(num)
    if dnum == 0:
        print("Thanks! Bye!")
        break
    
    if (num % 2) == 0:
        print("even")
    else:
        print("odd")



