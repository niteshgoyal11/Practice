from functools import reduce

lis = [1,2,3,4,5]
print(list(map(lambda x:x*x, lis)))
print(list(filter(lambda x:x %2 == 0, lis)))
print (reduce(lambda x,y: x + y, lis))
