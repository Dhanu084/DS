def better_permutation(arr, index, result):
    if index>=len(arr):
        return
    
    if index == len(arr)-1:
        result.append(arr[0:])
        return

    for i in range(index,len(arr)):
        swap(arr,i,index)
        better_permutation(arr,index+1,result)
        swap(arr,i,index)


def swap(arr, left_index, right_index):
    arr[left_index],arr[right_index] = arr[right_index],arr[left_index]


if __name__ == "__main__":
    arr = [1,2,3]
    result = []
    better_permutation(arr,0, result)
    for res in result:
        print(res)