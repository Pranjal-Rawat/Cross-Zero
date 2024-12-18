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


def Player1Turn(board):
  pos=input("ENter X position from [1,2,3, 4....9]");
  pos=int(pos);
  if(board[pos-1]!=0):
      print("Wrong Move");
      exit (0);
      board[pos-1]=-1;

def Player2Turn(board):
  pos=input("ENter O position from [1,2,3, 4....9]");
  pos=int(pos);
  if(board[pos-1]!=0):
      print("Wrong Move");
      exit (0);
      board[pos-1]=1;

def analyzeboard(board):
  # Check rows, columns, and diagonals for a win
  for i in range(0, 9, 3):
    if board[i] == board[i+1] == board[i+2] != 0:
      return board[i]
  for i in range(3):
    if board[i] == board[i+3] == board[i+6] != 0:
      return board[i]
  if board[0] == board[4] == board[8] != 0:
    return board[0]
  if board[2] == board[4] == board[6] != 0:
    return board[2]
  if 0 not in board:
    return 0
  return -1

def HumanTurn(board):
  ConstBoard(board);
  Player1Turn(board);

def Compturn(board):
  # Add AI logic here
  available_moves = [i for i, x in enumerate(board) if x == 0]
  if available_moves:
      move = random.choice(available_moves)
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
        ConstBoard(board);
        HumanTurn(board);

  else:
    print("Player1 (O) vs. Plaayer2(X)");
    player=input("Enter to olay 1(st) or 2(nd): ");
    player=int(player);
    for i in range(0, 9):
      if(analyzeboard(board)!=0):
        break;
      if((i+player)%2==0):
        ConstBoard(board);
        Player1Turn(board);
      else:
        ConstBoard(board);
        Player2Turn(board);

  x=analyzeboard(board);
  if(x==0):
    ConstBoard(board);
    print("Draw");
  elif(x==-1):
    ConstBoard(board);
    print("Player 1 won");
  else:
    ConstBoard(board);
    print("Player2 won");

if __name__ == "__main__":