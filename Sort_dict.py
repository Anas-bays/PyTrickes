# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sort = sorted(xs.items(), key=lambda x: x[1])

print(sort)

'''
OutPut:
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
'''

# Or:

# pip install operator
import operator

sort = sorted(xs.items(), key=operator.itemgetter(1))

print(sort)

'''
Output:
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
'''

