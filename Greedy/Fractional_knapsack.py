def fractional_knapsack(arr, weight, n):

    arr.sort(key = lambda x:x[0]/x[1])
    arr.reverse()
    value = 0
    curr_weight = 0
    for i in range(0,n):
        if curr_weight+arr[i][1]>weight:
            diff = weight-curr_weight
            value += (diff*(arr[i][0]/arr[i][1]))*10
            weight-=diff
        else:
            value += arr[i][0]
            weight -= arr[i][1]
    return value

if __name__=="__main__":
    arr = [[60,10],[100,20],[12,30]]
    value = fractional_knapsack(arr,50,3)
    print(arr)
    print(value)