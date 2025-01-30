''' 
Word Search
Given an m x n grid of characters board and a string word, return true
if word exists in the grid.The word can be constructed from letters of 
sequentially adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be used more than once.
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
 word = "ABCCED"
Output: true'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def backtrack(row,col,idx):
            if idx==len(word):
                return True
            if row<0 or col>=len(board[0]) or row>=len(board) or col<0:return False
            if word[idx]!=board[row][col]:return False
            if (row,col)  in visited:
                return False
            visited.add((row,col))
            found=(backtrack(row+1,col,idx+1) or 
            backtrack(row,col+1,idx+1) or 
            backtrack(row-1,col,idx+1) or 
            backtrack(row,col-1,idx+1)) 
            visited.remove((row,col))
            return found
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0]==board[i][j] and backtrack(i,j,0):
                    return True
        return False          