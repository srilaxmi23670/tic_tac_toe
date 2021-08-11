#Implementation of Two Player Tic-Tac-Toe game in Python.

print('Order of Numbers on board are:')
print('7, 8, 9 for first row')
print('4, 5, 6 for second row')
print('1, 2, 3 for third row')
print('\n')

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".  \nWhich place do you want to choose?")
        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nWhich place do you want to choose?")
            continue
        print('\n')

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ' or theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ' or theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':                
                printBoard(theBoard)                                    # across horintal line
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ' or theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ' or theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)                                    # across vertical line
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ' or theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)                                    # across diagonals
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
