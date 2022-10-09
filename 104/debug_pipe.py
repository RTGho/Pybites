
# MESSAGE = """Hello world!
# We hope that you are learning a lot of Python.
# Have fun with our Bites of Py.
# Keep calm and code in Python!
# Become a PyBites ninja!"""

MESSAGE = input('Sentence: ')

def split_in_columns(message=MESSAGE):
   x = list(MESSAGE) 
   MESSAGE.split('\n')
   print(x)
   columns = '|'.join(x)
   print(columns)
   return columns 
   

   pass


test = split_in_columns(MESSAGE)

print(test)