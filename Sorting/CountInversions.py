def merge_sort(arr, start,end):
    inversions = 0
    if start>end:
        return ([],inversions)

    if start == end:
        return ([arr[start]],inversions)

    mid = start+(end-start)//2
    left_arr,left_inversion = merge_sort(arr,start,mid)
    right_arr,right_inversion = merge_sort(arr,mid+1,end)

    inversions = left_inversion+right_inversion
    new_array = []
    i = j = 0

    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<=right_arr[j]:
            new_array.append(left_arr[i])
            i+=1
        else:
            new_array.append(right_arr[j])
            j+=1
            inversions+=len(left_arr)-i

    while i<len(left_arr):
        new_array.append(left_arr[i])
        i+=1

    while j<len(right_arr):
        new_array.append(right_arr[j])
        j+=1

    return (new_array,inversions)
        
if __name__== "__main__":
    # arr = [8,4,3,2]
    # arr,ans = merge_sort(arr,0, len(arr)-1)
    # print(ans)
    # print(arr)

    # arr = [1,2,3,4,5]
    # arr,ans = merge_sort(arr,0, len(arr)-1)
    # print(ans)
    # print(arr)

    # arr = [1,2,5,3,4] 
    # arr,ans = merge_sort(arr,0, len(arr)-1)
    # print(ans)
    # print(arr)

    # arr = []
    # arr,ans = merge_sort(arr,0, len(arr)-1)
    # print(ans)
    # print(arr)

    # arr = [5,2,6,1]
    # arr,ans = merge_sort(arr,0, len(arr)-1)
    # print(ans)
    # print(arr)
    
    arr = [36343342, 658445766, 281323766,703538013,437455363, 900766801, 84401391 ,159903601, 
    626186515, 127519304, 222484765, 609828661, 190927389 ,152625748 ,358752776 ,522920848 ,494568773 ,977351598 ,782415711 ,966011559]
    arr, ans = merge_sort(arr, 0, len(arr)-1)
    print(ans)