class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


    def insert_Node(self,node):
        curent_node = self
        while curent_node.next != None:
            curent_node = curent_node.next
        curent_node.next = node

    def search (self,value : int) -> bool:
        return self._search(self, value)

    def _search(self,node,value : int) -> bool:
        if node.value == value:
            return True
        elif node.next == None :
            return False
        else:
            return node.next._search(node.next,value)

    def print_Node(self):
        start = self
        while start is not None:
            print(start.value)
            start = start.next
head = Node(5)
head.insert_Node(Node(2))
head.insert_Node(Node(12))
head.insert_Node(Node(7))

print(head.search(5))
head.print_Node()