class Solution:
    def helper(self,s, k,index,dp):
        
        if index == len(s):
            if k == 0:
                # print(s[:index])
                return index
            return 0
        
        if k == 0:
            print(s[:index])
            return len(s)-index-1
    
        # if dp[index]!=-1:
        #     return dp[index]
        including = excluding = 0
        if int(s[:index],2)<=k:
            including = 1+self.helper(s,k-int(s[:index],2),index+1,dp)

        excluding = self.helper(s,k+int(s[:index],2),index+1,dp)
        dp[index] = max(including, excluding)
        return max(including, excluding)

    
    def longestSubsequence(self, s: str, k: int) -> int:
        if s=="":
            return 0
        dp = [-1 for i in range(len(s))]

        return self.helper(s,k,1, dp)
  

s = Solution()
print(s.longestSubsequence("1001010",5))
print(s.longestSubsequence("00101001",1))