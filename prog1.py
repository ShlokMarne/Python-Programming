mylist = []
for i in range(10):
    s1 = input('Enter one string: ')
    mylist.append(s1)

s2 = input('Enter string to be searched: ')
if s2 in mylist:
    print(s2 + ' Found in list')
else:
    print(s2 + ' not found in list')