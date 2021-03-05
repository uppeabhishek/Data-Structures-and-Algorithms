class BST():
    def __init__(self):
        self.head = None

    def insert_node(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while True:
                if node.data < temp.data:
                    if temp.left == None:
                        temp.left = node
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = node
                        break
                    else:
                        temp = temp.right

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def preorder(self, node):
        if node == None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")
