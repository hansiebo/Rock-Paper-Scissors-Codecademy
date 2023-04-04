import classes as cl

commands = {"Help": "\n" + "COMMANDS" + "\n"+ "\n"
                    "Help - to see this list of commands" + "\n"
                    "Active - to see the active player" + "\n"
                    "Switch - to change the active player" + "\n"
                    "New - to add another player" + "\n"
                    "Rename - to rename the active player" + "\n"
                    "Players - to get an overview of all players" + "\n"
                    "Play - to initiate a new game and challenge another player" + "\n",
        "Active": "\n" + "newplayer" + "\n",
        "Switch": "\n" + "tbd" + "\n",
        "New": "\n" + "tbdd" + "\n",
        "Rename": "\n" + "tbddd" + "\n",
        "Players": "\n" + "tb" + "\n",
        "Play": "\n" + "Starting game" + "\n"
        }

def check_for_commands(entry):
  entry = str(entry).title()
  while entry in commands:
    print(commands[entry])
    entry = str(input()).title()

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
#entry = input("First, we need to create our first player" + "\n")
#if key in commands:
#  print(commands[key])


# 3. INITIATE GAME


# 4. PLAY