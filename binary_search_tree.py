# Source: https://www.laurentluce.com/posts/binary-search-tree-library-in-python/comment-page-1/


class Node:
    """tree: left child, right child and node itself"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, data):
        if data < self.data:
            if self.left is None:
                return None
            return self.left.search(data)
        elif data > self.data:
            if self.right is None:
                return None
            return self.right.search(data)
        else:
            return self

    def traverse_inorder(self):
        """print tree in-order"""
        if self.left:
            self.left.traverse_inorder()
        print(self.data)
        if self.right:
            self.right.traverse_inorder()

    # def children_count(self):
    #     count = 0
    #     if self.left:
    #         count += 1
    #     if self.right:
    #         count += 1
    #     return count
    #
    # def delete(self, data):
    #     node = self.search(data)
    #     if node is not None:
    #         child_count = node.children_count()
    #
    #         if child_count == 0:
    #             if parent:


root = Node(8)
root.insert(3)
root.insert(10)
# root.insert(6)


node = root.search(6)
print(node)

print('In-order traversal:')
root.traverse_inorder()
