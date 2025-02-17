list1 = input("Enter integers: ")
ch = 0
while ch <= 4:
    print(" MENU ")
    print(" 1.Length ")
    print(" 2.Sum ")
    print(" 3.Average ")
    print(" 4.Multiplication ")
    print(" 5.Exit ")
    ch = int(input(' Enter your choice: '))
    if ch == 1:
        print(f"Length of list:  {len(list1)}")
    elif ch == 2:
        sum = 0
        for x in list1:
            sum = sum + x
        print("Sum of list: " + str(sum))
    elif ch == 3:
        avg = 0
        sum = 0
        for x in list1:
            sum = sum + x
            avg = sum / len(list1)
        print("Average is: " + str(avg))
    elif ch == 4:
        mul = 1
        for x in list1:
            mul = mul * x
        print("Multiplication of list is: " + str(mul))
    else:
        print("Exit")