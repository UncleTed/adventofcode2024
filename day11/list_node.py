# double or single linked list?
# list_node :
# next , prev points to the trailing and preceding element in the chain
# value, set_value
# split() : creates a new node. sets new node prev to me. sets new node next to the already existing me.next. sets me.next to the newly split


class Stone:
    def __init__(self, value):
        self.next:Stone = None
        self.prev: Stone = None
        self.value: int = value


class StraightLine:
    def __init__(self):
        self.head:Stone = None

    def traverse(self) -> str:
        current = self.head
        buff = []
        while current != None:
            buff.append(str(current.value))
            current = current.next

        return " ".join(buff)
    
    def insert_at_beginning(self,  value: int):
        new_node = Stone(value)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, value):
        new_stone = Stone(value)
        if self.head is None:
            self.head = new_stone
        else:
            self._get_last_node().next = new_stone

    def insert_in_middle(self, position: int, value: int):
        new_node = Stone(value)
        p = self._get_node_at_position(position)
        print(p.value)
        new_node.next = p.next
        p.next = new_node

    
    def _get_last_node(self)-> Stone:
        current = self.head
        while(current.next != None):
            current = current.next
        return current
    
    def _get_node_at_position(self, position: int)->Stone:
        current = self.head
        counter = 0
        while(current is not None):
            if counter == position:
                return current
            else:
                counter += 1
                current = current.next
            
    
