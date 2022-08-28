from math import inf
# Return max number between ranges
# TC - O(LogN)
# SC - O(N)
arr = [8,2,5,1,4,5,3,9,6,10]
segment = [0]*100
def segmentTree(arr, si, l, r, maximum):

    if l == r:
        segment[si] = arr[l]
        return

    mid = l+(r-l)//2
    segmentTree(arr,si*2+1, l, mid, maximum)
    segmentTree(arr, si*2+2,mid+1, r, maximum)

    segment[si] = max(segment[si*2+1], segment[si*2+2]) if maximum else min(segment[si*2+1], segment[si*2+2])

def query(si, li, ri, ql, qr, maximum):
    if li>=ql and ri<=qr:
        return segment[si]
    
    if ri<ql or li>qr:
        return -inf if maximum else inf
    mid = li+(ri-li)//2
    left = query(2*si+1, li, mid, ql, qr, maximum)
    right = query(2*si+2, mid+1, ri, ql ,qr, maximum)

    return max(left, right) if maximum else min(left, right)

if __name__=="__main__":
    
    segmentTree(arr, 0,0 ,len(arr)-1, True)
    # print(segment)
    q = [[0,4],[7,9],[0,9],[2,5]]

    for quer in q:
        print(query(0,0, len(arr)-1, quer[0], quer[1], True))
    print('Below is min range')
    segmentTree(arr, 0,0 ,len(arr)-1, False)
    # print(segment)
    q = [[0,4],[7,9],[0,9],[2,5]]

    for quer in q:
        print(query(0,0, len(arr)-1, quer[0], quer[1], False))
