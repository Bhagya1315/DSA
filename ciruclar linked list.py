class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(Self):
        self.head = None

    #Insert at begininng
    def insert_begin(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next =new_node
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head= new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def insert_at_position(self,pos,data):
        if pos == 0:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos-1):
            temp = temp.next
            if emp == self.head:
                return

        new_node.next = temp.next
        temp.next = new_node


    #deletion an element
    def delete_begin(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next


    def delete_end(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next.next!= self.head:
            temp = temp.next

            temp.next = self.head

    def delete_value(self,key):
        if self.head is None:
            return
        if self.head.data == key:
            self.delete_begin()
            return

        temp = self.head
        while temp.next!= self.head:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next


    #Access operations
    #search
    def search(self,key):
        if self.head is None:
            return False

        temp = self.head

        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False



    #Update value by position
    def update(self,pos,value):
        temp = self.head

        for _ in range(pos):
            temp = temp.next
            if temp == self.head:
                return
            temp.data = value

    def display(self):
        if self.hed is None:
            return
        temp = self.head
        while True:
            print(temp.data, end = '->')
            temp = temp.next
            if temp == self.head:
                break
            print("(back to head)")



cll = CircularLinkedList()

cll.insert_begin(20)
cll.insert_begin(10)
cll.insert_end(30)
cll.insert_end(40)
cll.display()

cll.insert_at_position(1,15)
cll.display()
cll.delete_begin()
cll.display()
cll.delete_end()
cll.display()
cll.delete_values(15)
cll.display()
print(cll.search(20))
cll.update(1,25)
cll.display()
            
            
                
