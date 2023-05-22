
## https://leetcode.com/problems/middle-of-the-linked-list/
## Difficulty = Easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or (head != None and head.next == None):
            return head
        
        pointer_1 = head
        pointer_2 = head.next
        while (pointer_2.next != None and pointer_2.next.next != None):
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
        return pointer_1.next

## test
class ListNode(object):
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def createLinkList(lst):
    head = ListNode(lst)
    p = head
    for i in range(1, len(lst)):
        p.next = ListNode(lst[i])
        p = p.next
    return head

def printList(head):
    lst = []
    p = head
    while p:
        lst.append(p.val)
        p = p.next
    return lst

t = [1, 2, 3, 4, 5]
t = [1, 2, 3, 4, 5, 6]
linkList = createLinkList(t)
s = Solution()
s = s.middleNode(linkList)
printList(s)


## guidance
# use two pointers with speed ratio = 1:2
# if the fast pointer reach the None (i.e. after the last node)
# then the next node after the slow pointer is the half size
# the time complexity is O(n)
# the space complexity is O(1)
