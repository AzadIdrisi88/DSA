'''
Bubble-Sort -->> In this sort we campare adjacent element.
If left element is greater than right element than we swap it that point.
3,2,1
2,1,3
1,2,3
'''
a=[3,2,1]
n=len(a)
for i in range(n-1):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        print(a)        

