def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i
    return -1

def binary_search(ids, target):
    low = 0
    high = len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            return mid
        if ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    ids = list(map(int, input('Enter customer IDs: ').split()))
    target = int(input('ID to search: '))
    print('Linear search index (-1 means absent):', linear_search(ids, target))
    ordered = sorted(ids)
    print('Sorted IDs:', ordered)
    print('Binary search index in sorted list:', binary_search(ordered, target))

if __name__ == '__main__':
    main()
