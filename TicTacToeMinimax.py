import random
board=[' ' for i in range (10)]
minM={}
def insertLetter(letter,pos):
    board[pos]=letter
def isEmpty(pos):
    return board[pos]==' '
def printBoard():
    print(" {} | {} | {} |".format(board[1],board[2],board[3]))
    print("___________")
    print(" {} | {} | {} |".format(board[4],board[5],board[6]))
    print("___________")
    print(" {} | {} | {} |".format(board[7],board[8],board[9]))
def isWinner(bo,ch):
    for j in range(1,4):
        flag=True
        for i in range(3*j-2,3*j+1):
            if(bo[i]!=ch):
                flag=False
        if(flag==True):
            return True
    for j in range(1,4):
        flag=True
        for i in range(j,7+j,3):
            if(bo[i]!=ch):
                flag=False
        if(flag==True):
            return True
    if(bo[1]==ch and bo[5]==ch and bo[9]==ch):
        return True
    if(bo[3]==ch and bo[5]==ch and bo[7]==ch):
        return True
    return False
def isBoardFull(bo):
    for i in range(1,10):
        if bo[i]==' ':
            return False
    return True
def playerMove():
    flag=False
    while(not(flag)):
        num=input('Enter a number that is available from 1-9 on the board ')
        try:
            num=int(num)
            if isEmpty(num):
                insertLetter('X',num)
                flag=True
            else:
                print('Error! The tile is already taken. Please try again')
        except:
            print("Please enter a valid number between 1 and 9")
def terminal(s):
    if(s.count(' ')==0):
        return True
    bo=list(s)
    bo.insert(0,' ')
    if(not(isWinner(bo,'X')) and not(isWinner(bo,'O'))):
        return False
    return True
def result(s,ele):
    li=list(s)
    if player(s)=='X':
        li[ele]='X'
    else:
        li[ele]='O'
    return ''.join(li)
def utility(s):
    bo=list(s)
    bo.insert(0,' ')
    if(not(isWinner(bo,'X')) and not(isWinner(bo,'O'))):
        return 0
    elif isWinner(bo,'X'):
        return -1
    else:
        return 1
def action(s):
    li=[i for i in range(len(s)) if s[i]==' ']
    return li
def player(s):
    if s.count('X')>s.count('O'):
        return 'O'
    else:
        return 'X'
def minimax(s):
    if s in minM:
        return minM[s]
    if terminal(s):
        minM[s]=utility(s)
        return minM[s]
    if player(s)=='O':
        li=action(s)
        num=-10
        ind =-1
        for i in li:
            if(minimax(result(s,i))>num):
                num=minimax(result(s,i))
                ind=i
        minM[s]=num
        return num
    else:
        li=action(s)
        num=10
        ind =-1
        for i in li:
            if(minimax(result(s,i))<num):
                num=minimax(result(s,i))
                ind=i
        minM[s]=num
        return num
def compMove():
    s=''.join(board)
    s=s[1:]
    num=-10
    ind=0
    for ele in action(s):
        if minimax(result(s,ele))>num:
            num=minM[result(s,ele)]
            ind=ele
    return ind+1
def beg():
    print("Welcome to Tic Tac Toe! ")
    printBoard()
    while(not(isBoardFull(board))):
        if(not(isWinner(board,'O'))):
            playerMove()
            printBoard()
        else:
            print("O has won, sorry !")
            break
        print("\n")
        if(not(isWinner(board,'X'))):
            pos=compMove()
            if pos==0:
                print('Tie game')
                break
            else:
                print('The computer has selected the position {} to insert an O'.format(pos))
                print("\n")
                insertLetter('O',pos)
                printBoard()
        else:
            print("X has won, congrats !")
            break
        print("\n")

    if(not(isBoardFull) or (not(isWinner(board,'X')) and not(isWinner(board,'O')))):
        print('Tie Game!')
playOn=True
while(playOn):
    beg()
    print('Do you want to continue playing? (Y/N)')
    ch=input()
    if ch=='N':
        playOn=False
    for i in range(1,10):
        board[i]=' '