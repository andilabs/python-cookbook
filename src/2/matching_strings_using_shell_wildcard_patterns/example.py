# example.py
#
# Example of using shell-wildcard style matching in list comprehensions

from fnmatch import fnmatchcase as match

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

a = [addr for addr in addresses if match(addr, '* ST')]
print(a)

b = [addr for addr in addresses if match(addr, '54[0-9][0-9] *CLARK*')]
print(b)

#nice!


# >>> import fnmatch
# >>> addresses = [
# ...     '5412 N CLARK ST',
# ...     '1060 W ADDISON ST',
# ...     '1039 W GRANVILLE AVE',
# ...     '2122 N CLARK ST',
# ...     '4802 N BROADWAY',
# ... ]

# >>> [ad for ad in addresses if fnmatch.fnmatchcase(ad, '[0-9]0[0-9][0-9] *')]
# ['1060 W ADDISON ST', '1039 W GRANVILLE AVE']
