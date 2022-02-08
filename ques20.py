num=int(input("enter number"))
i=1
while i<=num:
    j=1
    while j<=i:
        print("2",end="")
        j=j+1
    print(",",end="")
    i=i+1






# guess=5
# number=int(input("enter number 1 to 10"))
# while number<=5:
#     guess = int(input("guess again"))
#     number += 1
#     if guess < number:
#         print('Your guess is wrong')
#     if guess > number:
#         print('Your guess is wrong')
#     if guess == number:
#         break





number = 5
guess=int(input(" enter number 1 to 10"))
number_of_guesses = 0
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess != number:
      print('Your guess is wrong')
    if guess == number:
        break
if guess == number:
    print('your guess is right ')
else:
    print('sorry you have only five chance ' )        