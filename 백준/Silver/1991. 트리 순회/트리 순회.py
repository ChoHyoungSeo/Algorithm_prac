class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree(nodes):
    tree = {}
    for key, left, right in nodes:
        if key not in tree:
            tree[key] = Node(key)
        if left != '.':
            tree[key].left = Node(left)
            tree[left] = tree[key].left
        if right != '.':
            tree[key].right = Node(right)
            tree[right] = tree[key].right
    return tree

def preorder(node):
    if node:
        print(node.key, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end='')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end='')

if __name__ == '__main__':
    n = int(input())
    nodes = [input().split() for _ in range(n)]

    tree = build_tree(nodes)
    root = tree['A']

    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)