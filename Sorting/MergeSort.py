def merge_sort(arr, start,end):
    if start==end:
        return [arr[end]]
    
    if start>end:
        return []

    mid = start+(end-start)//2


    left_arr = merge_sort(arr, start,mid)
    right_arr = merge_sort(arr, mid+1,end)

    i = j = 0
    new_array = []

    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i] < right_arr[j]:
            new_array.append(left_arr[i])
            i+=1
        else:
            new_array.append(right_arr[j])
            j+=1
    
    while i<len(left_arr):
        new_array.append(left_arr[i])
        i+=1
    
    while j<len(right_arr):
        new_array.append(right_arr[j])
        j+=1
    return new_array


if __name__=="__main__":
    arr = [7,2,37,89,26,37,2,2,1,100,377,568,1000,389783,645,0,-1,-293,-4567]
    arr = merge_sort(arr, 0 ,len(arr)-1)
    print(arr)