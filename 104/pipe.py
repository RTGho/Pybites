from turtle import clear


MESSAGE = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=MESSAGE):
   x = (MESSAGE.split('\n'))
   columns = '|'.join(x)
   return columns 
   

   pass


test = split_in_columns(MESSAGE)

print(test)
