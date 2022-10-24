class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    '''
        get_data
        return: Value of the Node
    '''
    def get_data(self):
        return self.val
    
    '''
        set_data
        input: val:any
        Set the value for the particular node with the value given by the user
    '''
    def set_data(self, val):
        self.val = val
        
    '''
        get_next
        return: return the next node
    '''    
    def get_next(self):
        return self.next
    
    '''
        set_next
        input: next:node
        set the next node, to the given next node
    '''
    def set_next(self, next):
        self.next = next
        
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.count = 0
    
    '''
        printer()
        input: No Input
        Output: Prints out every single value in the linkedlist
    '''
    
    def printer(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data())
            current_node = current_node.get_next()      
            
    '''
        insert()
        input: value:any
        return: None
        add the given value to the linkedlist
    '''
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
    
    '''
        find()
        input: value:any
        return: return the value if it is on the list, if not print "Not Found"
    '''
    def find(self, val):
        current_node = self.head
        while current_node is not None:
            if current_node.get_data() == val:
                return current_node
            else:
                current_node = current_node.get_next() 
        return "Not found"

    '''
        delete()
        input: val:any
        delete the value given via the function
    '''
    def delete(self, val):
        current_node = self.head
        previous = None
        
        while current_node is not None:
            if current_node.get_data() == val:
                break
            print(current_node.get_data())
            previous = current_node
            current_node = current_node.get_next()
        
        if current_node is None:
            raise ValueError(f"{val} not in list")
        
        if previous is None:
            self.head = current_node.next
            self.count = self.count - 1
        else:
            previous.set_next(current_node.get_next())
            self.count = self.count - 1
            
    '''
        returnCount()
        return the total count (total number of nodes in the list)
    '''
    def returnCount(self):
        return self.count
    
    '''
        isEmpty()
        return whether the linkedlist is empty or not
    '''
    def isEmpty(self):
        return self.head == None

if __name__ == "__main__":
    # Experimenting with the functions
    L1 = LinkedList()
    L1.insert("balaji")
    L1.insert("Floyd")
    L1.printer()
    print(L1.find("mani"))
    L1.delete("Floyd")
    