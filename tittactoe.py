# Tittactoe game using python 
def sum (a,b,c):
    return a+b+c
def printBoard(xstate , ystate):
    zero  =  'X' if xstate[0] else ('O' if ystate[0] else 0)
    one   =  'X' if xstate[1] else ('O' if ystate[1] else 1)
    two   =  'X' if xstate[2] else ('O' if ystate[2] else 2)
    three =  'X' if xstate[3] else ('O' if ystate[3] else 3)
    four  =  'X' if xstate[4] else ('O' if ystate[4] else 4)
    five  =  'X' if xstate[5] else ('O' if ystate[5] else 5)
    six   =  'X' if xstate[6] else ('O' if ystate[6] else 6)
    seven =  'X' if xstate[7] else ('O' if ystate[7] else 7)
    eight =  'X' if xstate[8] else ('O' if ystate[8] else 8)
    print("\n")
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
    print(f"--|---|--")

def checkWin(xstate ,ystate):
    wins =[ [0,1,2], [3,4,5], [6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    # Check for each winning combination
    for win in wins:
        if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]])== 3):
            print("X WINS")
            return 1
        if(sum(ystate[win[0]], ystate[win[1]], ystate[win[2]])== 3):
            print("O WINS")
            return 0
    
    return -1



if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    ystate = [0,0,0,0,0,0,0,0,0]
    chance =1
    print("WELCOME TO Tic-Tac-Toe GAME")
    while(True):
        printBoard(xstate , ystate)
        if(chance ==1):
            print("\n")
            print("\nX's TURN\n")
            value = int(input ("Please enter the value: "))
            xstate[value] = 1
        else:
            print("\nO's TURN\n")
            value = int(input ("Please enter the value: "))
            ystate[value] = 1
        cWin= checkWin(xstate , ystate)
        if cWin != -1:
            print("Match Over")
            break

        # Check for draw
        if all(xstate[i] == 1 or ystate[i] == 1 for i in range(9)):
            print("Match Draw")
            break

        chance = 1 - chance
