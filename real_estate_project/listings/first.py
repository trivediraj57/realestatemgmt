from socket import ntohl



n = 5

def fact(n):
    if n == 0:
        return 1
    else:
        for i in range(n):
            return n * fact(n-1)


print(fact(n))