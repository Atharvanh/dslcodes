class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.deleted = object()

    def search(self, key):
        for step in range(self.size):
            index = (key % self.size + step) % self.size
            if self.table[index] is None:
                return -1
            if self.table[index] is not self.deleted and self.table[index] == key:
                return index
        return -1

    def insert(self, key):
        if self.search(key) != -1:
            return 'Key already exists'
        for step in range(self.size):
            index = (key % self.size + step) % self.size
            if self.table[index] is None or self.table[index] is self.deleted:
                self.table[index] = key
                return 'Inserted'
        return 'Table is full'

    def delete(self, key):
        index = self.search(key)
        if index == -1:
            return False
        self.table[index] = self.deleted
        return True

def main():
    table = HashTable()
    while True:
        choice = input('1 Insert  2 Search  3 Delete  4 Display  0 Exit: ')
        if choice == '0':
            break
        if choice == '1':
            print(table.insert(int(input('Integer key: '))))
        elif choice == '2':
            index = table.search(int(input('Key: ')))
            print('Not found' if index == -1 else 'Found at index ' + str(index))
        elif choice == '3':
            print('Deleted' if table.delete(int(input('Key: '))) else 'Not found')
        elif choice == '4':
            for i, value in enumerate(table.table):
                print(i, 'Deleted' if value is table.deleted else 'Empty' if value is None else value)
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
