def CombinationSum(arr,target_sum,temp,result,index):
    if target_sum<0 or index>len(arr)-1:
        return
    if target_sum == 0:
        result.append(temp[0:])
        return

    temp.append(arr[index])
    CombinationSum(arr,target_sum-arr[index],temp,result,index)
    temp.pop()
    CombinationSum(arr,target_sum,temp,result,index+1)


if __name__=="__main__":
    arr = [2,3,6,7]
    result = []
    CombinationSum(arr,7,[],result,0)
    for res in result:
        print(res)