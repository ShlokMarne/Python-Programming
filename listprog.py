mylist = []
for i in range (10):
    s1 = input("Enter string: ")
    mylist.append(s1)

oddcount = 0
evencount = 0
for x in mylist:
    x = len(x)
    if x % 2 == 0:
        evencount = evencount + 1
    else:
        oddcount = oddcount + 1
print("Even no.in list: " + str(evencount))
print("Odd no.in list: " + str(oddcount)) 