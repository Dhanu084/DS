def get_partition(arr, left, right):
    pivot = arr[right]
    start = left
    
    for i in range(left,right):
        if arr[i]<=pivot:
            arr[start],arr[i] = arr[i],arr[start] # swap the smaller elements to the left
            start+=1
    
    arr[start],pivot = pivot,arr[start]
    # left to start are the elements less than pivot and right to start are the elements greater than pivot
    return start


def quick_sort(arr,start,end):
    if start>end:
        return

    partition = get_partition(arr,start,end)

    quick_sort(arr, start, partition-1)
    quick_sort(arr,partition+1, end)


if __name__=="__main__":
    arr = [7,2,37,89,26,37,2,2,1,100,377,568,1000,389783,645,0,-1,-293,-4567]
    '''
    [7,2]
    '''
    quick_sort(arr,0,len(arr)-1)
    print(arr)
    arr1 = [4, 5, 1, 2, 3]
    '''
        [4, 5, 1, 2, 3]
        1, 5, 4, 2 ,3
        1, 2 ,4 5, 3

        1, 2, 3, 5, 4
    '''
    arr2 = [1, 2, 3, 4, 5]
    quick_sort(arr1,0,len(arr1)-1)
    quick_sort(arr2,0,len(arr2)-1)
    print(arr1)
    print(arr2)