def library_statistics(member_counts, books):
    average = sum(member_counts) / len(member_counts) if member_counts else 0
    zero = member_counts.count(0)
    highest = []
    lowest = []
    modes = []
    if books:
        high = max(books.values())
        low = min(books.values())
        highest = [name for name in books if books[name] == high]
        lowest = [name for name in books if books[name] == low]
        frequency = {}
        for count in books.values():
            frequency[count] = frequency.get(count, 0) + 1
        most = max(frequency.values())
        modes = [count for count in frequency if frequency[count] == most]
    return average, zero, highest, lowest, modes

def main():
    members = list(map(int, input('Enter books borrowed by each member: ').split()))
    books = {}
    for i in range(int(input('Number of books: '))):
        name = input('Book name: ')
        books[name] = int(input('Borrow count: '))
    if any(count < 0 for count in members + list(books.values())):
        print('Borrow counts must be non-negative')
        return
    average, zero, highest, lowest, modes = library_statistics(members, books)
    print('Average books borrowed:', average)
    print('Members with no books:', zero)
    print('Most borrowed books:', highest)
    print('Least borrowed books:', lowest)
    print('Mode of book borrow counts:', modes)
    print('For n members and b books:')
    print('Average: O(n) time, O(1) extra space')
    print('Zero count: O(n) time, O(1) extra space')
    print('Highest and lowest, including ties: O(b) time, O(b) result space')
    print('Mode, including ties: O(b) expected time, O(b) extra space')

if __name__ == '__main__':
    main()
