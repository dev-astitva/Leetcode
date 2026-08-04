# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        x,y=0,0
        top,bottom=0,m-1
        left,right=0,n-1
        mat=[[-1 for _ in range(n)] for _ in range(m)]
        curr=head
        while curr:
            while curr and x<=right:
                mat[top][x]=curr.val
                curr=curr.next
                x+=1
            top+=1
            y=top

            while curr and y<=bottom:
                mat[y][right]=curr.val
                curr=curr.next
                y+=1
            right-=1
            x=right
            
            while curr and x>=left:
                mat[bottom][x]=curr.val
                curr=curr.next
                x-=1
            bottom-=1
            y=bottom
            
            while curr and y>=top:
                mat[y][left]=curr.val
                curr=curr.next
                y-=1
            left+=1
            x=left

        return mat