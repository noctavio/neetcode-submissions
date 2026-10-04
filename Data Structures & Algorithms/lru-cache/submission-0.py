class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity# create a hashmap with `capacity`

        self.mstRcnt = Node(0,0)
        self.lstRcnt = Node(0,0)

        self.mstRcnt.next = self.lstRcnt
        self.lstRcnt.prev = self.mstRcnt

    def insert(self, node):
        nxt = self.mstRcnt.next

        self.mstRcnt.next = node
        node.prev = self.mstRcnt

        node.next = nxt
        nxt.prev = node


    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        # this is where the problem arises, we need to track least recent
        # if we do a linked list and say oldest is furthest in the LL
        # that makes it an O(n) operation. 
        if len(self.cache) > self.capacity:
            lru = self.lstRcnt.prev
            self.remove(lru)
            del self.cache[lru.key]
