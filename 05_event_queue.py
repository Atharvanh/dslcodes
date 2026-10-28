from collections import deque

class EventQueue:
    def __init__(self):
        self.events = deque()
        self.next_id = 1

    def add(self, name):
        event = (self.next_id, name)
        self.events.append(event)
        self.next_id += 1
        return event[0]

    def process(self):
        return self.events.popleft() if self.events else None

    def cancel(self, event_id):
        for event in self.events:
            if event[0] == event_id:
                self.events.remove(event)
                return True
        return False

def main():
    queue = EventQueue()
    while True:
        choice = input('1 Add  2 Process next  3 Display  4 Cancel  0 Exit: ')
        if choice == '0':
            break
        if choice == '1':
            print('Event ID:', queue.add(input('Event name: ')))
        elif choice == '2':
            event = queue.process()
            print('Processed:', event) if event else print('Queue is empty')
        elif choice == '3':
            print('Pending events:', list(queue.events))
        elif choice == '4':
            print('Cancelled' if queue.cancel(int(input('Event ID: '))) else 'Event not found')
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
