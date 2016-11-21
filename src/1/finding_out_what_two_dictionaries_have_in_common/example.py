# example.py
#
# Find out what two dictionaries have in common

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

print('Common keys:', a.keys() & b.keys())
print('Keys in a not in b:', a.keys() - b.keys())
print('(key,value) pairs in common:', a.items() & b.items())

# Note Python3:
# >>> type(b.keys())
# <class 'dict_keys'>



# while in Python 2.7:
#>>> type(b.keys())
#<type 'list'>

# 4.10.1. Dictionary view objects
# The objects returned by dict.keys(), dict.values() and dict.items() are view objects. 
# They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, 
# the view reflects these changes.
# Dictionary views can be iterated over to yield their respective data, and support membership tests
# https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
