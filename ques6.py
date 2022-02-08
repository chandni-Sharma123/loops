# i=1500
# while i<=2700:
#     i=i+1
#     if i%7==0:
#         print(i,"divisible")
#     if i%5==0:
#         print(i,"multiple")

    


l=[12,67,98,341]
i=0
sum=0
while i<len(l):
    k=l[i]%10
    k1=l[i]//10
    sum=k+k1
    print(sum,end=" ")
    i+=1
