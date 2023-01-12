"""
https://leetcode.com/problems/inorder-successor-in-bst/description/
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root: return None
        if p.right is not None:
            curr = p.right
            while curr.left is not None:
                curr = curr.left
            return curr
        ancestor = None
        curr = root
        while curr != p:
            if p.val < curr.val:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right
        return ancestor
