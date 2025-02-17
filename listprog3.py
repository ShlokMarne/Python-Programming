mylist = []
ch = 1
while ch <= 3:
    print('Menu ')
    print('1. Add data ')
    print('2. Remove data ')
    print('3. Display data ')
    print('4. Exit ')

    ch = int(input("Enter your choise: "))
    
    if ch == 1:
        s1 = input('Enter data: ')
        mylist.append(s1)
        print('Data added successfully ')
    elif ch == 2:
        if len(mylist) >= 1:
            mylist.pop(-1)
            print('Data removed successfully ')
        else:
            print('No data entered')
    elif ch == 3:
        print(mylist)
    else:
        print('Exit')