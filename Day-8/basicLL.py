class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
 
temp=head
while temp.next:
    print(temp.data,end=" ")
    temp=temp.next
print(temp.data)

temp=head
while temp:
    print(temp.data,end=" ")
    temp=temp.next
