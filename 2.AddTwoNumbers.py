class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def add_two_numbers(l1, l2):
    # Initialize the dummy head of the result list and a carry variable
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2:
        # Get the values from the current nodes in l1 and l2
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # Calculate the sum of the values and the carry from the previous step
        total = x + y + carry
        carry = total // 10

        # Create a new node with the ones digit of the total
        current.next = ListNode(total % 10)
        current = current.next

        # Move to the next nodes in l1 and l2 if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # If there's still a carry after processing all nodes, create one more node
    if carry > 0:
        current.next = ListNode(carry)

    return dummy_head.next

# Example usage:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Create the first linked list
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create the second linked list
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = add_two_numbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" -> " if result.next else "\n")
    result = result.next
