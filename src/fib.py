fibDict = {
    0 : 1,
    1 : 1
}

def fib(x):
    n = fibDict.get(x)
    if n == None:
        fibDict[x] = fib(x-1) + fib(x-2)
    return fibDict.get(x)