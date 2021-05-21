import random 

ch='y'
while ch.lower()=="y":
    #rock paper scissor
    print("_______ROCK!____PAPER!____SCISSOR!_________")
    c=0        #chances
    comp=0     #computer points
    j=0        #player points
    tie=0      #number of draws
    
    while c<10:
        c+=1
        n=input("enter S for scissor \nenter R for rock \nenter P for paper ")
        if n.lower()=="s":
            n="scissor"
            print("scissor")
        elif n.lower()=="r":
            n="rock"
            print("rock")
        elif n.lower()=="p":
            n="paper"                
            print("paper")
        else:
            print("wrong input")
  
        #computer will choose 
        l=["rock","paper","scissor"]
        m=random.choice(l)
        print("computer choosed: ",  m)
    
        if n=="rock" and m=="paper":
            print("you lose a point")
            comp+=1
            print("your points",j,"computer points",comp)
        
        elif n=="paper" and m=="rock":
            print("you won a point")
            j+=1
            print("your points",j,"computer points",comp)
        
        elif n=="scissor" and m=="rock":
            print("you lose a point")
            comp+=1
            print("your points",j,"computer points",comp)
        
        elif n=="rock" and m=="scissor":
            print("you won a point")
            j+=1
            print("your points",j,"computer points",comp)
        
        elif n=="paper" and m=="scissor":
            print("you lose a point")
            comp+=1
            print("your points",j,"computer points",comp)
        
        elif n=="scissor" and m=="paper":
            print("you won a point")
            j+=1
            print("your points",j,"computer points",comp)
           
        elif n==m:
            tie+=1
            print("tied")
            print("your points",j,"computer points",comp)
            
    #prints total points of computer and player's and number of draws       
    else:            
        print(f"Total points of computer are:{comp}\nTotal of your points are:{j},\nTotal number of draws:{tie}")
   
    '''
    print name of winner and point difference
    '''
        if comp>j:
            print("you loose the series by: ",comp-j,"points")
        elif comp==j:
            print("series tied ")
        else:
            print("you win the series by: ", j-comp,"points")
         
        #choice to play again or not 
        ch=input("Enter y to continue \nEnter any key to exit ")
        
else:
    print("Thanks for playing")
        
