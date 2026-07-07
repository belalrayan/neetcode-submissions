class Node:
    def __init__(self, key: int = 0, val: int = 0, next: 'Node' = None, prev: 'Node' = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        # dummy head and tail sentinels to avoid None checks
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, key: int) -> 'Node':
        node = self.dict[key]
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        return node

    def add_to_tail(self, node: 'Node') -> None:
        prev_last = self.tail.prev
        prev_last.next = node
        node.prev = prev_last
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.remove(key)
        self.add_to_tail(node)
        self.dict[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.remove(key)
            node.val = value
            self.add_to_tail(node)
            self.dict[key] = node
        else:
            if self.size == self.capacity:
                lru = self.head.next
                self.remove(lru.key)
                del self.dict[lru.key]
            node = Node(key, value)
            self.add_to_tail(node)
            self.dict[key] = node


            

            

        
