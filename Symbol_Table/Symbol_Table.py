import sys

class Symbol_Table:
    def __init__(self):
        self.root = None
        self.n = 0

    
    def insert(self, key, value):
        if(self.n == 0):
            self.root = Node(key, value)
        else:
            self.__insert_rec(self.root, key, value)
        self.n += 1
    
    def __insert_rec(self, current_node, key, value):
        if(key < current_node.key):
            if(current_node.left_child is None):
                current_node.left_child = Node(key, value)
            else:
                self.__insert_rec(current_node.left_child, key, value)
        elif(key > current_node.key):
            if(current_node.right_child is None):
                current_node.right_child = Node(key, value)
            else:
                self.__insert_rec(current_node.right_child, key, value)
        else:
            current_node.value = value


    def get(self, key):
        return self.__get_rec(self.root, key)
        
    def __get_rec(self, current_node, key):
        if(current_node is None):
            return None
        if(key < current_node.key):
            self.__get_rec(current_node.left_child, key)
        elif(key > current_node.key):
            self.__get_rec(current_node.right_child, key)
        else:
            return current_node.value
    
    def ceil(self, key):
        return self.__ceil_rec(self.root, key)
    
    def __ceil_rec(self, current_node, key):
        if(current_node is None):
            return None
        if(current_node.key == key):
            return key
        elif(key < current_node.key):
            result = self.__ceil_rec(current_node.left_child, key)
            if(result is None):
                return current_node.key
            return result
        else:
            return self.__ceil_rec(current_node.right_child, key)
    
    def print_st(self):
        items_levels = []
        self.__print_st(items_levels, self.root, 0)
        for level in items_levels:
            print(level)

    def __print_st(self, items_levels, current_node, level):
        if(current_node is not None):
            if(len(items_levels) <= level):
                items_levels.append([])
            items_levels[level].append((current_node.key, current_node.value))
            self.__print_st(items_levels, current_node.left_child, level+1)
            self.__print_st(items_levels, current_node.right_child, level+1)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right_child = None
        self.left_child = None

def main():
    st = Symbol_Table()
    st.insert(5, 1)
    st.insert(2, 10)
    st.insert(18, 0)
    st.insert(0, 20)
    st.insert(3, 2)
    st.insert(21, 3)
    st.insert(25, 3)
    st.insert(19, 3)
    st.print_st()
    st.remove(2)
    print("")
    print("")
    st.print_st()

main()