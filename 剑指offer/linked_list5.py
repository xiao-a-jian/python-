"""
题目：输入一个链表，从尾到头打印链表每个节点的值。若列表为空，输出[ ]。
首先需要定义一下链表节点的类，然后来构建链表。
按顺序把链表的元素依次保存到一个列表中，在最后反向输出列表的元素就可以了。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例入[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ls = []

        if listNode is None:
            return ls

        while listNode.next:
            ls.append(listNode.val)
            listNode = listNode.next

        ls.append(listNode.val)

        return ls[::-1]


s = Solution()
l1 = ListNode('a')
l2 = ListNode('b')
l3 = ListNode('c')

l1.next = l2
l2.next = l3

print(s.printListFromTailToHead(l1))
