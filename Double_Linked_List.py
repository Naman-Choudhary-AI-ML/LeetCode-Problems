class Node:
    def __init__(self, data=None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Double Linked List is empty, man")
            return
        itr = self.head
        dllstring = ''
        while itr:
            dllstring += str(itr.data) + '--->'
            itr = itr.next
        print(dllstring)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Double Linked List is empty, man")
            return
        itr = self.get_last_node()
        dllstring = ''
        while itr:
            dllstring += str(itr.data) + '--->'
            itr = itr.prev
        print(dllstring)

    def get_length(self):
        count = 0
        itr = self.head
        while itr :
            count += 1
            itr = itr.next
        return count
    
    def insert_at_begin(self, data):
        node = Node(data, self.head, None)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        
    def get_last_node(self):
        itr = self.head
        while itr:
            if itr.next is None :
                lastnode = itr
            itr = itr.next
        return lastnode
    
    def insert_at_end(self, data):
        if self.head is None :
            node = Node(data, None, None)
            self. head = node
            return
        lastnode = self.get_last_node()
        node = Node(data, None, lastnode)
        lastnode.next = node
    
    def insert_at(self, index, data):
        count = 0
        itr = self.head
        while itr:
            if count == index - 1 :
                node = Node(data, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if self.head is None :
            raise Exception('Nothing to Remove, its empty')
        if index < 0 or index >= self.get_length() :
            raise Exception('The index is beyond range')
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1 :
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after :
                break
            itr = itr.next
            count += 1
        #count+1, as we found the index of data_after entry, and we want to insert it after that point
        self.insert_at(count+1, data_to_insert)

    def remove_by_value(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data :
                break
            itr = itr.next
            count += 1
        self.remove_at(count)

if __name__ == '__main__':

    dll = DoubleLinkedList()
    dll.insert_at_begin(10)
    dll.insert_at_begin(12)
    dll.insert_at_begin(14)
    dll.insert_at_begin(16)
    dll.insert_at_end(25)
    dll.print_forward()
    dll.print_backward()

    print('------------------')
    
    dll = DoubleLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(12)
    dll.insert_at_end(14)
    dll.insert_at_end(16)
    dll.insert_at(2, 13)
    dll.insert_values([18,20,22])
    dll.insert_after_value(18, 19)
    dll.remove_by_value(18)
    dll.print_forward()
    # dll.remove_at(1)
    # dll.print_forward()
    dll.print_backward()