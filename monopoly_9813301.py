import random

class MonopolyState:
    def __init__(self, cash, properties_owned, position, turn):
        self.cash = cash
        self.properties_owned = properties_owned
        self.position = position
        self.turn = turn
        self.in_jail = False
        self.get_out_of_jail_free = False

class MonopolyGame:
    def __init__(self):
        self.board = ["Go", "Mediterranean Avenue", "Community Chest", "Baltic Avenue",
                      "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance",
                      "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Place",
                      "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad",
                      "St. James Place", "Community Chest", "Tennessee Avenue", "New York Avenue",
                      "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue",
                      "B. & O. Railroad", "Atlantic Avenue", "Ventnor Avenue", "Water Works",
                      "Marvin Gardens", "Go To Jail", "Pacific Avenue", "North Carolina Avenue",
                      "Community Chest", "Pennsylvania Avenue", "Short Line", "Chance", "Park Place",
                      "Luxury Tax", "Boardwalk"]
        
        self.property_prices = [0, 60, 0, 60, -200, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200,
                                180, 0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, -50, 300,
                                300, 0, 320, 200, 0, 350, 0, 400]
        
        self.property_rents = [0, 15, 0, 15, 0, 50, 25, 0, 25, 30, 0 , 35, 40, 35, 40, 50, 45, 0, 45,
                                50, 0, 55, 0, 55, 60, 50, 65, 65, 40, 70, 0, 75, 75, 0, 80, 50, 0, 90, 0, 100]
        
        self.owner = [0 for _ in range(len(self.board))]
        
        self.chance_cards = ["Advance to Go", "Go to Jail", "Advance to Illinois Avenue",
                             "Advance to St. Charles Place", "Advance to the nearest Utility",
                             "Advance to the nearest Railroad", "Bank pays you dividend of $50",
                             "Get out of Jail Free"]
        
        self.community_chest_cards = ["Advance to Go", "Bank error in your favor",
                                      "Get out of Jail Free", "Go to Jail", "Grand Opera Night",
                                      "Holiday Fund matures", "It's your birthday!",
                                      "Life insurance matures", "From sale of stock, you get $50"]
        
        self.num_players = 2
        self.current_player = 0
        self.players = [MonopolyState(1500, [], 0, 0) for _ in range(self.num_players)]
        self.is_game_over = False
        self.winner = 0
        
    def play_game(self):
        while not self.is_game_over:
            self.current_player = (self.current_player + 1) % self.num_players
            self.play_turn()
            self.players[self.current_player].turn += 1
        self.winner = (self.current_player + 1) % self.num_players
        
    def play_turn(self):
        player = self.players[self.current_player]
        roll = self.roll_dice()
        if player.in_jail:
            if roll == 6:
                player.in_jail = False
            else:
                return
        player.position = (player.position + roll) % len(self.board)
        
        if player.position == 30: # Go to Jail
            if player.get_out_of_jail_free:
                player.get_out_of_jail_free = False
                return
            player.position = 10
            player.in_jail = True
        
        elif player.position == 0: # Go
            player.cash += 200

        elif self.board[player.position] == "Community Chest":
            self.draw_community_chest_card(player)
            
        elif self.board[player.position] == "Chance":
            self.draw_chance_card(player)
            
        elif self.board[player.position] == "Income Tax":
            player.cash -= 200
        
        elif self.board[player.position] == "Luxury Tax":
            player.cash -= 100
        
        else :
            # here is expectimax turn to give us the best move
            move = expectimax(player, state, depth)
            make_move (move, state, player)

            # here i wrote a deterministic algorithm for play
            if self.board[player.position] not in player.properties_owned:
                if self.owner[player.position] == 0:
                    if player.cash < self.property_prices[player.position]:
                        self.is_game_over = True
                    else:
                        player.cash -= self.property_prices[player.position]
                        player.properties_owned.append(self.board[player.position])
                        self.owner[player.position] = self.current_player + 1
                else:
                    if player.cash < self.property_rents[player.position]:
                        self.is_game_over = True
                    else:
                        player.cash -= self.property_rents[player.position]
                        self.players[self.owner[player.position] - 1].cash += self.property_rents[player.position]
                        
                    
                        
                    player.properties_owned.append(self.board[player.position])
                    self.owner[player.position] = self.current_player + 1
                player.cash -= self.property_prices[player.position]
                player.properties_owned.append(self.board[player.position])
    
    def make_move():
        

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)
    
    def draw_community_chest_card(self, player):
        card = random.choice(self.community_chest_cards)
        if card == "Advance to Go":
            player.position = 0
        elif card == "Go to Jail":
            if player.get_out_of_jail_free:
                player.get_out_of_jail_free = False
                return
            player.position = 10
            player.in_jail = True
        elif card == "Get out of Jail Free":
            player.get_out_of_jail_free = True
        else:
            player.cash += 50

    def draw_chance_card(self, player):
        card = random.choice(self.chance_cards)
        if card == "Advance to Go":
            player.position = 0
        elif card == "Go to Jail":
            if player.get_out_of_jail_free:
                player.get_out_of_jail_free = False
                return
            player.position = 10
            player.in_jail = True
        elif card == "Get out of Jail Free":
            player.get_out_of_jail_free = True
        elif card == "Advance to Illinois Avenue":
            player.position = 24
        elif card == "Advance to St. Charles Place":
            player.position = 11
        elif card == "Advance to the nearest Utility":
            if player.position == 7:
                player.position = 12
            elif player.position == 22:
                player.position = 28
            else:
                player.position = 12
        elif card == "Advance to the nearest Railroad":
            if player.position == 7:
                player.position = 15
            elif player.position == 22:
                player.position = 25
            else:
                player.position = 5
        else:
            player.cash += 50

    
    def expectimax(player, state, depth):
        if depth == 0:
            return evaluation_function(player, state)

        if is_chance_node(state):
            return expectimax_chance_node(player, state, depth)
        else:
            return max(expectimax_max_node(player, state, depth), expectimax_min_node(player, state, depth))

    def expectimax_chance_node(player, state, depth):
        expected_value = 0
        for dice_roll in range(2, 13):
            probability = 1 / 36 if dice_roll == 7 else 1 / 18
            new_state = apply_dice_roll(state, player, dice_roll)
            expected_value += probability * expectimax(player, new_state, depth - 1)
        return expected_value

    def expectimax_max_node(player, state, depth):
        max_value = float('-inf')
        actions = get_possible_actions(player, state)
        for action in actions:
            new_state = apply_action(state, action)
            value = expectimax(player, new_state, depth - 1)
            max_value = max(max_value, value)
        return max_value

    def expectimax_min_node(player, state, depth):
        min_value = float('inf')
        actions = get_possible_actions(player, state)
        for action in actions:
            new_state = apply_action(state, action)
            value = expectimax(player, new_state, depth - 1)
            min_value = min(min_value, value)
        return min_value
    
    def get_possible_actions(self, player, state):
        action = []

    def evaluation_function(player, state):
        # Simple evaluation function that considers cash and the cost of properties
        sum = 0
        for i in player.property_owned:
         sum += property_prices[board.index(player.property_owned[i])] 
        return player.cash + 2*sum
    
    def is_chance_node(state):
        return state == "Chance"
    
    def apply_dice_roll(state, player, dice_roll):
        return player.position + dice_roll
    
    
    def apply_action(state, action):

        return new_state
    

# game UI
Game = MonopolyGame()
Game.play_game()
print('winner is', Game.winner)