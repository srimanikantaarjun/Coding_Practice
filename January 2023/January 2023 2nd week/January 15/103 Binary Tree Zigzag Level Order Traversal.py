"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        righttoleft = False
        if root is None:
            return res
        dq = deque()
        dq.append(root)
        while dq:
            size = len(dq)
            temp = []
            for i in range(size):
                node = dq.popleft()
                temp.append(node.val)
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            if righttoleft:
                temp.reverse()
            res.append(temp)
            righttoleft = not righttoleft
        return res
