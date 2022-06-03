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

  def include_word(self,target):
    visited=set()
    

  def _get_neighbours(self,a,b):
    possible_neighbours= [(a-1,b), (a+1,b), (a,b-1), (a,b+1), (a-1,b-1), (a-1,b+1), (a+1,b-1), (a+1,b+1)]
    neighbours = []
    for i in possible_neighbours:
      if i[0] < len(self.board[0]) and i[0] >= 0:
        if i[1] < len(self.board) and i[1] >=0:
          neighbours.append(i)
    print(neighbours)
      
    




game = BoggleBoard()
# print(game.board)
print(game.create_die())
print("------------------------------------")
game.shake()
game.include_word("hi")

