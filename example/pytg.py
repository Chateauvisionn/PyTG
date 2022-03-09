import time
import sys
import os
from os.path import isfile
from shutil import rmtree, copyfile


try:
  # project management
  if sys.argv[1] == "project":

    # create a project
    if sys.argv[2] == "create":

      try:
        # game folder
        print(f"Creating {sys.argv[3]} folder")
        os.mkdir(sys.argv[3])
        # main.py
        print(f"Creating {sys.argv[3]}/main.py")
        with open(f"{sys.argv[3]}/main.py", "w") as mpy:
          mpy.write("from pytg import *\nfrom config import Config\n\ndef game():\n  # game script\n pass\n\nif __name__ == '__main__':\n  game()")
        # config.py
        print(f"Creating {sys.argv[3]}/config.py")
        with open(f"{sys.argv[3]}/config.py", "w") as cpy:
          cpy.write("class Config():\n # config class that you can import in main.py\n pass")
        # saves
        os.mkdir(f"{sys.argv[3]}/saves")
        print(f"Creating {sys.argv[3]}/saves/chars.txt")
        with open(f"{sys.argv[3]}/saves/chars.txt", "w") as ct:
          ct.write("[]")

        # module
        copyfile("pytg.py", f"{sys.argv[3]}/pytg.py")
        print("Project created")

      except FileExistsError:
        print("Error: This project already exist.")
    
    # delete a project 
    if sys.argv[2] == "delete":

      try:
        rmtree(sys.argv[3])
        print("Project deleted")

      except FileNotFoundError:
        print("Error: This project doesn't exist.")
    
    # rename
    if sys.argv[2] == "rename":
      try:
        os.rename(sys.argv[3], sys.argv[4])
      except:
        print("This project doesn't exist.")

  # verify the installation
  if sys.argv[1] == "verify":
    if not os.path.isfile("__init__.py"):
      print("__init__.py is missing!")
    else:
      print("Everything is good!")
except IndexError:
  import os.path
  if os.path.isfile("help.txt"):
    os.system("cat help.txt")
  else:
      pass

chars = []

# créer un personnage
def crChar(name):
  chars.append(name)
  strChars = str(chars)
  with open("chars.txt", "w") as f:
    f.write(strChars)

# supprimer tout les personnages
def delAllChars():
  chars.remove()

# faire un choix
def choice(o1,cons1, o2=None, cons2=None):
  if isinstance(cons1, str):
    print(cons1)
  else:
    cons1
  if isinstance(cons2, str):
    print(cons2)
  else:
    cons2
  print(o1)
  print(o2)
  ch = True
  while ch:
    c = input("Choose: ")
    if c == o1:
      cons1
      ch = False
    elif c == o2:
      cons2
      ch = False
    else:
      print('Invalid choice')

# dialogue
def dialog(char, text):
  print(char,":", text)
