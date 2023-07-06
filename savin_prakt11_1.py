def my_factor(n):
    rez=1
    for i in range(n):
        rez=rez*(i+1)
    return rez

print("Введите натуральное число")
my_list=[]

for j in range(my_factor(int(input())),0,-1):
    my_list.append(my_factor(j))

print(my_list)
