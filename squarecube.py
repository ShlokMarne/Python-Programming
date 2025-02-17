list = [1,2,3,4,5,6,7,8,9,10]
squared_list = []
cubed_list = []
for x in list:
        squared_list.append(x ** 2)
        cubed_list.append(x ** 3)

print("Original list:", list)
print("Squared list:", squared_list)
print("Cubed list:", cubed_list)