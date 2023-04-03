class Player():
    def __init__(self, name):
        self.name = name.title()
        self.num_of_games = 0
        self.wins = 0
        self.rock_count = 0
        self.scissors_count = 0
        self.paper_count = 0
        self.rock_ratio = 0
        self.scissors_ratio = 0
        self.paper_ratio = 0
        self.player_type = ""

    def __repr__(self):
        return "The players name is " + self.name



class Game():
    def __init__(self, name):
        self.name = name.title()
        self.games = 0
        self.wins = 0

    def __repr__(self):
        return "The players name is " + self.name


# TEST

player1 = Player("Steffen")

print(player1.num_of_games)
print(player1.rock_count)
print(player1.rock_ratio)
