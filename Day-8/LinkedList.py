class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def length(self):
        temp=self.head
        l=0
        while temp:
            l+=1
            temp=temp.next
        return l

    def sumOfEven(self):
        s=0
        temp=self.head
        while temp:
            if temp.data%2==0:
                s+=temp.data
            temp=temp.next
        return s 

l=LinkedList()
values = list(map(int,input().split()))
for i in values:
    l.append(i)
l.display()
print(l.length())
print(l.sumOfEven())
