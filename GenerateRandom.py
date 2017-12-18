import random
class GenerateRandom:
    a=1
    while a!=0:
        a+=1
        dice = ['1','2','3','4','5','6']
        randomno = random.randint(1, 6)
        print(randomno)
        ans=input("would u like to roll again?")
        if ans=="yes":
            a=1
        else:
                a=0
        
        
      
        
        
