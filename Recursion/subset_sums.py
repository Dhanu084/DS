def subset_sums(arr,index,curr_sum,result):
    
    if index>len(arr)-1:
        result.append(curr_sum)
        return
    
    subset_sums(arr,index+1,curr_sum+arr[index],result)

    subset_sums(arr,index+1,curr_sum,result)

if __name__=="__main__":
    # arr = [5,2,1]
    # result = []
    # subset_sums(arr,0,0,result)
    # result.sort() # if needed in sorted order
    # print(result)

    arr = [1,2,2]
    result = []
    subset_sums(arr,0,0,result)
    result.sort() # if needed in sorted order
    print(result)