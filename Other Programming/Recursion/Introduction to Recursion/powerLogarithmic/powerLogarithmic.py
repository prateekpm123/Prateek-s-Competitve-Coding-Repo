# x = int(input())
# n = int(input())
x = 2
n = 5

def powerLogarithmic(x, n):
    n = int(n)
    if(n==0):
        return 1

    if( n <1):
        return 1

    ans = powerLogarithmic(x, n/2)
    print(n)
    print(type(n))
    total = ans * ans

    if(n %2 ==1 ):
        total = total*x

    return total

final=powerLogarithmic(x, n)
print(final)