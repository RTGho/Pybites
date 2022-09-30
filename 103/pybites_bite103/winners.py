GAME_STATS = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won):
   for name, num in games_won.items(): 
      if num == 1: 
         print(f"{name} has won {num} game")
      else:
         print(f"{name} has won {num} games")
      
   


print_game_stats(GAME_STATS)