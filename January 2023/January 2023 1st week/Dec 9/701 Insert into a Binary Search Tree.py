"""https://leetcode.com/problems/search-in-a-binary-search-tree/
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion.
You can return any of them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new = TreeNode(val)
        if root is None:        # if root is empty
            return new          # we return the node with the value
        prev = None
        curr = root
        while curr is not None:
            if val == curr.val:
                return root
            elif val < curr.val:    # if value is less than root
                prev = curr
                curr = curr.left    # we traverse the left subtree
            else:
                prev = curr
                curr = curr.right   # else we traverse the right subtree
        if val < prev.val:
            prev.left = new
        else:
            prev.right = new
        
        return root
# t.c. = O(log n) for balanced BST, O(n) for skewed BST
# s.c. = O(1)
