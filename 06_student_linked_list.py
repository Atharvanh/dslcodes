class Node:
    def __init__(self, roll, name, marks):
        self.data = (roll, name, marks)
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def search(self, roll):
        current = self.head
        while current:
            if current.data[0] == roll:
                return current
            current = current.next
        return None

    def add(self, roll, name, marks):
        if self.search(roll):
            return False
        node = Node(roll, name, marks)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        return True

    def delete(self, roll):
        current = self.head
        previous = None
        while current:
            if current.data[0] == roll:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def update(self, roll, name, marks):
        node = self.search(roll)
        if not node:
            return False
        node.data = (roll, name, marks)
        return True

    def sort(self, field, descending=False):
        current = self.head
        while current:
            other = current.next
            while other:
                if (current.data[field] < other.data[field] if descending else current.data[field] > other.data[field]):
                    current.data, other.data = other.data, current.data
                other = other.next
            current = current.next

    def records(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

def main():
    students = StudentList()
    while True:
        choice = input('1 Add  2 Delete  3 Update  4 Search  5 Sort  6 Display  0 Exit: ')
        if choice == '0':
            break
        if choice in ('1', '3'):
            roll = int(input('Roll number: '))
            name = input('Name: ')
            marks = float(input('Marks: '))
            ok = students.add(roll, name, marks) if choice == '1' else students.update(roll, name, marks)
            print('Done' if ok else 'Duplicate roll number or record not found')
        elif choice == '2':
            print('Deleted' if students.delete(int(input('Roll number: '))) else 'Not found')
        elif choice == '4':
            node = students.search(int(input('Roll number: ')))
            print(node.data if node else 'Not found')
        elif choice == '5':
            field = input('Sort by 1 Roll number or 2 Marks: ')
            order = input('Order: 1 Ascending or 2 Descending: ')
            if field not in ('1', '2') or order not in ('1', '2'):
                print('Invalid choice')
                continue
            students.sort(0 if field == '1' else 2, order == '2')
            print('Records:', students.records())
        elif choice == '6':
            print('Records:', students.records())
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
