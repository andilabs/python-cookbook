"""
Make an iterator that returns consecutive keys and groups from the iterable. 
The key is a function computing a key value for each element. 
If not specified or is None, key defaults to an identity function and returns the element unchanged. 
Generally, the iterable needs to already be sorted on the same key function.

!!!!!!!!!!!!!!!!!!!!!!!!!! FUCKING IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:

The operation of groupby() is similar to the uniq filter in Unix. 
It generates a break or new group every time the value of the key function changes
(which is why it is usually necessary to have sorted the data using the same key function). 
That behavior differs from SQL’s GROUP BY which aggregates common elements regardless of their input order.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

The returned group is itself an iterator that shares the underlying iterable with groupby(). 
Because the source is shared, when the groupby() object is advanced, the previous group is no longer visible. 
So, if that data is needed later, it should be stored as a list:
"""

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from itertools import groupby
# https://docs.python.org/3/library/itertools.html#itertools.groupby


rows.sort(key=lambda r: r['date'])
for date, items in groupby(rows, key=lambda r: r['date']):
    print(date)
    for i in items:
        print('    ', i)

# Example of building a multidict
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)


    



