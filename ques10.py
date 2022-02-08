# n=int(input("enter no. of row"))
# # i=1
# while n>0:
#     # b=1
#     # while b<i:
#     #     print(" ",end=" ")
#     #     b=b+1
#     j=1
#     while (j<=n*2-1):
#         print(n,end=" ")
#         j=j+1
#     print()
#     n=n-1
#     # i=i+1








n = 8
m = n+1
  

for i in range(n//2-1):
    for j in range(m):
          
        # condition for printing stars to GFG upper line
        if i == n//2-2 and (j == 0 or j == m-1):
            print("💓", end=" ")
              
        # condition for printing stars to left upper
        elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
                            or (j-i == m//2-n//2+3 and j > m//4)):
            print("💓", end=" ")
              
        # condition for printing stars to right upper
        elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
                           or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
            print("💓", end=" ")
              
        # condition for printing spaces
        else:
            print(" ", end=" ")
    print()
  
# loops for lower part
for i in range(n//2-1, n):
    for j in range(m):
          
        # condition for printing stars
        if (i-j == n//2-1) or (i+j == n-1+m//2):
            print("💓", end=" ")
              
        # condition for printing GFG
        elif i == n//2-1:
              
            if j == m//2-1 or j == m//2-1:
                print('chandni', end=" ")
            elif j == m//2:
                print('', end=" ")
            else:
                print('', end=" ")
                  
        # condition for printing spaces
        else:
            print(' ', end=" ")
              
    print()





















