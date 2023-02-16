def play_rock(x,y):
    if y=='scissors':
        x>y
        print(f'{x} is superior to {y}: Player 1. won!')
    elif y== 'paper':
            x<y
            print(f'{y} is superior to {x}: Player 2. won!')     
    elif y== 'rock':
        print("It's a Draw; Play again.") 
    else:
        print("Please enter a valid choice.")
    
    
    
def play_scissors(x,y):
    if y=='paper':
        x>y
        print(f'{x} is superior to {y}: Player 1. won!')         
    elif y== 'rock':
            x<y
            print(f'{y} is superior to {x}: Player 2. won!')  
    elif y== 'scissors':
        print("It's a Draw; Play again.") 
       
    else:
        print("Please enter a valid choice.")
    
def play_paper(x,y):
    if y=='rock':
        x>y
        print(f'{x} is superior to {y}: Player 1. won!')         
    elif y== 'scissors':
            x<y
            print(f'{y} is superior to {x}: Player 2. won!')      
    elif y== 'paper':
        print("It's a Draw; Play again.") 
    else:
        return print("Please enter a valid choice.")




options=['scissors','rock','paper'] 
print(options)

#first player
play=input("Play an option:")
#opponent player
choice =input("Enter your option:")

if play=="rock":
    play_rock(play,choice)
 
elif play=="scissors":
    play_scissors(play,choice)
    
elif play=="paper":
    play_paper(play,choice)
else:
    print("Please enter a valid option. ")