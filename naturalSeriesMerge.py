# scalanie serii naturalnych

import re


class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None


head = Node(2)
tmp = head
tab = [3,5,1,2,4,2,3,4,7,9]
for i in tab:
    tmp.next = Node(i)
    tmp = tmp.next

def printList(head):
    tmp = head
    while(tmp != None):
        print(tmp.data, end=' ')
        tmp = tmp.next
    print(" ")

def odetnij(head):
    backup = head
    while(head != None):
        if(head.next == None):
            return (backup, head.next)
        if(head.next.data < head.data):
            tmp = head
            head = head.next
            tmp.next = None
            return (backup, head)
        head = head.next

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


def findLast(head):

    while(head.next != None):
        head = head.next
    return head


def appendToEnd(head, toAppend):
    if(head == None):
        return toAppend

    last = findLast(head)
    last.next=toAppend
    return head
    



def scalanieSeriiNaturalnej(head):

    while(True):
        p1, head = odetnij(head)
        if(head == None): 
            break
        p2, head = odetnij(head)

        p3 = merge(p1, p2)
        
        head = appendToEnd(head, p3)
     
        printList(head)
       
    printList(p1)

scalanieSeriiNaturalnej(head)