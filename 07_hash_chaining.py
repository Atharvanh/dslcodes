class HashTable:
    def __init__(self):
        self.table = [[] for i in range(10)]

    def insert(self, key, value):
        bucket = self.table[key % 10]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        for stored_key, value in self.table[key % 10]:
            if stored_key == key:
                return value
        return None

    def delete(self, key):
        bucket = self.table[key % 10]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return True
        return False

def main():
    table = HashTable()
    while True:
        choice = input('1 Insert  2 Search  3 Delete  4 Display  0 Exit: ')
        if choice == '0':
            break
        if choice == '1':
            table.insert(int(input('Integer key: ')), input('Value: '))
        elif choice == '2':
            value = table.search(int(input('Key: ')))
            print('Not found' if value is None else 'Value: ' + value)
        elif choice == '3':
            print('Deleted' if table.delete(int(input('Key: '))) else 'Not found')
        elif choice == '4':
            for i, bucket in enumerate(table.table):
                print(i, bucket)
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
