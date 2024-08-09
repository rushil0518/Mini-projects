import random
print("Welcome to Stone-Paper-Scissor")
def winner (i,c) :
   if (i == c) :
     return 0
   elif (i == 1 and c == 2) :
      return -1
   elif (i == 2 and c ==3) :
      return -1
   elif (i ==3 and c ==1) :
      return -1 
   else :
     return 1   
r = int(input("Enter the number of rounds you want to play : "))
user = 0
comp = 0
for d in range(1,r+1) :
 print(f"Round {d}")

 i = int(input("Enter 1 for Stone 2 for Paper 3 for scissor : "))
 if (i > 3 or i < 1) :
     raise ValueError ("Invalid number")
 c = random.randrange(1,3) 
 

 print("You :",i)
 print("Opponent :",c)
 score = winner(i,c)
 if (score == 0) :
    print("Draw")
 elif (score == -1) :
    print("You lose")
    comp = comp + 1
 else :
    print ("You win")
    user = user + 1
 print(f"Score after this round -> {user} : {comp}")

print(f"Final score -> {user} : {comp}")
if (user == comp) :
   print("Match is drawn")
elif (user < comp) :
   print("You lost the match")
else :
   print("You win the match")

