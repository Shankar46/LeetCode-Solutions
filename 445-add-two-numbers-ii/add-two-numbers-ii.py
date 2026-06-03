# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr=l1
        values=[]
        while curr:
            values.append(curr.val)
            curr=curr.next
        prev=l2
        value=[]
        while prev:
            value.append(prev.val)
            prev=prev.next
        new=int("".join(map(str, values)))+int("".join(map(str, value)))
        result = [int(digit) for digit in str(new)]
        dummy=ListNode(0)
        prev=dummy
        for i in result:
            prev.next=ListNode(i)
            prev=prev.next
        return dummy.next