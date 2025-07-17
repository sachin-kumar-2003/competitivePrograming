'''1137. N-th Tribonacci Number'''
class Solution:
  def tribonacci(self, n: int) -> int:
    def recursion(n,dp):
      if n<=0:return 0
      if n==1 or n==2:return 1
      if dp[n]!=-1:
        return dp[n]
      dp[n]=recursion(n-1,dp)+recursion(n-2,dp)+recursion(n-3,dp)
      return dp[n]
    
    dp=[-1]*(n+1)
    return recursion(n,dp)