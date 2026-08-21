# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None

        while current:
            tmp = current.next #2 3 4 5 None
            current.next = prev # None 1 2 3 4
            prev = current #1 2 3 4 5
            current = tmp #2 3 4 5 None
        return prev

