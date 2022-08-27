class PrefixSum:

    def __init__(self, arr) -> None:
        self.prefixSum = [0]*(len(arr))
        self.prefixSum[0] = arr[0]
        for i in range(1,len(arr)):
            self.prefixSum[i] = self.prefixSum[i-1] + arr[i]

    def querySum(self,l,r):
        return self.prefixSum[r]-self.prefixSum[l-1]


if __name__=="__main__":
    p = PrefixSum([ 3, 6, 2, 8, 9, 2 ])
    print(p.prefixSum)
    q =[ [ 2, 3 ],[ 1, 4 ]]

    for query in q:
        print(p.querySum(*query))