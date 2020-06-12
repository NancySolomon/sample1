class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist(node):

    def __init__(self):
        self.head = None

    def insertfirst(self, data):
        newnode = node(data)
        if not self.head:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def insertlast(self,data):
        newnode = node(data)
        if not self.head:
            insertfirst(data)
            return
        actualnode = self.head
        while actualnode.next != None:
            actualnode = actualnode.next
        actualnode.next = newnode
    def insertmid(self,data,after):
        newnode = node(data)
        actualnode = self.head
        previousnode = self.head
        while actualnode.data != after:
            previousnode = actualnode
            actualnode = actualnode.next
        previousnode.next = newnode
        newnode.next = actualnode

    def disp(self):
        actualnode = self.head
        while actualnode != None:
            print(actualnode.data)
            actualnode = actualnode.next
a = linkedlist()
a.insertfirst(1)
a.insertfirst(2)
a.insertlast(3)
a.insertmid(5,2)
a.disp()
