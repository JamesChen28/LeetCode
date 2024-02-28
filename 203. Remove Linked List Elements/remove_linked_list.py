
## https://leetcode.com/problems/remove-linked-list-elements/
## Difficulty = Easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        while (head != None and head.val == val):
            head = head.next
        
        pointer = head

        while (pointer != None and pointer.next != None):
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        
        return head


## test
Solution().removeElements(head = [1, 2, 6, 3, 4, 5, 6], val = 6)
Solution().removeElements(head = [], val = 1)
Solution().removeElements(head = [7, 7, 7, 7], val = 7)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linkedlist(list):
    head = ListNode(list[0])
    p = head
    
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    
    return head
    
def printList(head):
    p = head
    list = []
    while p:
        list.append(p.val)
        p = p.next
    return list

head = [1, 2, 6, 3, 4, 5, 6]
val = 6
linkList = linkedlist(head)
s = Solution()
s = s.removeElements(linkList, val)
printList(s)


## guidance
# need to visit all nodes whose value is equal to the given value
# the time complexity is O(n)
# the space complexity is O(1)
