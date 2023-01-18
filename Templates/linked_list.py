from Nodes import Node

class LinkedList:
    def __init__(self, value=None):
        """
        Initialize a new Linked List with a given value as the head Node (default is None)
        """
        self.head_node = Node(value)

    def get_head_node(self):
        """
        Get the head Node of the Linked List
        """
        return self.head_node

    def insert_beginning(self, new_value):
        """
        Insert a new Node with a given value at the beginning of the Linked List
        """
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        """
        Convert the Linked List to a string
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
        Remove the first Node with a given value from the Linked List
        """
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
