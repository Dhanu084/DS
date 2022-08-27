def subsequence(arr,index,subseq):
    
    if index == len(arr):
        print(subseq)
        return

    subseq.append(arr[index])
    subsequence(arr,index+1,subseq)
    subseq.pop()
    subsequence(arr,index+1,subseq)


if __name__=="__main__":
    arr = [1,2,3]
    subsequence(arr, 0 , [])