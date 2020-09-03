class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []
        def _walk(node):
            if not node:
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return output


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while (current):
                if current.value > value: # Got to left
                    if current.left == None: # if current is a leaf
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None: # if current is a leaf
                        current.right = Node(value)
                        break
                    current = current.right

if __name__=='__main__':
    print('First empty binary tree got created!!!')
