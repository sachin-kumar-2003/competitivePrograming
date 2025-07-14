'''2685. Count the Number of Complete Components'''
from collections import List,defaultdict
class Solution:
  def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    ans=0
    visited=[0]*n
    adjacencyList=defaultdict(list)
    for key,val in edges:
      adjacencyList[key].append(val)
      adjacencyList[val].append(key)
    def dfs(node,nodeSet):
      visited[node]=1
      nodeSet.add(node)
      for i in adjacencyList[node]:
        if visited[i] ==0 :dfs(i,nodeSet)
    for node in range(n):
      if visited[node]==0:
        isComplete=True
        nodeSet=set()
        dfs(node,nodeSet)
        for i in nodeSet:
          if len(adjacencyList[i])!=len(nodeSet)-1:
            isComplete=False
            break
        if isComplete:ans+=1
    return ans