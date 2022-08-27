from collections import defaultdict
class Solution:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.n,self.m = len(matrix), len(matrix[0])

        self.ps = [[0 for i in range(self.m+1)] for j in range(self.n+1)]

        for i in range(1, self.n+1):
            for j in range(1,self.m+1):
                self.ps[i][j] = self.ps[i-1][j]+self.ps[i][j-1]-self.ps[i-1][j-1]+self.matrix[i-1][j-1]
    
    def solve(self, target):
        count = 0
        for r1 in range(1,self.n+1):
            for r2 in range(r1, self.m+1):
                h = defaultdict(int)
                h[0] = 1

                for c in range(1, self.m+1):
                    currSum = self.ps[r2][c]-self.ps[r1-1][c]
                    count+=h[currSum-target]
                    h[currSum]+=1
        return count

if __name__=="__main__":
    s = Solution([[0,1,0],[1,1,1],[0,1,0]])
    print(s.solve(0))