
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def append(self, val):
        head = self.head
        if head == None:
            head = ListNode(val)
        else:
            head.next = ListNode(val)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.head = None
        while l1.next != None and l2.next != None:
            if l1.val < l2.val:
                self.append(l1.val)
                self.append(l2.val)
            else:
                self.append(l2.val)
                self.append(l1.val)
            l1 = l1.next
            l2 = l2.next
        while l1.next != None:
            self.append(l1.val)
            l1 = l1.next
        while l2.next != None:
            self.append(l2.val)
            l2 = l2.next
        return self.head

# [1,2,4]
# [1,3,4]

def printList(left, right):
    l = left
    r = right
    while l.next != None:
        print(l.val)
        l = l.next
    while r.next != None:
        print(r.val)
        r = r.next

if __name__ == "__main__":
    solution = Solution()
    z = ListNode(4)
    y = ListNode(2)
    x = ListNode(1)
    y.next = z
    x.next = y

    print(x)

    # c = ListNode(4)
    # b = ListNode(3)
    # a = ListNode(1)
    # a.next = b
    # b.next = c
    # printList(x, a)
    # actual = solution.mergeTwoLists(x, c)
    # print(actual)
    # for x in actual:
    #     print(x)
