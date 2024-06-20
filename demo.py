from unittest import TestCase

class TestNode(TestCase):
    def test_node_value(self):
        
        import exercise
        node = exercise.Node(1)
        self.assertEqual(node.value, 1)

    def test_node_next(self):
        import exercise
        node1 = exercise.Node(1)
        self.assertIsNone(node1.next)
        node2 = exercise.Node(2)
        node1.next = node2
        self.assertEqual(node1.next, node2)
        
class TestLinkedList(TestCase):
    def test_initialization_of_linked_list(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 1)
        self.assertEqual(linked_list.length, 1)
    
    def test_head(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.head.value, 1)

    def test_tail(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.tail.value, 1)

    def test_length(self):
        import exercise
        linked_list = exercise.LinkedList(1)
        self.assertEqual(linked_list.length, 1)        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp




my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop_first())
