from typing import Optional
class ListNode :
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Linkedlistcycle:
    def linkedlistcycle(self,head: Optional[ListNode]):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
    
        return False
