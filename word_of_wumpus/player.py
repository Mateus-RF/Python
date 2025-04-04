class Player:
    ranking = {"easy": {}, "medium": {}, "hard": {}}

    def __init__(self, m: dict, nome: str, condicao: str):
        self._hunter = [1, 1]
        self._score = 0
        self._nome_player = nome
        self._map = m
        self._condition = condicao
        self._aim = ('x', '+')
        self.wumpus_position = () 
        self.has_gold = False


    def shoot_arrow(self):
        x, y = self._hunter
        direction, sign = self._aim
        
        step_x, step_y = (1, 0) if direction == 'x' and sign == '+' else \
                        (-1, 0) if direction == 'x' else \
                        (0, -1) if direction == 'y' and sign == '+' else \
                        (0, 1) if direction == 'y' and sign == '-' else (0, 0)

    
        while True:
            x += step_x
            y += step_y
           

            if not (1 <= x < self._map.grid_size and 1 <= y < self._map.grid_size):
                return "Sua flecha errou completamente e se perdeu... 🏹❌"

            if (x, y) in self._map._object_map:
                objeto = self._map._object_map[(x, y)]

                if "🧌" in objeto:
                   
                    objeto.remove("🧌")
                    objeto.append("💀")
                    self._score += 100
                    self.wumpus_position = (x, y)
                    self.update_ranking()
                    return "Sua flecha acerta mortalmente o Wumpus! 💀"

                elif "🕳️" in objeto:
                    return "Sua flecha caiu em um buraco e desapareceu no abismo... 🕳️🏹"

                elif "💰" in objeto:
                    return "Sua flecha atingiu o tesouro e quebrou! 🎯💰"

                else:
                    return "Sua flecha acertou uma parede e quebrou! O Wumpus sentiu sua intenção e move-se🏹❌"
    
    
    def show_aim(self) -> str:
        match self._aim:
            case ('x', '-'):
                return '⬅️'
            case ('x', '+'):
                return '➡️'
            case ('y', '+'):
                return '⬆️'
            case ('y', '-'):
                return '⬇️'


    def walk_map(self, key :str) -> None:

        

        if key == b'a' and self._hunter[0] > 1:
            if self._aim != ('x', '-'): 
              self._aim = ('x', '-')
            else: 
              self._hunter[0] -= 1
        elif key == b'd' and self._hunter[0] < self._map.grid_size - 1:
            if self._aim != ('x', '+'):
              self._aim = ('x', '+')
            else:
              self._hunter[0] += 1
        elif key == b'w' and self._hunter[1] > 1:
            if self._aim != ('y', '+'):
                self._aim = ('y', '+')
            else:
                self._hunter[1] -= 1
        elif key == b's' and self._hunter[1] < self._map.grid_size - 1:
            if self._aim != ('y', '-'):
              self._aim = ('y', '-')
            else: 
              self._hunter[1] += 1


    def update_ranking(self) -> None:
        if self._condition in self.ranking:
          if self._nome_player in self.ranking[self._condition]:
              self.ranking[self._condition][self._nome_player] += self._score
          else:
              self.ranking[self._condition][self._nome_player] = self._score  
          

    @staticmethod
    def show_ranking(condition: str) -> None:
        if condition in Player.ranking:
            print('RANKING ' + condition.upper() + '\n')
            for player, value in Player.ranking[condition].items():
                print(f'Player: {player} | Pontuação: {value}')


    def set_score(self):
        self._score += 100

    
    def check_win_condition(self) -> bool:
        if not self.has_gold:
            ouro_no_mapa = any("💰" in objetos for objetos in self._map._object_map.values())
            
            if not ouro_no_mapa:
                self.set_score()
                self.update_ranking()
                self.has_gold = True

        if self.has_gold and self.wumpus_position and tuple(self._hunter) == (1, 1):
            print("\n🎉 PARABÉNS! Você matou o Wumpus e pegou o ouro! 🏆")
            return True
        
        return False

