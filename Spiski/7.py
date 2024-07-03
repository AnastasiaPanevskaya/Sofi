#Что покажет этот код?
lst = [5]
lst *= 3
lst[0] = 0
lst[2] = 10

print(sum(lst))