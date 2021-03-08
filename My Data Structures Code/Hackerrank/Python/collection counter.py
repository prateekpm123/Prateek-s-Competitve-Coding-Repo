# https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import functools as fnct

noOfShoes = int(input())

# here split takes values from the input as string and converts them into 
# list of string, now that list acts as parameter for map and int acts as a typecasting function
# then we get a object of a map, in order to make in into a list we typecast it with list
shoeSizes = list(map(int, input().split()))

noOfCustomer = int(input())
allCustomerRequirement = []
for i in range(noOfCustomer):
    customerRequirement = list(map(int,input().split()))
    allCustomerRequirement.append(customerRequirement)

# print(shoeSizes)
# print(allCustomerRequirement)
salesMade = []
for i in range(noOfCustomer):
    shoeSize = allCustomerRequirement[i][0]
    shoeMoney = allCustomerRequirement[i][1]
    if(shoeSize in shoeSizes):
        foundShoeSizeAtIndex = shoeSizes.index(shoeSize)
        salesMade.append(shoeMoney)
        shoeSizes.pop(foundShoeSizeAtIndex)
    
# print(salesMade)
if(len(salesMade) != 0):
    sumSales = fnct.reduce(lambda a,b:a+b, salesMade)
    print(sumSales)
else:
    print(0)
