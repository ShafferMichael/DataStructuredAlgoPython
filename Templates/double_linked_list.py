class DoubleNode:
    def __init__(self, value, prev_node=None, next_node=None):
        """
        Initialize a new Node with a given value and links to the previous and next Nodes (default is None)
        """
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def set_prev_node(self, prev_node):
        """
        Set the link to the previous Node
        """
        self.prev_node = prev_node

    def get_prev_node(self):
        """
        Get the link to the previous Node
        """
        return self.prev_node

    def set_next_node(self, next_node):
        """
        Set the link to the next Node
        """
        self.next_node = next_node

    def get_next_node(self):
        """
        Get the link to the next Node
        """
        return self.next_node

    def get_value(self):
        """
        Get the value of the Node
        """
        return self.value


class DoubleLinkedList:
    def __init__(self, value=None):
        """
        Initialize a new Double Linked List with a given value as the head Node (default is None)
        """
        self.head_node = DoubleNode(value)
        self.tail_node = self.head_node

    def get_head_node(self):
        """
        Get the head Node of the Double Linked List
        """
        return self.head_node

    def get_tail_node(self):
        """
        Get the tail Node of the Double Linked List
        """
        return self.tail_node

    def insert_beginning(self, new_value):
        """
        Insert a new Node with a given value at the beginning of the Double Linked List
        """
        new_node = DoubleNode(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node.set_prev_node(new_node)
        self.head_node = new_node

    def insert_end(self, new_value):
        """
        Insert a new Node with a given value at the end of the Double Linked List
        """
        new_node = DoubleNode(new_value)
        new_node.set_prev_node(self.tail_node)
        self.tail_node.set_next_node(new_node)
        self.tail_node = new_node

    def stringify_list(self):
        """
        Convert the Double Linked List to a string
        """
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        """
        Remove the first Node with a given value from the Double Linked List
        """
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            # update head and tail
            if current_node.get_next_node() is None:
                self.head_node = None
                self.tail_node = None
            else:
                self.head_node = current_node.get_next_node()
                self.head_node.set_prev_node(None)
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    # update links
                    current_node.set_next_node(next_node.get_next_node())
                    # update tail if need
                    if next_node.get_next_node() is None:
                        self.tail_node = current_node
                    else:
                        next_node.get_next_node().set_prev_node(current_node)
                    current_node = None
                else:
                    current_node = next_node
