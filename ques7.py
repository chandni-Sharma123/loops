number=int(input('enter number'))
number_2 = number
sum=0
while number > 0:
    num = number %10
    sum = sum + num**3
    number= number // 10
if sum ==number_2:
    print(number_2,"Amstrong")
else:
    print(number_2,"Not Amstrong")












    


















































    
    
    
    