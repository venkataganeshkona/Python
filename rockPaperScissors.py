"""
    create a two-player rock-paper-scissors game
    ask for plays using input, compare them, print
    out a message of congrats to the winner, and ask
    if players want to start a new game

"""

y = 'y'
while(y=='y'):
   
    firstPlay=input("player 1 enter a move please: ")
    secondPlay=input("player 2 enter a move please: ")
    rock,paper,scissors="rock","paper","scissors"
    
    def game():
        if (firstPlay == rock and secondPlay == rock):
            return("Draw")
        elif(firstPlay == paper and secondPlay == paper):
            return("Draw")
        elif(firstPlay == scissors and secondPlay == scissors):
            return("Draw")
        elif(firstPlay == rock and secondPlay == scissors):
            return("player1 wins!")
        elif(firstPlay == rock and secondPlay == paper):
            return("player2 wins!")
        elif(firstPlay == scissors and secondPlay == rock):
            return("player2 wins!")
        elif(firstPlay == paper and secondPlay == scissors):
            return("player2 wins!")
        elif(firstPlay == scissors and secondPlay == paper):
            return("player1 wins!")
        elif(firstPlay == paper and secondPlay == rock):
            return("player1 wins!")
        else:
            print("you have not selected proper rock-paper-scissor choice")
    print(game())
    
    if(y=='n'):
        break
    else:
        y = input("play again? y or n: ")
