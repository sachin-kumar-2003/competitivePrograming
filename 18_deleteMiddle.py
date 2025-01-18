'''
Delete Middle Node Of Linked List
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional,ListNode
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next==None:
      return head.next
    slow=head
    fast=head
    curr=head
    while fast and fast.next!=None:
      curr=slow
      slow=slow.next
      fast=fast.next.next
    curr.next=slow.next
    slow.next=None
    return head