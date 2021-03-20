#Simple Sanke and Ladder game using Random Generated value
#TMR

def random_generator(x,y):                          #Random generator 
    return random.randint(x,y)

import random
end = 100                                           #Initilizing the End value
p1, p2 = 0, 0                                       #Initilizing the position of Player 1 and Player 2
out_list = []
no_of_out = random_generator(9,15)                  #Generating Total no. of Snakes in the game
for i in range(0,no_of_out):                        #For loop to generate the snake position
    outs = random_generator(1,99)
    if outs not in out_list:
        out_list.append(outs)
out_list.sort()
print(out_list)                                     #List of snakes in the board
while (p1 < end and p2 < end):                      #While loop executes untill any one of the player reaches the end position
    print("\nPlayer 1's turn")
    dice = input("Press 'r' to roll the dice : ")
    if dice == 'r':                                 #Get input from the user to roll the dice
        value = random_generator(1,6)               #Generate value randomly from 1 to 6
        p1 += value
        if p1 in out_list:                          #If Player 1 position reaches the Snake position in the list, the Player 1 will returned to any position randomly
            p1 -= random_generator(1,p1)
        if p1 > end:                                #If Player 1 position suppossed exceeds the end position the Player 1 will not be moved (i.e. Player 1 will be at the same position
            p1 -= value
        print("Player 1's position : ",p1)          #Printing Player 1 position
        if (p1 == end):
            print("\nPLAYER 1 WINS!!!")
            break                                   #The loop will break if Player 1 WINS
    print("\nPlayer 2's turn")
    dice = input("Press 'r' to roll the dice : ")
    if dice == 'r':
        value = random_generator(1,6)
        p2 += value
        if p2 in out_list:
            p2 -= random_generator(1,p2)
        if p2 > end:
            p2 -= value
        print("Player 2's position : ",p2)
        if (p2 == end):
            print("\nPLAYER 2 WINS!!!")
            break
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(out_list)                                 #Display the Snake Position throughout the game
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
