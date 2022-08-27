def safe(board,i,j):

    for row in range(i-1,-1,-1):
        if board[row][j] == 'Q':
            return False

    for row in range(i+1,len(board)):
        if board[row][j] == 'Q':
            return False
   
    col = j-1
    for row in range(i-1,-1,-1):
        if col>=0 and  board[row][col] == 'Q':
            return False
        col-=1

    col = j+1
    for row in range(i-1,-1,-1):
        if col<len(board) and board[row][col] == 'Q':
            return False
        col+=1

    
    row = i+1
    for col in range(j-1,-1,-1):
        if row<len(board) and board[row][col] == 'Q':
            return False
        row+=1
    
    row = i+1
    for col in range(j+1,len(board)):
        if row<len(board) and board[row][col]=='Q':
            return False
        row+=1

    return True 

def NQueens(board,row,result):
    # print(row)
    if row>=len(board):
        temp = []
        for bd in board:
            temp.append(bd[0:])
        result.append(temp)
        return

    for i in range(len(board)):
        if safe(board,row,i):
            board[row][i] = 'Q'
            NQueens(board,row+1,result)
            board[row][i] = '.'


if __name__=="__main__":
    board = [['.' for i in range(4)]for y in range(4)]
    result = []
    NQueens(board,0,result)
    for boards in result:
        for board in boards:
            print(board)
        print('*'*10)
        