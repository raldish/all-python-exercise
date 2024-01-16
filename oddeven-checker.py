print("Odd/Even checker")
while True:

    num = float(input("Please provide a whole number! :>  "))
    a = int(num)
    if a != 0:
        b = a % 2

        if (b % 2) == 0:
            print("even")
        else:
            print("odd" )

    else:

        print("Thanks! Bye!")
        break
