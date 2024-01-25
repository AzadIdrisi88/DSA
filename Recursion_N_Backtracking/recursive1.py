'''
                                Recursion
            When function calling itself is called Recursion.
               def f1():
                   f1() 
'''
def f1(n):
    if n==1:
        return 1
    return n+f1(n-1)
s=f1(int(input('Give number to find sum = ')))
print ('The sum of is = ',s)