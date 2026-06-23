class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):

    # base/terminating condition
    if not head or not head.next:
        return head
    
    # recursive decomposition
    new_head = reverse_list(head.next)

    # reverse current connection while unwinding
    head.next.next = head

    # break old link 
    head.next = None

    return new_head

def print_list(head):

    current = head

    while current:
        print(current.val, end='->')
        current = current.next
    
    print('None')


# linked list creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


# print original linked list
print("Original List:")
print_list(head)

# reverse linked list
new_head = reverse_list(head)
print("Reversed List:")
print_list(new_head)