n = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())

def toh(n, n1, n2, n3):
    if(n==0):
        return
    toh(n-1, n1, n3, n2)
    print(n, "[", n1," -> ",n2, "]")
    toh(n-1, n3, n2, n1)


toh(n, n1, n2, n3)