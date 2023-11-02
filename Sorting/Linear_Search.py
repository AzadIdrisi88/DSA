'''
linear search of sorted array.find a given number.
'''
# x=int(input('enter a number to find = '))
# a=[1,2,5,10,15,25]
# n=len(a)
# for i in range(n):
#     if x==a[i]:
#         # print(a[i],i)
#         # print(f'The Number {a[i]} found at {i}')
#         print(' The Number '+str(a[i])+ ' found at index '+str(i))
#         break
# print('not found')

'''
Count the occurence of the given number .
'''
# x = int(input('enter a number to find = '))
# a = [1, 2, 5, 10, 15, 2, 8, 5, 2]
# n = len(a)
# count = 0
# for i in range(n):
#     if x == a[i]:
#         count = count+1
#         # count +=1
#         print(f'Found {x} at index {i}')
# # print('count = ',count)
# print(f' The Number {x} appear {count} times in a list.')

'''
Find the first index and last index of given number.
'''       
# x=int(input('Enter the number = '))
# a=[1,2,5,8,7,9,8,3,4,8,9]   
# n=len(a)
# result1='Not Found'
# result2='Not Found'
# for i in range(n):
#     if x==a[i]:
#         result1=' First index of '+str(x)+' at '+str(i)
#         break
# print(result1)
    
# for i in range(n-1,-1,-1):
#     if x==a[i]:
#        result2=' Last index of '+str(x)+' at '+str(i) 
#        break
# print(result2)
   
'''
Find Minimum Value in given list and also find its position and swap it. 
'''
a=[2,5,8,7,1,-4,9]
minimum=a[0]
minimumindex=0
n=len(a)
for i in range(n):
    if a[i]<minimum:
        minimum=a[i]
        minimumindex=i
# print(minimum,minimumindex)
print(a)
# temp=a[0]
# a[0]=a[minimumindex]
# a[minimumindex]=temp
a[0],a[minimumindex]=a[minimumindex],a[0]
print(a)
