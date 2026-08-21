# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums=[]
        curr=head
        while curr:
            nums+=[curr.val]
            curr=curr.next

        def convert(l,r):
            if l>r:
                return
            mid=(l+r)//2
            node=TreeNode(nums[mid])
            node.left=convert(l,mid-1)
            node.right=convert(mid+1,r)

            return node
        
        return convert(0,len(nums)-1)