# Complete the has_cycle function below.

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if head == None:
        return False
    current=head
    while True:
        if current.next==None:
            return False
        if current.next=='cycle':
            return True
        next=current.next
        current.next='cycle'
        current=next

