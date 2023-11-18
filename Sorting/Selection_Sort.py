'''
Selection sort -->> In selection sort we consider first element as a minimum element and 
compare rest of the element.Easy way to understand is to dry run method on copy. 
'''
a = [2,4,3,1,6,5]
n = len(a)
for i in range(n-1):
    minimum = a[i]
    minimumindex = i
    for j in range(i+1, n):
        if a[j] < minimum:
            minimum = a[j]
            minimumindex = j
    a[i], a[minimumindex] = a[minimumindex], a[i]
    print(a)
