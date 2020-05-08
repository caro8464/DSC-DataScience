# Controls the game play
class TicTacToe:
  def __init__(self):
    self.board = Board()
    self.player_x = Player("Madame X", "X", self.board)
    self.player_o = Player("Mister O", "O", self.board)
    self.current_player = self.player_x
    
  def play(self):
    while True:
      self.board.render()
      self.current_player.get_coordinates()
      if (self.check_game_over()):
        return 0
      self.switch_players()
      
  def check_game_over(self):
    if (self.check_victory() or self.check_draw()):
      return True
    else:
      return False
    
  def check_draw(self):
    if (self.board.is_draw()):
      print("\nDRAW!!!\nYou both lose!")
      
  def check_victory(self):
    if (self.board.is_victory()):
      print("\nWELL DONE %s\nYou Are The Winner!!!\n" % self.current_player)
      return True
    
  def switch_players(self):
    if (self.current_player == self.player_x):
      self.current_player = self.player_o
    else:
      self.current_player = self.player_x

# Manages all player-related functionality
class Player:
  def __init__(self, name, sign, board):
    self.name = name
    self.sign = sign
    self.board = board
  
  def __str__(self):
    return self.name
  
  def get_coordinates(self):
    while True:
      coordinates = input("please enter coordinates 0-2 , A-C eg. (0A)")
      
      if (self.validate_coordinates_format(coordinates)):
        if (self.board.place_sign(coordinates, self.sign)):
          break
        else:
          self.board.render
          print("\nYou can't place a stone upon another\nTry Again!")
      else:
        print("\nWrong coordinate format, '0A' to '2C' are possible\nTry Again!")

  def validate_coordinates_format(self, coordinates):
    length = len(coordinates) == 2
    number = int(coordinates[0]) in [0,1,2]
    letter = coordinates[1].upper() in ['A','B','C']
    if (length and number and letter):
      return True
    else:
      return False


# Maintains game board state
class Board:
  def __init__(self):
    self.board = [[None for x in range(3)] for x in range(3)]
    self.victor = ""
  def render(self):
    output = ""
    for row in self.board:
      output += ("|")
      for cell in row:
        if cell != None:
          output += (cell + "|")
        else:
          output += (" |")
      output += ("\n")
    print(output)
  def is_draw(self):
    counter = 9
    for row in self.board:
      for cell in row:
        if cell == None:
          counter -= 1
    return False if counter > 0 else True
  def place_sign(self, coordinates, sign):
    x = int(coordinates[0])
    y = ord(coordinates[1].upper()) - 65
    if (self.board[x][y] == None):
      self.board[x][y] = sign
    else:
      return False
    return True
  def is_victory(self):
    win = 0
    win += self.is_win_vertical()
    win += self.is_win_horizontal()
    win += self.is_win_diagonal()
    
    return True if win > 0 else False
  def is_win_diagonal(self):
    diagonal1 = [self.board[0][0],self.board[1][1], self.board[2][2]]
    diagonal2 = [self.board[0][2],self.board[1][1], self.board[2][0]]
    return 1 if self.all_the_same(diagonal1) or self.all_the_same(diagonal2) else 0
  def is_win_horizontal(self):
    horizontal1 = [self.board[0][0],self.board[1][0], self.board[2][0]]
    horizontal2 = [self.board[0][1],self.board[1][1], self.board[2][1]]
    horizontal3 = [self.board[0][2],self.board[1][2], self.board[2][2]]
    return 1 if self.all_the_same(horizontal1) or self.all_the_same(horizontal2) or self.all_the_same(horizontal3) else 0
  def is_win_vertical(self):
    vertical1 = [self.board[0][0],self.board[0][1], self.board[0][2]]
    vertical2 = [self.board[1][0],self.board[1][1], self.board[1][2]]
    vertical3 = [self.board[2][0],self.board[2][1], self.board[2][2]]
    return 1 if self.all_the_same(vertical1) or self.all_the_same(vertical2) or self.all_the_same(vertical3) else 0
  def all_the_same(self, elements):
   return False if not all(elements) else len(elements) < 1 or len(elements) == elements.count(elements[0])

def main():
  game = TicTacToe()
  game.play()

if __name__ == "__main__":
    main()