class BST:

    def __init__(self):
        self.n = 0
        self.root = None

    def insert(self, content):
        if(self.root is None):
            self.root = Node(content)
        else:
            self.__insert_rec(self.root, content)

    def __insert_rec(self, node, content):
        if(node.content >= content):
            if(node.left_child is None):
                node.left_child = Node(content)
            else:
                self.__insert_rec(node.left_child, content)
        else:
            if(node.right_child is None):
                node.right_child = Node(content)
            else:
                self.__insert_rec(node.right_child, content)

    def print_tree(self):
        levels_array = []
        self.print_tree_rec(self.root, 0, levels_array)
        for level in levels_array:
            print(level)
    
    def print_tree_rec(self, node, level, levels_array):
        if(node is not None):
            if(len(levels_array) <= level):
                levels_array.append([])
            levels_array[level].append(node.content)
            self.print_tree_rec(node.left_child, level+1, levels_array)
            self.print_tree_rec(node.right_child, level+1, levels_array)


class Node: 

    def __init__(self, content):
        self.content = content
        self.right_child = None
        self.left_child = None

def main():
    bst = BST()
    bst.insert(1)    
    bst.insert(3)
    bst.insert(10)
    bst.insert(2)
    bst.print_tree()

main()            
