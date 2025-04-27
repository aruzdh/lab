from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val: int = x
        self.next: Optional["ListNode"] = None


# Time complexity is O(n), where n is the number of nodes in the linked list, with O(1) extra space.
def has_cycle(head):
    """
    Detects if a linked list has a cycle.

    Args:
        head (ListNode): The head node of the singly linked list.

    Returns:
        bool: True if there is a cycle, False otherwise.
    """
    if not head or not head.next:
        return False

    low = head
    fast = low.next.next

    while fast and fast.next:
        if low == fast:
            return True
        low = low.next
        fast = fast.next.next
    return False
