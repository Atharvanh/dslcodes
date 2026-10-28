class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    while root:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False

def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = root.right
        while successor.left:
            successor = successor.left
        root.key = successor.key
        root.right = delete(root.right, successor.key)
    return root

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)

def display(root, level=0):
    if root:
        display(root.right, level + 1)
        print('    ' * level + str(root.key))
        display(root.left, level + 1)

def main():
    root = None
    while True:
        choice = input('1 Insert  2 Delete  3 Search  4 Display  0 Exit: ')
        if choice == '0':
            break
        if choice == '1':
            root = insert(root, int(input('Key: ')))
        elif choice == '2':
            key = int(input('Key: '))
            if search(root, key):
                root = delete(root, key)
                print('Deleted')
            else:
                print('Not found')
        elif choice == '3':
            print('Found' if search(root, int(input('Key: '))) else 'Not found')
        elif choice == '4':
            print('Ascending order:', inorder(root))
            print('Tree (right subtree above each node):')
            display(root)
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
