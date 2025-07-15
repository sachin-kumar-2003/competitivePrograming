'''547. Number of Provinces'''
from collections import  defaultdict
from typing import List
class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    def dfs(curr,visited,adj):
      visited.add(curr)
      for ngbr in adj[curr]:
        if ngbr not in visited:
          dfs(ngbr,visited,adj)


    N=len(isConnected[0])
    adj=defaultdict(list)
    visited=set()

    for i in range(N):
      for j in range(N):
        if isConnected[i][j]==1 and i!=j:
          adj[i].append(j)
          adj[j].append(i)
    
    ans=0
    for i in range(N):
      if i not in visited:
        ans+=1
        dfs(i,visited,adj)
    return ans