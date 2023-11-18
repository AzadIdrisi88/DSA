'''
Quick Sort
'''


def quickSort(a, left, right):
    if left >= right:
        return
    pivot = a[left]
    fp = left
    for i in range(left+1, right+1):
        if a[i] >= pivot:
            continue
        fp += 1
        a[fp], a[i] = a[i], a[fp]
    a[left], a[fp] = a[fp], a[left]
    quickSort(a, left, fp-1)
    quickSort(a, fp+1, right)


a = [2, 5, 8, 6, 7, 3, 9, 4]
n = len(a)
print(a)
quickSort(a, 0, n-1)
print(a)
