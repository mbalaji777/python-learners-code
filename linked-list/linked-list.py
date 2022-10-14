class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def get_data(self):
        return self.val
    def set_data(self, val):
        self.val = val
    def get_next(self):
        return self.next
    def set_next(self, next):
        self.next = next
        
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.count = 0
    def printer(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data())
            current_node = current_node.get_next()      
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    
    def find(self, val):
        current_node = self.head
        while current_node is not None:
            if current_node.get_data() == val:
                return current_node
            else:
                current_node = current_node.get_next() 
        return "Not found"

    def delete(self, val):
        current_node = self.head
        previous = None
        
        while current_node is not None:
            if current_node.get_data() == val:
                break
            previous = current_node
            current_node = current_node.get_next()
        
        if current_node is None:
            raise ValueError(f"{val} not in list")
        
        if previous is None:
            self.head = current_node.next
            count -= 1
        else:
            previous.set_next(current_node.get_nextI())
            count -= 1
    def count(self):
        return self.count
    def isEmpty(self):
        return self.head == None

if __name__ == "__main__":
    L1 = LinkedList()
    L1.insert("balaji")
    L1.insert("Floyd")
    L1.printer()
    print(L1.find("mani"))
    