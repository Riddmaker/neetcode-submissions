# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#AI EXAMPLE SOLUTION, FOR ME:
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Base Case: Both nodes are None -> The subtrees are identical at this position
        if not p and not q:
            return True
            
        # 2. Base Case: Only one node is None, OR the values do not match -> The subtrees are different
        # (Since we already checked if BOTH are None above, "not p or not q" 
        # specifically catches the case where exactly ONE is None).
        if not p or not q or p.val != q.val:
            return False
            
        # 3. Recursive Step: Both nodes exist and share the same value.
        # Now, recursively check both the left subtree AND the right subtree.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)