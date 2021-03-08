# num = int(input())
num = 5
val = 0
def factorial(num):
    if(num==0):
        return 1
    val = num* factorial(num-1)
    return val

factIs = factorial(num)
print(factIs)