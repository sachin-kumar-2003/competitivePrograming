'''1079. Letter Tile Possibilities
You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can
make using the letters printed on those tiles.
Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are
"A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".'''
class Solution:
  def numTilePossibilities(self, tiles: str) -> int:
    temp=''
    unique=set()
    used=[0]*len(tiles)
    def backtrack(unique,used,temp):
      if temp in unique:
        return 
      unique.add(temp)
      for i in range(len(tiles)):
        if used[i]==1:
          continue
        used[i]=1
        backtrack(unique,used,temp+tiles[i])
        used[i]=0
    backtrack(unique,used,'')
    return len(unique)-1     