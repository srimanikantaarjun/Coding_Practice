"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
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
                for child in node.children:
                    dq.append(child)
            res.append(temp)
        return res
