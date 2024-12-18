def ConstBoard(board):
  print("Current State of the Board: \n\n");
  for i in range(0,  9):
    if((i>0) and (i%3==0)):
      print("\n");
    if(board[i]==0):
      print("_", end=" ");
      if(board[i]==-1):
        print("X", end=" ");
      if(board[i]==1):
        print("O", end=" ");
  print("\n\n");

def analyzeboard(board):
    for i in range(0, 3):
        row = board[i * 3 : (i + 1) * 3]
        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]
    for i in range(0, 3):
        column = [board[i], board[i + 3], board[i + 6]]
        if column.count(column[0]) == len(column) and column[0] != 0:
            return column[0]
    if board[0] == board[4] == board[8] and board[0] != 0:
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != 0:
        return board[2]
    if 0 not in board:
        return -1
    return 0

def HumanTurn(board):
  pos=input("ENter X position from [1,2,3, 4....9]");
  pos=int(pos);
  if(board[pos-1]!=0):
      print("Wrong Move");
      exit (0);
      board[pos-1]=-1;

def Compturn(board):
  # Add AI logic here
  move = 0
  while board[move] != 0:
      move += 1
  board[move] = 1

def main():
  choice=input("Enter 1 for single Player, 2 for Multiplayer");
  choice = int(choice);
  board=[0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(choice==1):
    print("Ai(O) vs. you(X)");
    player=input("Enter to olay 1(st) or 2(nd): ");
    player=int(player);
    for i in range(0, 9):
      if(analyzeboard(board)!=0):
        break;
      if((i+player)%2==0):
        Compturn(board);
      else:
        ConstBoard(board)
        HumanTurn(board)
  else:
    print("Player1 (O) vs. Plaayer2(X)");
    player=input("Enter to olay 1(st) or 2(nd): ")
    player=int(player)
    for i in range(0, 9):
      if(analyzeboard(board)!=0):
        break;
      if((i+player)%2==0):
        ConstBoard(board)
        Player1Turn(board)
      else:
        ConstBoard(board)
        Player2Turn(board)

  x=analyzerboard(board)
  if(x==0):
    ConstBoard(board)
    print("Draw")
    if(x==-1):
      ConstBoard(board)
      print("Player 1 won")
    if(x==1):
      ConstBoard(board);
      print("Player2 won");

if __name__ == "__main__":
  main();