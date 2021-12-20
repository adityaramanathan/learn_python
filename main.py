my_list = [1,2,3,4,5]
print(7 in my_list)
print(2 in my_list)
a = 1
for i in range(1):
    print(my_list[a-1])
b = my_list[a]
my_list[a] = my_list[a+2]
my_list[a+2] = b
print(my_list)