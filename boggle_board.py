import string
import random
from turtle import pos

class BoggleBoard:
  # we initialize a 2d array for the dice and the board with the corresponding size
  def __init__(self, die=[["_"]*6 for i in range(16)], board=[["_"]*4 for i in range(4)]):
    self.die = die
    self.board = board

  # we fill every subarray with a random letter
  def create_die(self):
    abc = string.ascii_uppercase
    for i,k in enumerate(self.die):
      for j,p in enumerate(k):
        rand = random.choice(abc)
        if rand == 'Q':
          self.die[i][j] = 'Qu'
        else:
          self.die[i][j] = rand
    return self.die

  # we fill every subarray with a random letter from an incrementing index, calling a different die every time
  def shake(self):
    abc = string.ascii_uppercase
    side = 0
    for i,k in enumerate(self.board):
      for j,p in enumerate(k):
        rand = random.choice(self.die[side])
        side += 1
        if rand == 'Q':
          self.board[i][j] = 'Qu'
        else:
          self.board[i][j] = rand
    for i in self.board:
      line_format= '{:<2} {:<2} {:<2} {:<2}'.format(i[0],i[1],i[2],i[3])
      print(line_format)

  def _is_neighbour(self,a,b,a1, b1):
    possible_neighbours= [(a-1,b), (a+1,b), (a,b-1), (a,b+1), (a-1,b-1), (a-1,b+1), (a+1,b-1), (a+1,b+1)]
    neighbours = []
    for i in possible_neighbours:
      if i[0] < len(self.board[0]) and i[0] >= 0:
        if i[1] < len(self.board) and i[1] >=0:
          neighbours.append(i)
    return (a1,b1) in possible_neighbours
  
  def include_char(self,char):
    for i, die in enumerate(self.board):
      for j,side in enumerate(self.board[i]):
        if char == side:
          return (i,j)
    return False

  def include_word(self,target):
    x = 1
    pos = self.include_char(target[x])
    pos1 = self.include_char(target[0])
    while x < len(target):
      if pos1:
        self._is_neighbour(pos[0],pos[1],)
      

    # if target_list[0] not in self.board:
    #   return False
    # for i in range(1,len(target_list)):
    #   if self._is_neighbour()
    




game = BoggleBoard()
# print(game.board)
print(game.create_die())
print("------------------------------------")
game.shake()
game.include_word("PLG")




