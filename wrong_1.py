a=[[0], [1, 3], [5, 7], [9, 11], [13, 15],[9,8,7,6]]
i=0
min=a[0]
c=[]
while i<len(a):
    if len(a[i])<min:
        min=a[i]
    print(min)
    i=i+1
j=0
max=0
while j<len(a):
    if len(a)>max:
        max=a[j]
    j=j+1
print(max)
print(min)








# l=[[0],[1,4,2,],[5,7],[9,11],[13,15,17]]
# i=0
# max=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         a=len(l[i])
#         if max<a:
#             max=a
#         t=l[i]
#         j+=1
#     i+=1
# print(t)

# i =0
# max = 0
# while i < len(l):
#     if max < len(l[i]):
#         max = len(l[i])
#         index_list = l[i]
#     i+=1
# print(index_list)



# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# while i<len(numbers):
#         if numbers[i]>20:
#             count=count+1
#         i=i+1
# print(count)





# list1=[[78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78]]
# i=0
# sum=0
# while i<len(list1):
#     j=0
#     while j<len(list1[i]) :
#       sum=sum+(list1[i][j])
#       j=j+1
#     i=i+1
# print(sum)
    