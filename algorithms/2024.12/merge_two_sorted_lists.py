# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "[val=" + str(self.val) + ", next=" + str(self.next) + "]"

def arrayToLinkedList(lst):
    node = None;
    head = None;
    for i in lst:
        if node is None:
            node = ListNode(i, None);
        else:
            node.next = ListNode(i);
            node = node.next;
        head = node if head is None else head;
    return head;

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None;
        node = None;
        tmp = None;
        while True:
            if (list1 is None and list2 is None):
                break;
            if list1 is None:
                tmp = list2;
                list2 = list2.next;
            elif list2 is None:
                tmp = list1;
                list1 = list1.next;
            
            if tmp is None:
                if list1.val < list2.val:
                    tmp = ListNode(list1.val, None);
                    list1 = list1.next
                else:
                    tmp = ListNode(list2.val, None);
                    list2 = list2.next;

            if node is None:
                node = tmp;
                if head is None:
                    head = node;
            else:
                node.next = tmp;
                node = node.next;
            tmp = None;
        return head;

s = Solution()

list1 = arrayToLinkedList([1, 2, 4]);
list2 = arrayToLinkedList([1, 3, 4]);

res = s.mergeTwoLists(list1, list2);
print(res);

list1 = arrayToLinkedList([]);
list2 = arrayToLinkedList([0]);
res = s.mergeTwoLists(list1, list2);
print(res);