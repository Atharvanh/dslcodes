class Editor:
    def __init__(self):
        self.text = ''
        self.undo_stack = []
        self.redo_stack = []

    def change(self, text):
        self.undo_stack.append(self.text)
        self.text = text
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return False
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        return True

    def redo(self):
        if not self.redo_stack:
            return False
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        return True

def main():
    editor = Editor()
    while True:
        choice = input('1 Change  2 Undo  3 Redo  4 Display  0 Exit: ')
        if choice == '0':
            break
        if choice == '1':
            editor.change(input('Enter complete new document: '))
        elif choice == '2':
            if not editor.undo():
                print('Nothing to undo')
        elif choice == '3':
            if not editor.redo():
                print('Nothing to redo')
        elif choice != '4':
            print('Invalid choice')
        print('Document:', editor.text)

if __name__ == '__main__':
    main()
