VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
   while True:
       color = input()
       if color == 'quit':
           print("bye")
           break
       if color in VALID_COLORS: 
           print(color.lower())
       elif color != VALID_COLORS:
           print("Not a valid color")
           print('bye')
       else:
           continue
       pass