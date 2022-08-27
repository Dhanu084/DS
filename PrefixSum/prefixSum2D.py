class PrefixSum:

    def __init__(self, arr) -> None:
        n = len(arr)
        m = len(arr[0])
        self.prefixSum = [[0 for i in range(m+1)] for j in range(n+1)]


        for i in range(1,n+1):
            for j in range(1,m+1):
                self.prefixSum[i][j] = self.prefixSum[i-1][j] + self.prefixSum[i][j-1] - self.prefixSum[i-1][j-1]+arr[i-1][j-1]

    def printMatrix(self, mat = None):
        if mat is None:
            mat = self.prefixSum
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=' ')
            print()

    def query(self, r1, c1, r2, c2):
        r2, c2 = r2+1, c2+1

        return self.prefixSum[r2][c2]-self.prefixSum[r1][c2]-self.prefixSum[r2][c1] + self.prefixSum[r1][c1]


if __name__=="__main__":
    mat = [[1,5,4],[2,0,2],[1,3,2]]
    # mat = [[0,1,0],[1,1,1],[0,1,0]]
    p = PrefixSum(mat)
    p.printMatrix(mat)
    print('*'*10)
    p.printMatrix()
    print('*'*10)
    print(p.query(1,1,2,2))
    print(p.query(0,0,1,2))
    print(p.query(1,0,2,2))
    print(p.query(0,1,2,2))