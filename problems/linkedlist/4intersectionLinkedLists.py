from typing import Optional
class ListNode:
    def __init__(self , x):
        self.val = x
        self.next = None
class Solution:
    def Intersection_linked_lists(self , headA : ListNode , headB : ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1

# ---------- Example usage ----------

# Create common intersection part: 8 -> 10
c1 = ListNode(8)
c2 = ListNode(10)
c1.next = c2

# Create List A: 3 -> 7 -> 8 -> 10
a1 = ListNode(3)
a2 = ListNode(7)
a1.next = a2
a2.next = c1

# Create List B: 99 -> 1 -> 8 -> 10
b1 = ListNode(99)
b2 = ListNode(1)
b1.next = b2
b2.next = c1

# Run the solution
sol = Solution()
intersection = sol.Intersection_linked_lists(a1, b1)

# Print result
if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")



        