class Solution:
    def __find_path_helper(self,i,j,m,n,visited,path,result):

        if i<0 or j<0 or i>=n or j>=n or visited[i][j] == 1 or m[i][j] == 0:
            return
        if i==n-1 and j==n-1:
            result.append(path)
            return
        visited[i][j] = 1
        self.__find_path_helper(i+1,j,m,n,visited,path+"D",result)
        self.__find_path_helper(i,j+1,m,n,visited,path+"R",result)
        # self.__find_path_helper(i-1,j,m,n,visited,path+"U",result)
        # self.__find_path_helper(i,j-1,m,n,visited,path+"L",result)
        visited[i][j] = 0
        
    def findPath(self, m, n):
        # code here
        result = []
        visited = [[0 for i in range(n)]for j in range(n)]
        # print(visited)
        self.__find_path_helper(0,0,m,n,visited,"",result)
        return result

if __name__=="__main__":
    m = [
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]
        ]

    n = len(m)
    s = Solution()
    res = s.findPath(m,n)
    print(res)


    m = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
        ]

    n = len(m)
    s = Solution()
    res = s.findPath(m,n)
    # print(res)
