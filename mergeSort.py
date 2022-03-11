##złożoności
## time: n logn
## space: logn


class Node:
    def __init__(self,key):
        self.data=key
        self.next=None


def findMid(head): ## podejście żółwia i królika na szukanie mida
    slow = head
    fast = head.next
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow



def mergeSort(head):
    if(head.next == None):
        return head
    mid = findMid(head)
    head2 = mid.next
    mid.next = None
    newHead1 = mergeSort(head)
    newHead2 = mergeSort(head2)
    final = merge(newHead1, newHead2)
    return final

def merge(head1,head2):
    merged = Node(-1)
     
    temp = merged
    # While head1 is not null and head2
    # is not null
    while (head1 != None and head2 != None):
        if (head1.data < head2.data):
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
     
    # While head1 is not null
    while (head1 != None):
        temp.next = head1
        head1 = head1.next
        temp = temp.next
     
    # While head2 is not null
    while (head2 != None):
        temp.next = head2
        head2 = head2.next
        temp = temp.next
     
    return merged.next ## to za wartownikiem !!