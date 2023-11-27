class dlinklist:
    def __init__(self, key, value, pre, next):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.num_elem = 0
        self.capacity = capacity
        self.kv = dict()
        self.head = dlinklist(-1, -1, None, None)
        self.head.pre = self.head
        self.head.next = self.head

    def move_node_to_front(self, node):
        node.pre.next = node.next 
        node.next.pre = node.pre
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next.pre = node
    
    def remove_tail(self):
        tail = self.head.pre
        del self.kv[tail.key]
        self.head.pre = tail.pre
        tail.pre.next = self.head

    def lru_evict(self):
        self.num_elem -= 1
        self.remove_tail()

    def lru_update(self, node):
        self.move_node_to_front(node)
    
    def lru_insert(self, key, value):
        self.num_elem += 1
        temp = self.head.next
        node = dlinklist(key, value, self.head, temp)
        self.head.next = node
        temp.pre = self.head.next
        self.kv[key] = node

    def get(self, key: int) -> int:
        if key in self.kv.keys():
            node = self.kv[key]
            self.lru_update(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv.keys(): # cache update
            node = self.kv[key]
            node.value = value
            self.lru_update(node)
        else:
            if self.num_elem >= self.capacity:
                self.lru_evict()
            self.lru_insert(key, value)
            
if __name__ == "__main__":
    lru = LRUCache(1)
    lru.put(2, 1)
    print(lru.get(2))
    lru.put(3, 2)
    print(lru.get(2))
    print(lru.get(3))