# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

num = int(input())

inventory = OrderedDict()
temp = []
for i in range(num):
    item = input().split()
    temp.append(item)
    
# print(temp)
prices = []
items = []
for i in range(num):
    names = ""
    prices.append(int(temp[i][len(temp[i])-1]))
    for j in range(len(temp[i])-1):
        print(i,j)
        names += temp[i][j]
        print(names)
        names += " "
    items.append(names)
    
# print(items, prices)


for i in range(num):
    inventory[items[i]] = 0

for i in range(num):
    inventory[items[i]] += prices[i]

for key, value in inventory.items():
    print(key, end="")
    print(value)

# print(inventory)
