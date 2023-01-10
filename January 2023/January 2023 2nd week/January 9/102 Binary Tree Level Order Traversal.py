"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        q = []
        res = []
        q.append(root)
        while q:
            nodes = []
            temp = []
            while q:
                node = q.pop(0)
                nodes.append(node.val)
                if node.left is not None:
                   temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            q = temp
            res.append(nodes)
        return res
