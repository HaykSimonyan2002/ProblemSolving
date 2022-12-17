# Given the root of a binary tree, 
# return the inorder traversal of its nodes' values.



class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def rec(my_root):
            if my_root:
                rec(my_root.left)
                lst.append(my_root.val)
                rec(my_root.right)
        if root:
            rec(root)
        return lst
