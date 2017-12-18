import random
class GuessTheNumber:
    def generateNumber(self):
        x= random.randint(1,100)
        return x
    def compareNumber(self):
         b = int(input("Enter Number of your choice"))
         return b


guess = GuessTheNumber()
a= guess.generateNumber()
#print("the random number is ",a)
b=guess.compareNumber()
if a > b:
    print("the random number is ",a)
    print("guess is low")
elif a<b:
    print("the random number is ",a)
    print("guess is high")
elif a==b:
    print("the random number is ",a)
    print("match")
             
            


            
            

        
        

    
