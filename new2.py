import random
x=input("Do you want to play(Y/N):")

if x=="Y":
    y=random.randint(1,10)
    z=int(input("Guess the number:"))
    if y==z:
        print("Correct answer!!")
    else:
        print("Input was invalid or incorrect.Try again!!")    
elif x=="N":
    print("As you wish.We hope you may wish to play later!!!")
else:
    print("Please give the answer again with Y OR N")        
    
       
