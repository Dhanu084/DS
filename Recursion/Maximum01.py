def helper(matrix, N,M,i,j, dp):
    if i>=N or j>=M or i<0 or j<0 or matrix[i][j] == -1:
        return 1000

    if matrix[i][j] == 1:
        # print("1 present")
        return 0
    if dp[i][j] !=-1:
        return dp[i][j]

    temp = matrix[i][j]
    matrix[i][j] = -1
    di = 0

    right = 1+helper(matrix, N,M,i,j+1,dp)
    left = 1+helper(matrix, N, M, i, j-1,dp)
    up = 1+helper(matrix,N,M,i-1,j,dp)
    down = 1+helper(matrix, N, M, i+1,j,dp)
    matrix[i][j] = temp

    # print(up,right,left,down)
    di = min(up,right,left, down)
    dp[i][j] = di
    return di
        
def maximumZeroOneDistance(matrix, N, M):
   # Write your code here
   # Return an integer denoting the maximum of minimum distances between 0's and 1's.
    ans = 0
    dp = [[-1 for i in range(M)]for j in range(N)]
    for i in range(0, N):
        for j in range(0,M):
            if matrix[i][j] == 0:
                ans = max(ans,helper(matrix,N,M,i,j,dp))
                # print(ans)
    return ans


if __name__=="__main__":
    matrix = [
        [1, 1, 0, 0 ,0, 1 ,0 ,1 ,0, 1],
        [1 ,0 ,1, 0, 1 ,1, 1, 0, 0 ,1],
        [0 ,0, 1, 0, 1 ,0 ,0 ,1 ,0, 0],
        [0 ,0, 0, 0, 1, 1, 1, 0, 0, 0]
        ]
    print(maximumZeroOneDistance(matrix, len(matrix), len(matrix[0])))