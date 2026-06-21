class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Node:
    def __init__(self):
        self.head=None
    
    def insertNode(self,data):
        newNode=ListNode(data)
        if self.head==None:
            self.head=newNode
            return
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=newNode

    def printlist(self):
        cur=self.head
        while cur!=None:
            print(cur.val,end='->')
            cur=cur.next
        print("Null")

def solution(l1,l2):
    dummy=ListNode()
    cur=dummy
    carry=0
    while l1 or l2 or carry:
        v1=l1.val if l1 else 0
        v2=l2.val if l2 else 0
        value=v1+v2+carry
        carry=value//10
        value=value%10
        cur.next=ListNode(value)
        cur=cur.next
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None
    return dummy.next
l1=Node()
l2=Node()
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
for i in arr1:
    l1.insertNode(i)
for i in arr2:
    l2.insertNode(i)
res=Node()
res.head=solution(l1.head,l2.head)
res.printlist()