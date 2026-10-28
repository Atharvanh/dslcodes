def selection_sort(values):
    a = values.copy()
    for i in range(len(a) - 1):
        smallest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    return a

def bubble_sort(values):
    a = values.copy()
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def main():
    salaries = list(map(float, input('Enter salaries: ').split()))
    print('Selection sort:', selection_sort(salaries))
    ordered = bubble_sort(salaries)
    print('Bubble sort:', ordered)
    print('Top 5 highest salaries:', ordered[::-1][:5])

if __name__ == '__main__':
    main()
