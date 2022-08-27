from typing import List

class Solution:
    # Recursion
    def dfs(self, prices, index, buy, n):
        if index == n:
            return 0
        
        buying = selling = 0
        
        if buy:
            buying = max(
                -prices[index]+self.dfs(prices, index+1, False, n),
                self.dfs(prices,index+1, True, n)
            )
        else:
            selling = max(
                prices[index]+self.dfs(prices, index+1, True, n),
                self.dfs(prices,index+1, False, n)
            )
        return max(buying, selling)
    
    def maxProfit(self, prices: List[int]) -> int:
        return self.dfs(prices, 0, True, len(prices))


class Solution:
    # Memoized
    def dfs(self, prices, index, buy, n, dp):
        if index == n:
            return 0
        
        if dp[index][buy]!=-1:
            return dp[index][buy]
        
        buying = selling = 0
        
        if buy:
            buying = max(
                -prices[index]+self.dfs(prices, index+1, False, n, dp),
                self.dfs(prices,index+1, True, n, dp)
            )
        else:
            selling = max(
                prices[index]+self.dfs(prices, index+1, True, n, dp),
                self.dfs(prices,index+1, False, n, dp)
            )
        dp[index][buy] =  max(buying, selling)
        return dp[index][buy]
    
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for i in range(2)] for j in range(len(prices))]
        return self.dfs(prices, 0, True, len(prices), dp)

class Solution:
    # dp
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[-1 for i in range(2)] for j in range(n+1)]

        dp[-1][0] = dp[-1][1] = 0
             
        for i in range(n-1,-1,-1):
            for buy in range(2):
                buying = selling = 0
                
                if buy == 0:
                    buying = max(-prices[i]+dp[i+1][1], dp[i+1][0])
                else:
                    selling = max(prices[i]+dp[i+1][0], dp[i+1][1])
                    
                dp[i][buy] = max(buying, selling)

        return dp[0][0]
        

# Space optimized
def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        next,current = [0]*2, [0]*2
        
        for i in range(n-1, -1, -1):
            for j in range(0,2):
                buy = sell = 0
                if j == 0:
                    buy = max(-prices[i]+next[1], next[0])
                else:
                    sell = max(prices[i]+next[0], next[1])

                current[j] = max(buy, sell)
            next = current[0:]
        return current[0]