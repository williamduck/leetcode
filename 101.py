#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 22/4/21 10:48 AM
# @Author   : haichen.zhao@shopee.com
# @File     : 101.py
"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, left, right):
        # if node not exists
        if not left and not right:
            return True
        # compare the contents of symmetric nodes
        if not left or not right or left.val != right.val:
            return False
        # recursive
        return self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)
