# Lecture about map, filter and reduce
#########################################
# map() maps the functions on every entry on the list
# filter() filters the values accounding to a certain truthness of a function
# reduce() is a function that reduces the values by following a sequence and returns a single value


def cube(x):
    return x * x * x

lst = [1, 2, 3, 4, 5, 6, 7, -1, 0 ,-22]

new_lst = list(map(cube, lst))
print(new_lst)

# Filtering certain values according to the TRUE of function
def filter_function(a):
    return a>0

filtered_new_lst = list(filter(filter_function, lst))
print(filtered_new_lst)

# We can also plug lambda functions in it
a_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mapping = list(map(lambda x: x*x, a_list))
filtering = list(filter(lambda x: x>=0, a_list))
print(mapping)
print(filtering)

# reduce() is imported from functool module
from functools import reduce
# reduce is a function that reduces the values by following a sequence and returns a single value
numbers_x = [1, 2, 3, 4, 5]
sum = reduce(lambda x,y: x+y, numbers_x)
print(sum)
