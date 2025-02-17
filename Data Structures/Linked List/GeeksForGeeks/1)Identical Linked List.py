Question:

'''Given the two singly Linked Lists respectively. The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have the same data and with the same arrangement too. If both Linked Lists are identical then return true otherwise return false. 

Examples:

Input: LinkedList1: 1->2->3->4->5->6, LinkedList2: 99->59->42->20
Output: false
Explanation:

As shown in figure linkedlists are not identical.
Input: LinkedList1: 1->2->3->4->5, LinkedList2: 1->2->3->4->5
Output: true
Explanation: 
 
As shown in figure both are identical.
Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)'''

Solution:

class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        

class Solution:
    def areIdentical(self, head1, head2):
        while head1 is not None and head2 is not None:
            if head1.data != head2.data:
                return False
        
        # Move to next nodes
        head1 = head1.next
        head2 = head2.next
    
        return head1 is None and head2 is None
