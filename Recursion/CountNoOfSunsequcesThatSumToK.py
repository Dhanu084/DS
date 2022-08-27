def count_no_of_subsequence_count_to_prime(arr,index,curr_sum,target_sum)->int:
    if index>=len(arr):
        if curr_sum == target_sum:
            return 1
        return 0

    with_curr = without_curr = 0

    with_curr = count_no_of_subsequence_count_to_prime(arr,index+1,curr_sum+arr[index],target_sum)
    without_curr = count_no_of_subsequence_count_to_prime(arr,index+1,curr_sum,target_sum)

    return with_curr+without_curr


if __name__ == "__main__":
    arr = [1,1,2,3]
    ans = count_no_of_subsequence_count_to_prime(arr,0,0,4)
    print(ans)