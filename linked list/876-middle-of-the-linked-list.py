# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        array = []

        length = 0
        while head is not None:
            array.append(head)
            head = head.next
            length += 1

        return array[length // 2]

    # time complexity: O(n), where n is the number of nodes in the linked list. We traverse the entire linked list once to store the nodes in an array, which takes linear time.
    # space complexity: O(n), where n is the number of nodes in the linked list. We store all the nodes in an array, which requires linear space.

        # middle = head
        # end = head
        #
        # while end is not None and end.next is not None:
        #     middle = middle.next
        #     end = end.next.next
        #
        # return middle

        # time complexity: O(n), where n is the number of nodes in the linked list. We traverse the entire linked list once to find the middle node, which takes linear time.
        # space complexity: O(1), as we only use a constant amount of extra space
