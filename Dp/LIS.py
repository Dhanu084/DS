from typing import List

class Solution:
    # Recursion
    def dfs(self, nums, index, n, prev):
        if index>= n:
            return 0
        
        including = excluding = 0
        
        if prev == -1 or nums[prev]<nums[index]:
            including = 1+self.dfs(nums, index+1,n,index)
        excluding = self.dfs(nums, index+1, n, prev)
        
        return max(including, excluding)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.dfs(nums, 0, len(nums), -1)

    
    # Memoization
    def dfs(self, nums, index, n, prev, dp):
        if index>= n:
            return 0
        
        if dp[index][prev+1]!=-1:
            return dp[index][prev+1]
        
        including = excluding = 0
        
        if prev == -1 or nums[prev]<nums[index]:
            including = 1+self.dfs(nums, index+1,n,index, dp)
        excluding = self.dfs(nums, index+1, n, prev, dp)
        
        dp[index][prev+1] = max(including, excluding)
        
        return dp[index][prev+1]
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for i in range(n+1)] for j in range(n)]
        return self.dfs(nums, 0, n, -1, dp)