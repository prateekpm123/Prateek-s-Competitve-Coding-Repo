#!/bin/python3
from collections import OrderedDict
# s = input()
s = "bbbaaaccde"
some = OrderedDict()
for i in s:
    some[i] = 0
    # print(s[)
for i in s:
    some[i] += 1
    # print(s[)

count = 0
some = OrderedDict(sorted(some.items(),reverse=True, key=lambda t: t[1]))
# some = OrderedDict(sorted(some.items(), key=lambda t: t[0]))

print(some['a'] )
print(len(some))
for items in some.items():
    if(count<3):
        # print(key, value)
        print()
        count += 1