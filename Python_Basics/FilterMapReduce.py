import functools

list1 = [1,0,2,1,2,0]

#Filter function just filters the items from the iterable which matches the expression expectations
print("Filter result\t:", list(filter(lambda x:x>=1,list1)))

# Map function operates on every item in the iterable to modify every item
print("Map result\t:", list(map(lambda x:x**2,filter(lambda x:x>=1,list1))))
# result = list(map(lambda x:x**2,filter(lambda x:x == 2,list1)))

# Reduce function does mathematical operation to give single value by performing same operation till the iterable is iterated fully
result = functools.reduce(lambda x,y: x+y,map(lambda x:x**2,filter(lambda x:x>=1,list1)))
print("Reduce result\t: ",result)


# OUTPUT
'''
Filter result   : [1, 2, 1, 2]
Map result      : [1, 4, 1, 4]
Reduce result   :  10
'''
