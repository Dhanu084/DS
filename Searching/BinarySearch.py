def binary_search_recursive(arr,low,high,item):

    if(high>=low):
        mid = low+(high-low)//2

        if arr[mid] == item:
            return mid
        
        if arr[mid] < item:
            return binary_search_recursive(arr,mid+1,high,item)
        else:
            return binary_search_recursive(arr,low,mid-1,item)
    else:
        return -1

def binary_search_iterative(arr,low,high,item):
    while high>=low:
        mid = low+(high-low)//2
        if arr[mid] == item:
            return mid
        if arr[mid]>item:
            high = mid-1
        else:
            low = mid+1
    return -1



if __name__=="__main__":
    arr = [1,2,3,4,5,6]
    print(binary_search_recursive(arr,0,len(arr)-1,6))
    print(binary_search_recursive(arr,0,len(arr)-1,1))
    print(binary_search_recursive(arr,0,len(arr)-1,7))
    print(binary_search_recursive(arr,0,len(arr)-1,-1))
    print(binary_search_recursive(arr,0,len(arr)-1,2))
    print(binary_search_recursive(arr,0,len(arr)-1,3))

    print('*'*100)
    print(binary_search_iterative(arr,0,len(arr)-1,6))
    print(binary_search_iterative(arr,0,len(arr)-1,1))
    print(binary_search_iterative(arr,0,len(arr)-1,7))
    print(binary_search_iterative(arr,0,len(arr)-1,-1))
    print(binary_search_iterative(arr,0,len(arr)-1,2))
    print(binary_search_iterative(arr,0,len(arr)-1,3))