# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Given a non-empty special binary tree consisting of nodes with the non-negative value, 
    where each node in this tree has exactly two or zero sub-node. If the node has two 
    sub-nodes, then this node's value is the smaller value among its two sub-nodes. 
    More formally, the property root.val = min(root.left.val, root.right.val) always holds.
    
    Given such a binary tree, you need to output the second minimum value in the set 
    made of all the nodes' value in the whole tree.
    
    If no such second minimum value exists, output -1 instead.
    """
    def traverse(self, cur, vals):
        if cur.left:
            vals = self.traverse(cur.left, vals)
        if cur.right:
            vals = self.traverse(cur.right, vals)
        
        vals.add(cur.val)
        return vals
        
        
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        vals = sorted(list(self.traverse(root,set())))
        try:
            return vals[1]
        except:
            return -1
        