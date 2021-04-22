#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 22/4/21 11:08 AM
# @Author   : haichen.zhao@shopee.com
# @File     : 104.py
"""
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.search_max_depth(root.left, 1), self.search_max_depth(root.right, 1))

    def search_max_depth(self, node, max_depth):
        # recursive
        if not node:
            return max_depth
        max_depth += 1
        return max(self.search_max_depth(node.left, max_depth), self.search_max_depth(node.right, max_depth))


