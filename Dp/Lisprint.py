def lis(arr):
    n = len(arr)

    dp = [1 for i in range(n)]
    h = [i for i in range(n)]
    maxI = 0
    lastIndex = 0

    for i in range(n):
        for j in range(0,i):
            if arr[i]>arr[j] and dp[i]<1+dp[j]:
                dp[i] = 1+dp[j]
                h[i] = j
        # print(dp)
        if dp[i]>maxI:
            maxI = dp[i]
            lastIndex = i
    
    print(dp, lastIndex, h)

    output = []
    while lastIndex!=h[lastIndex]:
        
        output.append(arr[lastIndex])
        lastIndex = h[lastIndex]
    
    output.append(arr[lastIndex])
        
    
    print(output[::-1])


if __name__=="__main__":
    arr = [5,4,11,1,16,8]
    lis(arr)