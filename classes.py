class Player():
    number_of_players = 0

    def __init__(self, name):
        self.name = name.title()
        self.number_of_games = 0
        self.wins = 0
        self.rock_count = 0
        self.scissors_count = 0
        self.paper_count = 0
        self.rock_ratio = 0
        self.scissors_ratio = 0
        self.paper_ratio = 0
        self.player_type = "Noob"
        self.player_id = Player.number_of_players + 1
        Player.number_of_players += 1

    def __repr__(self):
        return "The players name is " + self.name
    
    def update_after_game(self, win, choice):
        pass


    def set_name(self, name):
        self.name = name.title()
        print("Name of player with ID " + str(self.player_id) + " has been changed to " + self.name + ".")

    def get_name(self):
        print("getter message called")
        return self.name

    def get_number_of_games(self):
        print("getter message called")
        return self.number_of_games

    def get_wins(self):
        print("getter message called")
        return self.wins

    def get_rock_count(self):
        print("getter message called")
        return self.rock_count

    def get_scissors_count(self):
        print("getter message called")
        return self.scissors_count

    def get_paper_count(self):
        print("getter message called")
        return self.paper_count

    def get_rock_ratio(self):
        print("getter message called")
        return self.rock_ratio

    def get_scissors_ratio(self):
        print("getter message called")
        return self.scissors_ratio

    def get_paper_ratio(self):
        print("getter message called")
        return self.paper_ratio

    def get_player_type(self):
        print("getter message called")
        return self.player_type

    def get_player_id(self):
        print("getter message called")
        return self.player_id







class Game():
    def __init__(self, name):
        self.name = name.title()
        self.games = 0
        self.wins = 0

    def __repr__(self):
        return "The players name is " + self.name


# TEST

# player1 = Player("Steffen")

# print(player1.number_of_games)
# print(player1.rock_count)
# print(player1.rock_ratio)

### ++++++


# player1.set_name("Julia")