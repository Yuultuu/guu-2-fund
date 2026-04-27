import random
import timeit

def sum_list(list):
    list_sum = 0
    for i in range(0, 10, 2):
        list_sum = list[i] + list[i+1] + list_sum
    return list_sum

def prodlist(list):
    m = list[0]
    for i in list:
        if i == 0:
            break
        else:
            m = m * i
    return m

def filter(list, x):
    greater = [n for n in list if n > x]
    less = [n for n in list if n < x]
    return greater, less

x = 5
list = [random.randint(0, 10) for _ in range(10)]
list.sort()

greater, less = filter(list, x)

print(list,"\n",list[0],"\n",list[-1],"\n",sum_list(list),"\n",prodlist(list),"\n",greater,"\n",less)