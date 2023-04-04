import classes as cl

# Initialize Dictionaries
players = {}

games = {}

commands = {}

# Functions
def check_for_commands(entry):
  entry = str(entry).title()
  while entry in commands:
    print(commands[entry])
    entry = str(input()).title()

def add_player():
  name = input("What is the name of player number {id}? ".format(id=cl.Player.number_of_players + 1))
#  check_for_commands(name)
  players[name] = cl.Player(name)
  print("\n" + "You succesfully added the following player:" + "\n")
  print(players[name])
  print("")
  entry = input("Do you want to add another player? (y/n)")
  check_for_commands(entry)
  if entry == "y":
    add_player()
  elif entry == "n":
    entry = input("alright! let's move on!")
    check_for_commands(entry)

# Dictionaries tbd
commands["Help"]= ("\n" + "COMMANDS" + "\n"+ "\n"
                  "Help - to see this list of commands" + "\n"
                  "Active - to see the active player" + "\n"
                  "Switch - to change the active player" + "\n"
                  "New - to add another player" + "\n"
                  "Rename - to rename the active player" + "\n"
                  "Players - to get an overview of all players" + "\n"
                  "Play - to initiate a new game and challenge another player" + "\n")
commands["Active"] = "\n" + "active player" + "\n"
commands["Switch"] = "\n" + "switch" + "\n"
commands["New"] = add_player
commands["Rename"] = "\n" + "tbddd" + "\n"
commands["Players"] = "\n" + "tb" + "\n"
commands["Play"] = "\n" + "Starting game" + "\n"


# 1. INTRO | WELCOME
print("\n"
      "===================================================" + "\n"
      "WELCOME TO ROCK PAPER SCISSORS - THE TERMINAL GAME!" + "\n"
      "===================================================" + "\n")

entry = input("In order to move to the next step anywhere in the game, either answer the question or hit 'Enter'." + "\n")
check_for_commands(entry)

entry = input("Well done!" + "\n" + "\n" + 
              "The following commands work everywhere inside the game: " + "\n"  + "\n"
              "Help - to see this list of commands" + "\n"
              "Active - to see the active player" + "\n"
              "Switch - to change the active player" + "\n"
              "New - to add another player" + "\n"
              "Rename - to rename the active player" + "\n"
              "Players - to get an overview of all players" + "\n"
              "Play - to initiate a new game and challenge another player" + "\n" + "\n"
              "Hit 'Enter' to continue." + "\n" + "\n")
check_for_commands(entry)

entry = input("Type 'GO' to get started! " + "\n" + "\n")
check_for_commands(entry)

while (entry.upper() != "GO"):
  entry = input("\n" + "Awww, you don't want to play? That's ok. But if you do want to play, type 'GO' to get started." + "\n" + "\n")
  check_for_commands(entry)

entry = input("\n" + "Awesome! Let's get started!" + "\n")
check_for_commands(entry)

  
# 2. CREATE PLAYERS
entry = input("You can play 'ROCK PAPER SCISSORS' either against a friend or the computer." + "\n")
check_for_commands(entry)


add_player()


input("FIN")


# 3. INITIATE GAME


# 4. PLAY