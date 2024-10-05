import random
import os


def graphics(show):  #initializing player's board
  for i in range(10):
    if i==0:
      print("  A B C D E F G H I J\n") 
    print(f"{i}[{show[i][0]} {show[i][1]} {show[i][2]} {show[i][3]} {show[i][4]} {show[i][5]} {show[i][6]} {show[i][7]} {show[i][8]} {show[i][9]}]\n")
    
def win_lose(l):
  P_C=0
  for i in range(5):
    for j in range(ship_size[i]):
      if l[i][j]=='0':
        P_C+=1
  if P_C==17: 
    return 1
  return 0

def check_comp_repeat_ship(a,b,ship_size,ship_no,comp_ship_info):
  for i in range(ship_size[ship_no]):
    for j in range(ship_no):
      for k in range(ship_size[j]):
        if x+(a*i) ==comp_ship_info[j][k][0] and y+(b*i) ==comp_ship_info[j][k][1]:
          return 1
  return 0
  
  

print("Your main Board:")
player_board = [['-' for i in range(10)] for j in range(10)]
attack_board = [["-" for i in range(10)] for j in range(10)]
ship_size =  [5,4,3,3,2]
ship_banner=['%','@','#','*','&']
comp_ship_info=[[[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]],[[-1,-1],[-1,-1],[-1,-1],[-1,-1]],[[-1,-1],[-1,-1],[-1,-1]],[[-1,-1],[-1,-1],[-1,-1]],[[-1,-1],[-1,-1]]]


  
ship_no=0

while 1:
  a=0
  b=0
  if ship_no==0:
    key=0
  else:
    key=1
  x=random.randint(0,9)
  y=random.randint(0,9)
  while key:
    x=random.randint(0,9)
    y=random.randint(0,9)
    key=0
    for i in range(5):
      for j in range(ship_size[i]):
        if x ==comp_ship_info[i][j][0] or y==comp_ship_info[i][j][1]:
          key=1
          break
      if key:
        break
    
    
  position = random.choice(["Horizontal", "Vertical"])
  
  # for j in range(ship_size[ship_no]):
  #   if position == "Horizontal":
  #     if y+ship_size[ship_no]>9:
  #       # attack_board[x][y-j]=ship_banner[ship_no]#should be deleted after testing
  #       comp_ship_info[ship_no].append([[x],[y-j]])
  #       a=0
  #       b=-1
  #     else:
  #       # attack_board[x][y+j]=ship_banner[ship_no]#should be deleted after testing
  #       comp_ship_info[ship_no].append([[x],[y+j]])
  #       a=0
  #       b=1
  #   else:
  #     if x+ship_size[ship_no]>9:
  #       # attack_board[x-j][y]=ship_banner[ship_no]#should be deleted after testing
  #       comp_ship_info[ship_no].append([[x-j],[y]])
  #       a=-1
  #       b=0
  #     else:
  #       # attack_board[x+ship_no][y]=ship_banner[ship_no]#should be deleted after testing
  #       comp_ship_info[ship_no].append([[x+j],[y]])
  #       a=1
  #       b=0
  
  for j in range(ship_size[ship_no]):
    if position == "Horizontal":
        if y + ship_size[ship_no] > 9:
            comp_ship_info[ship_no][j]=[x, y - j]
            a = 0
            b = -1
        else:
            comp_ship_info[ship_no][j]=[x, y + j]
            a = 0
            b = 1
    else:
        if x + ship_size[ship_no] > 9:
            comp_ship_info[ship_no][j]=[x - j, y]
            a = -1
            b = 0
        else:
            comp_ship_info[ship_no][j]=[x + j, y]
            a = 1
            b = 0
  
  temp=comp_ship_info.pop(ship_no)
  comp_ship_info.insert(ship_no, [])
  
  if check_comp_repeat_ship(a,b,ship_size,ship_no,comp_ship_info): 
    continue
  comp_ship_info.pop(ship_no)
  comp_ship_info.insert(ship_no,temp)
  
  ship_no+=1
 

  

player_ship_info=[[],[],[],[],[]]

no=0
# Setting up the player's board
while 1:
  graphics(player_board)
  print(f"Enter the coordinates of the no.{no+1} ship\nIt is {ship_size[no]} space long")
  
  # a=1
  # while a:
  #   x = int(input("Enter the x-coordinate for the ship head(0-9):"))
  #   y = int(input("Enter the y-coordinate for the ship head(0-9):"))
  #   if (x>9 or x<0 or y>9 or y<0): #check whether the input is out of range
  #     print("The input range should be 0 to 9")
  #   else:
  #     a=0  #execute the loop

  # b=1
  # while b:
  #   pos1=input("horizontal/vertical? (hor/ver):")
  #   if (pos1!=hor or pos!=ver):
  #     print("Please input again!")
  #   else:
  #     b=0
  # pos2 = input("left/right? :") if pos1 == "hor" else input("up/down? :")
  
  for i in range(ship_size[no]):
    if pos1=="hor" :
      if pos2=="right": 
        player_board[x][y+i]=ship_banner[no]
        player_ship_info[i].append([[x],[y+i]])
      else:
        player_board[x][y-i]=ship_banner[no]
        player_ship_info[i].append([[x],[y-i]])
    else:
      if pos2=="up":
        player_board[x-i][y]=ship_banner[no]
        player_ship_info[i].append([[x-i],[y]])
      else:  
        player_board[x+i][y]=ship_banner[no]
        player_ship_info[i].append([[x+i],[y]])
  
    
  os.system('cls' if os.name == 'nt' else 'clear')
  no+=1
  if no==5:
    break
  


# main game, if hit successfully -> "x" ,else->"."

while 1:

  #get the player's move
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Enemy's board:")
  graphics(attack_board) 
  print("Player's board:")
  graphics(player_board)
  print("Player's turn:\nWhich position would u like to attack? ")
  # c=1
  # while c:
  #   player_attack_x=int(input("x-coordinate?(0-9):"))
  #   player_attack_y=int(input("y-coordinate?(0-9):"))
  #   if (player_attack_x>9 or player_attack_x<0 or player_attack_y>9 or player_attack_y<0): 
  #   print("The input range should be 0 to 9")
  # else:
  #   c=1 
    
  key=0
  for i in range(5):
    for j in range(ship_size[i]):
      if player_attack_x==comp_ship_info[i][j][0] and player_attack_y==comp_ship_info[i][j][1]:
        os.system('cls')
        comp_ship_info[i][j]='0'
        print("HIT!!!")
        attack_board[player_attack_x][player_attack_y]="x"
        key=1
        break
    if key:
      break
  if key==0:
    print("MISSED!!!")
    attack_board[player_attack_x][player_attack_y]="."
  
  com_l=0
  #win define
  for i in range(5):
    for j in range(ship_size[i]):
      if comp_ship_info[i][j]=='0':
        com_l+=1
  
  if comp_l==17: 
    print("YOU WIN!!")
    break
  
  # if win_lose(comp_ship_info):
  #   print("YOU WiN!!")
  #   break
    
  
  
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Enemy's board:")
  graphics(attack_board) 
  print("Player's board:")
  graphics(player_board)
  print("Enemy's turn:")
  while 1:
    enemy_attack_x=random.randint(0,9)
    enemy_attack_y=random.randint(0,9)
    if player_board[enemy_attack_x][enemy_attack_y]!='x':
      break
  key=0    
  for i in range(5):
    for j in range(ship_size[i]):
      if enemy_attack_x==player_ship_info[i][j][0] and enemy_attack_y==comp_ship_info[i][j][1]:
        player_ship_info[i][j]='0'
        print("HIT!!!")
        key=1
        break
    if key:
      break
    
  if key==0:
    print("MISSED!!!")
    player_board[enemy_attack_x][enemy_attack_y]="x"
  
  
  player_l=0
  #win define
  for i in range(5):
    for j in range(ship_size[i]):
      if player_ship_info[i][j]=='0':
        player_l+=1
  if player_l==17: 
    print("YOU LOSE!!")
    break
  
  
  
  # if win_lose(player_ship_info):
  #   print("YOU LOSE!!")
  #   break
      
  
  
    
  














