from random import randint
from player import Player
class Map:

  def __init__(self, level: str):
    self.condition = level
    self._object_map: dict = {}
    self._phantom_map: dict = {}
    self.grid_size = 0
    self.player = None
    

    if self.condition == 'easy':
      self.grid_size = 5
    elif self.condition == 'medium':
      self.grid_size = 7
    elif self.condition == 'hard':
      self.grid_size = 11


  def difficulty_map(self):
    for x in range(1,self.grid_size):
      for y in range(1, self.grid_size):
        self._phantom_map[(x, y)] = '❓'


    for x in range(1,self.grid_size):
      for y in range(1, self.grid_size):
        self._object_map[(x, y)] = []
    self.obstacle()


  def obstacle(self):
    lista = ['🧌', '💰']

    if self.condition == 'easy':
        lista += ['🕳️'] * 3
    elif self.condition == 'medium':
        lista += ['🕳️'] * 4
    elif self.condition == 'hard':
        lista += ['🕳️'] * 5

    self.place_obstacles(lista)
    self.place_sensations()


  def place_obstacles(self, list_obstacles : list) -> None:
                for obstacle in list_obstacles:
                  while True:
                    x = randint(2, self.grid_size -1)
                    y = randint(2, self.grid_size -1)

                    if self._object_map.get((x, y)) == []:
                      self._object_map[(x, y)].append(obstacle)
                      break



  def ramdom_wumpus(self):
     while True:
      x = randint(2, self.grid_size -1)
      y = randint(2, self.grid_size -1)

      if self._object_map.get((x, y)) == '🧌':
        self._object_map[(x, y)] = ""
        break


  def delete_sensation_wumpus(self, player_position : tuple):
     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
     x, y = player_position
     for dx, dy in directions:

      adj_x, adj_y = x + dx, y + dy

      if (adj_x, adj_y) in self._object_map and '💤' in self._object_map[(adj_x, adj_y)]:
          self._object_map[(adj_x, adj_y)].remove('💤')
        


  def place_sensations(self) -> None:

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for (x, y), value in self._object_map.items():
          if '🧌' in value:
              sensation = '💤'
          elif '🕳️' in value:
              sensation = '☁️'
          else:
              continue

          for dx, dy in directions:

              adj_x, adj_y = x + dx, y + dy

              if (adj_x, adj_y) in self._object_map:
                  self._object_map[(adj_x, adj_y)].append(sensation)


  def verify_perception(self, player_position: tuple) -> str:
    objetos = self._object_map.get(player_position, [])
    text = ''
    if objetos:
        for objeto in objetos:
            if objeto == "🧌":
                return "Você deu de cara com o Wumpus e morreu miseravelmente!"
            elif objeto == "🕳️":
                return "Você caiu em um abismo e foi de F!\n"
            elif objeto == "💰":
                self.player.has_gold = True
                text += "Você encontrou o tesouro, meus parabéns!!! 🎉💰\n  Press E para pegar o ouro\n"
            elif objeto == "💤":
                text += "Você sente um cheiro horrível... Algo perigoso está por perto!\n"
            elif objeto == "☁️":
                text += "Você sente uma leve brisa... Pode haver um abismo próximo.\n"
            elif objeto == "💀":
               text += "\nVocê vê a carcaça de wumpus, mas decide não fazer nada..."
    
    return text.strip() 



  def show_map(self, player_position: tuple) -> str:
    text = ''
    for y in range(1, self.grid_size):
        for x in range(1, self.grid_size):
            if (x, y) == player_position:
                text += '🥷🏽'
            else:
                text += self._phantom_map.get((x, y), ' ') + ' '
        text += '\n'
    return text
  

  def set_player(self, player: Player)-> None:
     self.player = player