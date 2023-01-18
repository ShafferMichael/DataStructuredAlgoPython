class Node:
    def __init__(self, value, link_node=None):
        """
        Initialize a new Node with a given value and a link to the next Node (default is None)
        """
        self.value = value
        self.link_node = link_node

    def set_link_node(self, link_node):
        """
        Set the link to the next Node
        """
        self.link_node = link_node

    def get_link_node(self):
        """
        Get the link to the next Node
        """
        return self.link_node

    def get_value(self):
        """
        Get the value of the Node
        """
        return self.value
