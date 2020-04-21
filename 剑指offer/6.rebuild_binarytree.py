"""
题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列 {1,2,4,7,3,5,6,8} 和中序遍历序列 {4,7,2,1,5,3,8,6}，则重建二叉树并返回。

思路：对于这个题，必须先知道二叉树的前序遍历和中序遍历的特性。
前序遍历是“根左右”，中序遍历是“左根右”，因此可以通过根的位置来划分左右两边的结点。
此外，在划分两边之后，对于每一边，采取的策略依然和之前一样，因此我们可以考虑采用递归来进行操作。
对于边界值，当前序或者中序的长度为0时return None。
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution (object):
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None

        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root


s = Solution()
pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
res = s.reConstructBinaryTree(pre, tin)
print(res.val)
print(res.left.val)






























