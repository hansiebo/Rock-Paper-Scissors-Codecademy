import classes as cl

commands = {"Help": "\n" + "COMMANDS" + "\n"+ "\n"
                    "Help - to see this list of commands" + "\n"
                    "Active - to see the active player" + "\n"
                    "Switch - to change the active player" + "\n"
                    "New - to add another player" + "\n"
                    "Rename - to rename the active player" + "\n"
                    "Players - to get an overview of all players" + "\n"
                    "Play - to initiate a new game and challenge another player" + "\n" + "\n",
        "Active": "newplayer",
        "Switch": "tbd",
        "New": "tbdd",
        "Rename": "tbddd",
        "Players": "tb",
        "Play": "Starting game"
        }

def inputs(key):
  if key in commands:
    print(commands[key])
  else:
    print("NaN")


# 1. INTRO | WELCOME
print("Welcome to Rock Paper Scissors - The Terminal Game!"+ "\n" + "\n")

input("All throughout the game, in order to move to the next step, either answer the question or hit 'Enter' to move to the next text step." + "\n")

key = input("At any point in the game, you can type any of the following commands: " + "\n"  + "\n"
      "Help - to see this list of commands" + "\n"
      "Active - to see the active player" + "\n"
      "Switch - to change the active player" + "\n"
      "New - to add another player" + "\n"
      "Rename - to rename the active player" + "\n"
      "Players - to get an overview of all players" + "\n"
      "Play - to initiate a new game and challenge another player" + "\n" + "\n") 

inputs(key)


key = input("Type 'GO' to get started! " + "\n" + "\n")
if key in commands:
  print(commands[key])
while (key != "GO"):
  key = input("Awww, you don't want to play? That's ok. But if you do want to play, type 'GO' to get started." + "\n" + "\n")

key = input("Awesome! Let's get started!" + "\n")
if key in commands:
  print(commands[key])


key = input("First, we need to create our first player" + "\n")
if key in commands:
  print(commands[key])

###

key = input("test 2")
if key in dict:
  print(dict[key])
else: 
   print("a")

   

# 2. CREATE PLAYERS


# 3. INITIATE GAME


# 4. PLAY