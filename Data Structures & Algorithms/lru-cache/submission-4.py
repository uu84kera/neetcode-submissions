# ListNode to store (key, value)
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {} # store {key: Node}
        
        # dummy node
        self.left = Node()
        self.right = Node()

        # double linked list
        self.left.next = self.right
        self.right.prev = self.left

    # remove operation
    def remove(self, node):
        # remove from double linke list
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node


    # maintain most_recont
    def most_recent(self,node):
        # previous right node
        previous_right_node = self.right.prev

        # add node be the most recent node
        previous_right_node.next = node
        node.prev = previous_right_node
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        # if key not in cache
        if key not in self.dic:
            return -1
        
        cur_node = self.dic[key]
        self.remove(cur_node)
        self.most_recent(cur_node)
        return cur_node.value
        

    def put(self, key: int, value: int) -> None:
        # case 1: if key already exists
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            node.value = value
            self.most_recent(node)
            return
        
        # case 2: new key
        new_node = Node(key, value)
        self.dic[key] = new_node
        self.most_recent(new_node)

        # capacity check: exceeded
        if len(self.dic) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.dic[lru.key]