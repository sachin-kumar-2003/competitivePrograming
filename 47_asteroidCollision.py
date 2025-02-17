'''735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row. The
indices of the asteriod in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode. Two asteroids
moving in the same direction will never meet
Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.'''
from typing import List
class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack=[]
    for num in asteroids:
      if num>0 or not stack:
        stack.append(num)
      else:
        while stack:
          if stack[-1]<0:
            stack.append(num)
            break
          elif stack[-1]==abs(num):
            stack.pop()
            break
          elif stack[-1]<abs(num):
            stack.pop()
            if not stack:
                stack.append(num)
                break
          else:break                    
    return stack