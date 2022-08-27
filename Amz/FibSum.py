def sumFibOptimized(n, fibArr):
    # O(1) solution given a fibonacci series array as input
    return fibArr[n+2]-1


def sumFib(n):
    # O(n) approach
    arr = [0]*(n+1)

    arr[0], arr[1] = 0,1

    for i in range(2, n+1):
        arr[i] = arr[i-1]+arr[i-2]
    
    return sum(arr)


if __name__ == "__main__":
    s = sumFib(4)
    print(s)
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    print(sumFibOptimized(4, arr))