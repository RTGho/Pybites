GAME_STATS = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won): # my solution
   for name, num in games_won.items(): 
      if num == 1: 
         print(f"{name} has won {num} game")
      else:
         print(f"{name} has won {num} games")
      
   
def print_game_stats_bob(games_won): # bob solution
   for name, score in games_won.items(): 
      game = 'game' if score == 1 else 'games'
      print(f"{name} has won {score} {game}")



# print_game_stats(GAME_STATS)
print_game_stats_bob(GAME_STATS)
