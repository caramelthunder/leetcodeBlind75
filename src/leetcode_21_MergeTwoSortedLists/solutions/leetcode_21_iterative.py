from helpers.leetcode_21_helper import ListNode

class Solution:
    def main(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.main(list1.next, list2)
            return list1
        else:
            list2.next = self.main(list1, list2.next)
            return list2