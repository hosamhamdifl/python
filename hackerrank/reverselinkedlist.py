def reverse(llist):
    # Write your code here
    node=llist
    prev=None
    while node:
            next_node=node.next
            node.next=prev
            prev=node
            node=next_node
    return prev 