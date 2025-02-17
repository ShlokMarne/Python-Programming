s1 = input("Enter a string: ")
flag = 0
i = 0
j = len(s1) - 1
while i < j:
    if (s1[i] != s1[j]):
        flag = 1
        print(s1 + " not palindrom")
        break
    i = i + 1
    j = j - 1

if flag == 0:
    print("Palindrom")