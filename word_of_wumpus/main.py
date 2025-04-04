from mapa import Map
from player import Player
import msvcrt
import os

def main():
    
    os.system('cls')
    print("Bem-vindo ao Mundo de Wumpus!\n")
    while True:
        cont = 1
        print('\nWord of Wumpus\n'+
              '\nJogar - Press Enter\n'+
              'Ranking - Press R\n'+
              'Sair - Press ESC')
        key = msvcrt.getch().lower()
        if key == b'\r':
            os.system('cls')
            while True:
                print("Escolha a dificuldade:\n"+
                "1 - Facil\n"+
                "2 - Medio\n"+
                "3 - Dificil")
                numero = input("Digite o Numero: ")
                if numero == '1':
                    level = 'easy'
                    break
                elif numero == '2':
                    level = 'medium'
                    break
                elif numero == '3':
                    level = 'hard'
                    break
                else:
                    print('Opção Invalida!!!')


            game_map = Map(level)
            game_map.difficulty_map()

            nome = input("Digite seu nome: ")
            player = Player(game_map, nome, game_map.condition)
            game_map.set_player(player)

            print("\nO jogo começou!.\n")
            shot_attempt = ''
            
            while True:
                text_temp = ''
                os.system('cls')
                print("Use WASD para se mover, F para atirar, e ESC para sair.")
                print("Direção da mira: " + player.show_aim())
                print(shot_attempt)
                shot_attempt = ''
                print(text_temp)
                print(player._map.verify_perception(tuple(player._hunter)))
                print("\n" + game_map.show_map(tuple(player._hunter)))

                key = msvcrt.getch().lower()
                if key == b'\x1b':
                    print("\n\nSaindo do jogo...")
                    break
                elif key == b'e':
                    if "💰" in game_map._object_map.get(tuple(player._hunter), []):
                        game_map._object_map[tuple(player._hunter)].remove("💰")
                        player.has_gold = True
                elif key == b'f':
                    if cont != 0:
                        shot_attempt = player.shoot_arrow()
                        cont = 0

                        if shot_attempt == "Sua flecha acerta mortalmente o Wumpus! 💀":
                            game_map.delete_sensation_wumpus(tuple(player.wumpus_position))
                            print(player._map.verify_perception(tuple(player._hunter)))
                    else:
                        text_temp = "Você já usou sua ultima flecha..."

                elif key in [b'w', b'a', b's', b'd']:  # Movimento
                    player.walk_map(key)
                    if player.check_win_condition():
                        break  
                
                
                
                resultado = player._map.verify_perception(tuple(player._hunter))
                if resultado and ("morreu" in resultado or "caiu" in resultado):
                    print(resultado)
                    break 
                

            print("Fim de jogo!")
        elif key == b'r':
            os.system('cls')
            while True:
                print("Escolha o ranking:\n"+
                    "1 - Facil\n"+
                    "2 - Medio\n"+
                    "3 - Dificil")
                numero = input("Digite o Numero: ")
                    
                if numero in ['1', '2', '3']:
                    level = {'1': 'easy', '2': 'medium', '3': 'hard'}[numero]
                    Player.show_ranking(level)
                    break
              
            
        elif key == b'\x1b':
            print('Saindo do jogo...')
            break

if __name__ == "__main__":
    main()
