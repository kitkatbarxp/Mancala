"""
A text-based version of the two-player board game Mancala. This program is player vs. player, NOT player vs computer.
"""

# Kit Tse
# 11/26/2012
# CS150A
# Test Project 2: Mancala
#-------------------------------------------------------------------------------

def config():
    """ Initial configuration of the board."""
    
    bowls = {"1":4, "2":4, "3":4, "4":4, "5":4, "6":4, "7":0, "8":4, "9":4, "10":4, "11":4, "12":4, "13":4, "14":0} 
    # "7" is "P1", "14" is "P2"
    
    return bowls


def display_board(bowls):
    """ Display the mancala board."""
    
    board = "-----------------\nCurrent board:\n   "
    
    top_bowls = [13,12,11,10,9,8]
    
    for bowl in top_bowls:
        if bowls[str(bowl)] < 10:
            board += str(bowls[str(bowl)]) + "  "
        else:
            board += str(bowls[str(bowl)]) + " "
    
    if bowls["14"] > 9:
        board += "\n" + str(bowls["14"]) + "                   " + str(bowls["7"]) + "\n   "
    else:
        board += "\n" + str(bowls["14"]) + "                    " + str(bowls["7"]) + "\n   "
    
    for bowl in range(1,7):
        if bowls[str(bowl)] < 10:
            board += str(bowls[str(bowl)]) + "  "
        else:
            board += str(bowls[str(bowl)]) + " "  
            
    print board


def new_board(bowls,bowl):
    """Determines the new board configuration after a move is made. This includes
    checking to see if the bowl in which the last stone is placed is empty."""
    
    if (bowl == 7 or bowl == 14):
        print "Invalid bowl. Please enter your choice again!"
    elif bowls[str(bowl)] == 0:
        print "That bowl is empty!"
    else:
        continued = 0
        
        # figures out how many stones are in the bowl the player has picked
        # then distributes it to the next bowls one by one
        for i in range(bowls[str(bowl)]+1):
            if i != 0:
                # makes it loop over so if there are stones after placing one in
                # the 14th bowl (player 2's mancala), go back to bowl 1 and on
                if (bowl+i) > 14:
                    continued += 1
                    bowls[str(continued)] += 1
                else:
                    bowls[str(bowl+i)] += 1 
            
            if i == range(bowls[str(bowl)]+1)[-1]:
                
                last_bowl(bowls,bowl,player)
            
        bowls[str(bowl)] = 0 
                    
    return bowls    


def move_choice(player):
    """ Displays the bowl choices a player has each turn."""
    
    print "Select a move:"
    
    if player % 2 != 0:
        print "   –  –  –  –  –  –   \n–                    –\n   1  2  3  4  5  6\n"
    else:
        print "   13 12 11 10 9  8   \n—                    —\n   —  —  —  —  —  —\n"
    

def pick_bowl(player):
    """Prompts user to choose a bowl when it's his/her turn."""    
    
    if player % 2 != 0:
        bowl = raw_input("Player 1 -- from 1-6: ")
        
        choices = [1,2,3,4,5,6]
        
        if int(bowl) not in choices:
            print "Invalid input. Choose again!"
            return pick_bowl(player)
    else:
        bowl = raw_input("Player 2 -- from 8-13: ")
        
        choices = [8,9,10,11,12,13]
        
        if int(bowl) not in choices:
            print "Invalid input. Choose again!"
            return pick_bowl(player)
   
    return bowl


def last_bowl(bowls,bowl,player):
    """checks to see if the main bowl in which the last stone is placed was 
    empty"""
    
    last_bowl = bowl + bowls[str(bowl)]
                            
    if last_bowl > 14:
        actual_bowl = last_bowl - 14
        last_bowl = actual_bowl
        
    if last_bowl != (7 and 14):
        num_of_stones = bowls[str(last_bowl)]
        if num_of_stones == 1:
            opposite_bowl= 14 - last_bowl
            if player % 2 == 0:
                bowls["14"] += bowls[str(opposite_bowl)]
            else:
                bowls["7"] += bowls[str(opposite_bowl)]
                        
            bowls[str(opposite_bowl)] = 0
            bowls[str(bowl)] = 0
            return bowls    
        

def num_stones(bowls):
    """ Calculates the number of stones in each side of the main bowls."""
    
    player_1_stones = bowls["1"] + bowls["2"] + bowls["3"] + bowls["4"] + bowls["5"] + bowls["6"]
    
    player_2_stones = bowls["8"] + bowls["9"] + bowls["10"] + bowls["11"] + bowls["12"] + bowls["13"]    
    
    return player_1_stones, player_2_stones
    
                
if __name__ == "__main__":
    print "Welcome to the text-based version of Mancala!\n"
    player = 1
    current_board = config()
    move_choice(player)
    done = False
    while not done:
        bowl = pick_bowl(player)
            
        if current_board[str(bowl)] == 0:
            print "That bowl is empty!"
        else:
            new_board(current_board,int(bowl))
            display_board(current_board)
            
            player_1_stones, player_2_stones = num_stones(current_board)
            
            if player_1_stones == 0 or player_2_stones == 0:
                player_1_mancala = current_board["7"]
                player_2_mancala = current_board["14"]
                
                if player_1_mancala > player_2_mancala:
                    winner = "Player 1"
                else:
                    winner = "Player 2"
                
                print "The winner is %s." %winner
                print "Player 1 has %i points and player 2 has %i points." %(player_1_mancala, player_2_mancala)
                print "Play again soon!"
                done = True
            else:    
                player += 1
                move_choice(player)
