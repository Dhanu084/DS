def findSubsequenceofSum(arr,index,subsequence,curr_sum,target_sum):
    # print(subsequence,curr_sum)
    if index>=len(arr):
        # print(subsequence,curr_sum,target_sum)
        if curr_sum == target_sum:
            print(subsequence)
        return

    subsequence.append(arr[index])
    findSubsequenceofSum(arr,index+1,subsequence,curr_sum+arr[index], target_sum)
    subsequence.pop()
    findSubsequenceofSum(arr,index+1,subsequence,curr_sum,target_sum)

if __name__ == "__main__":
    arr = [1,1,2,3]
    findSubsequenceofSum(arr,0,[],0,2)