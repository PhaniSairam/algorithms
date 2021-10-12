class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left_child:
                self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                self.right_child.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value), " --> ", end=" ")
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()

    def postorder(self):
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(str(self.value), " --> ", end=" ")

    def inorder(self):
        if self:
            if self.left_child:
                self.left_child.inorder()
            print(str(self.value), " --> ", end=" ")
            if self.right_child:
                self.right_child.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return True
        else:
            return self.root.insert(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()

    def remove(self, data):
        """
        Remove Element scenario's:
        1. If Tree is empty, return False
        2. If trying to remove a node which doesnt exist in Tree, return False
        3. Node has no children
        4. Node which we are trying to remove has only one left child
        5. Node which we are trying to remove has only one right child
        6. Check if the node we are trying to remove has both left and right childs
        7. Node trying to delete is the root node.
        """
        # Case 1:
        if self.root is None:
            # Empty Tree
            return False

        parent = None
        node = self.root
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.left_child
            elif data > node.value:
                node = node.right_child

        # Case 2 : Node doesnt exist
        if node is None or node.value != data:
            return False

        # Case 3: remove-node has no children
        elif node.left_child is None and node.right_child is None:
            if data < parent.value:
                parent.left_child = None
            else:
                parent.right_child = None

        # case 4: Remove node which has left child only
        elif node.left_child and node.right_child is None:
            if data < parent.value:
                parent.left_child = node.left_child
            else:
                parent.right_child = node.left_child

        # case 5: Remove node which has right child only
        elif node.right_child and node.left_child is None:
            if data < parent.value:
                parent.left_child = node.right_child
            else:
                parent.right_child = node.right_child

        # Case 6: Node has both left and right children
        elif node.right_child and node.left_child:
            delNodeparent = node
            delNode = node.right_child
            while delNode.left_child:
                delNodeparent = delNode
                delNode = delNode.left_child
            node.value = delNode.value
            if delNode.right_child:
                if delNodeparent.value > delNode.value:
                    delNodeparent.left_child = delNode.right_child
                elif delNodeparent.value < delNode.value:
                    delNodeparent.right_child = delNode.right_child
            else:
                if delNodeparent.value < delNode.value:
                    delNodeparent.left_child = None
                else:
                    delNodeparent.right_child = None
        else:  # Case 7: Root Node
            if self.root.value == data:
                if self.root.left_child is None and self.root.right_child:
                    self.root = self.root.right_child
                elif self.root.left_child and self.root.right_child is None:
                    self.root = self.root.left_child
                elif self.root.left_child and self.root.right_child:
                    delNodeParent = self.root
                    delNode = self.root.right_child
                    while delNode.left_child:
                        delNodeParent = delNode
                        delNode = delNode.left_child
                    if delNode.right_child:
                        if delNodeParent.value > delNode.value:
                            delNodeParent.left_child = delNode.right_child
                        elif delNodeParent.value < delNode.value:
                            delNodeParent.right_child = delNode.right_child
                    else:
                        if delNode.value < delNodeParent.value:
                            delNodeParent.left_child = None
                        else:
                            delNodeParent.right_child = None
                    self.root.value = delNode.value
                else:  # Incase if no childs available i.e only one node in the graph
                    self.root = None
        return True


bst = Tree()
bst.insert(10)
bst.insert(100)
bst.insert(900)
bst.insert(50)
bst.insert(5)
bst.insert(6)
bst.insert(4)
bst.preorder()
print()
bst.postorder()
print()
bst.inorder()
print()
print(f"Remove node - 5 - {bst.remove(5)}")
bst.inorder()
