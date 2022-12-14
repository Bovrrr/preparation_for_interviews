class Node:
    def __init__(self, value, next, prev):
        self.value = value or 0
        self.next = next or None
        self.prev = prev or None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.size = 1 if head is not None else 0

    def push_back(self, new_node):
        if self.tail is None:
            self.head, self.tail = [new_node] * 2
            self.size = 1
        else:
            self.tail.next = new_node
            self.size += 1

    def push_forward(self, new_node):
        if self.head is None:
            self.head, self.tail = [new_node] * 2
            self.size = 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def insert(self, x, i):
        if i < 0 or self.size < i - 1:
            print(f"i={i} is out of bound. size is {self.size}")
        else:
            j = 0
            curr_node = self.head
            new_node = Node(value=x)
            while j != i - 1:
                curr_node = curr_node.next
                j += 1

            new_node.prev = curr_node
            new_node.next = curr_node

            curr_node.next.prev = new_node
            curr_node.next = new_node

            self.size += 1
