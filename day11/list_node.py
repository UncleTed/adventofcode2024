# double or single linked list?
# list_node :
# next , prev points to the trailing and preceding element in the chain
# value, set_value
# split() : creates a new node. sets new node prev to me. sets new node next to the already existing me.next. sets me.next to the newly split


class Stone:
    def __init__(self, value):
        self.next:Stone = None
        self.prev: Stone = None
        self.value: str = value


class StraightLine:
    def __init__(self):
        self.head:Stone = None
        self.tail: Stone = None

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
        new_stone = Stone(str(value))
        if self.head is None:
            self.head = new_stone
            self.tail = new_stone
        else:
            self.tail.next = new_stone
            self.tail = new_stone

    def insert_in_middle(self, position: int, value: int):
        new_node = Stone(value)
        p = self._get_node_at_position(position)
        print(p.value)
        new_node.next = p.next
        p.next = new_node

    def split(self, splittie: Stone, value: str)->Stone:
        left, right = self._split_in_half(value)
        splittie.value = left
        new_stone = Stone(right)
        new_stone.next = splittie.next
        splittie.next = new_stone
        return new_stone
        
    def size(self)->int:
        counter = 0
        current = self.head
        while(current is not None):
            current = current.next
            counter += 1

        return counter
    
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
            
    
    def _split_in_half(self, value:str):
        middle = len(value)//2
        left= value[0:middle]
        right = value[middle:]
        right = str(int(right))
        return left, right
    
