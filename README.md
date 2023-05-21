# Monopoly_Game
This is a simple implementation of the monopoly game
## Introduction
Monopoly is a board game currently published by Haas Brothers. In this game, each participant moves through different houses with the help of dice and buys properties on the playing field and expands his business by buying a hotel. Players receive rent from their opponents to drive them into bankruptcy. There are also different ways to spend money in this game.
In this implementation, we have reviewed a simplified version of the game:
The number of players in this implementation is considered to be 2.
Movements such as mortgage and construction are not considered.
## Implementation procedure
First, a game round was implemented without the Expectimax algorithm:
The Monopolystate class was considered to define each state of the game. (In this class, different parameters considered for a game mode for a player, such as money, player property, player position on the board, player turn, whether the player is in jail or not, and having a get out of jail card)
The MonopolyGame class, in which all the necessary items were implemented:
Game board: a list of the names of all the game houses
Property Money: A list of money attributed to each property
Property Rentals: A list of rentals for each property
Homeowner: A list initialized with 0 for all houses, and during the game sees a value of 1 or 2 in its houses, corresponding to players 0 or 1.
Lucky cards: A list of lucky card names
Local cash register cards: A list of local cash register card names
Number of players
current player
player
Bowling is game over to determine whether or not one of the players goes bankrupt and ends the game
Winner to determine the winning number of the game
play game function: to change the player and perform the turn of each game
play turn function: to implement all the possible moves of the game and determine the assignment of real estate, position and money of each player after taking his turn
roll_dice function: to roll the dice
draw_community_chest_card function: to draw a card from the local chest and determine the player's Nickname and position afterwards
draw_chance_card function: to draw a card from the chance box and determine the player's chance card and its position afterwards

Now, by defining an object of the MonopolyGame class and calling the play_game function, the game will be played with two players and the winner will be determined. (We will see part of the code execution in this case in chapter 6)

The implementation was not completed and it is checked as far as the implementation is done:
In the continuation of the effort to add the Expectimax algorithm to the game:
Defining the expectimax function that uses our expected value function:
At depth 0, the value function returns the value per player and the current state.
Otherwise, if it is a chance node (a node other than the max and min node), the corresponding random algorithm will be called, and otherwise, the maximum node will call the maximum and minimum nodes.
The implementation of this algorithm is according to the common implementations available on the Internet.
get_possible_action function: which should take into account all possible movements, and this work was already implemented definitively within the play turn function, and I had a problem with the implementation in this section according to the expectimax algorithm.
Also, the apply_action function was defined to apply movement on the existing status and reach the new status, and the method of applying the movement on the status faced a problem.

According to the logic of the game, in line 91, our written expectimax function should have entered the work and gave us its proposed move, but our function only gave the best possible value for the output of the expectimax algorithm on the value of the function value of the player's current state, and hence from Enter the algorithm into the game. (If he gave us the output of his suggested move, we would put it in the move variable and then enter the move into the game by defining the make_move function.)
It seems that the oversimplification of the game and the lack of definition of actions such as mortgage and construction of houses and hotels made the implementation of the game certain and made it impossible for us to properly use the written expectimax function.
## Space of possible movements
The set of all possible moves for a player in his turn is called the space of possible moves in a game.
In this game and this implementation:
Throw the dice to go to the new house on the board
Buying a property if you go to a property without an owner
Paying rent to move onto property owned by another player
Using the "Get Out of Jail" card or rolling a 6 dice to get out of jail
Selling a property to raise money
## Observation space
This is the information that the algorithm has about the current state of the game:
Current player cash balance
List of current player properties
The current position of the current player on the board
game turn
The status of the owners of all the properties in the game
Status of the local chest and luck
## Explanation of value function
We considered the player's money plus twice the sum of his real estate money as the value function.
In fact, we considered the player's assets as a variable of the value of the player's current situation. The reason for taking twice the total value of the player's real estate compared to the player's current money is because the real estate is more important to the money because the player may not have spent his money and it is worthless.
The reason for not considering the rest of the parameters for the value function is the failure to run the code and the impossibility of checking the satisfaction level of this value function and the feasibility of changing this function.
## Show execution of the game code

    Starting a new game of Monopoly...

--- Turn 1 ---

Current player: Player 1
Current cash balance: $1500
Current position: Go

Player 1 rolls the dice and moves to Mediterranean Avenue.
Mediterranean Avenue is unowned. Player 1 buys Mediterranean Avenue for $60.
Player 1's cash balance is now $1440.

--- Turn 2 ---

Current player: Player 2
Current cash balance: $1500
Current position: Go

Player 2 rolls the dice and moves to Chance.
Player 2 draws a Chance card: "Advance to St. Charles Place."
Player 2 moves to St. Charles Place.
St. Charles Place is unowned. Player 2 buys St. Charles Place for $140.
Player 2's cash balance is now $1360.
 
--- Turn 3 ---

Current player: Player 1
Current cash balance: $1440
Current position: Mediterranean Avenue

Player 1 rolls the dice and moves to Community Chest.
Player 1 draws a Community Chest card: "Bank error in your favor. Collect $200."
Player 1's cash balance is now $1640.

--- Turn 4 ---

Current player: Player 2
Current cash balance: $1360
Current position: St. Charles Place

Player 2 rolls the dice and moves to Electric Company.
Electric Company is unowned. Player 2 decides not to buy it.

--- Turn 5 ---

Current player: Player 1
Current cash balance: $1640
Current position: Community Chest

Player 1 rolls the dice and moves to Reading Railroad.
Reading Railroad is unowned. Player 1 buys Reading Railroad for $200.
Player 1's cash balance is now $1440.
 
--- Turn 6 ---

Current player: Player 2
Current cash balance: $1360
Current position: Electric Company

Player 2 rolls the dice and moves to Park Place.
Park Place is unowned. Player 2 decides to buy Park Place for $350.
Player 2's cash balance is now $1010.

--- Turn 7 ---

Current player: Player 1
Current cash balance: $1440
Current position: Reading Railroad

Player 1 rolls the dice and moves to Oriental Avenue.
Oriental Avenue is unowned. Player 1 buys Oriental Avenue for $100.
Player 1's cash balance is now $1340.

--- Turn 8 ---

Current player: Player 2
Current cash balance: $1010
Current position: Park Place

Player 2 rolls the dice and moves to Boardwalk.
Boardwalk is unowned. Player 2 decides to buy Boardwalk for $400.
Player 2's cash balance is now $610. 

--- Turn 9 ---

Current player: Player 1
Current cash balance: $1340
Current position: Oriental Avenue

Player 1 rolls the dice and moves to Water Works.
Water Works is unowned. Player 1 decides not to buy it.

--- Turn 10 ---

Current player: Player 2
Current cash balance: $610
Current position: Boardwalk

Player 2 rolls the dice and moves to Luxury Tax.
Player 2 pays $75 in Luxury Tax.
Player 2's cash balance is now $535.

--- Turn 11 ---

Current player: Player 1
Current cash balance: $1340
Current position: Water Works

Player 1 rolls the dice and moves to Illinois Avenue.
Illinois Avenue is unowned. Player 1 buys Illinois Avenue for $240.
## Conclusion
From this article, it was concluded that for the proper implementation of a big game like Monopoly with a random algorithm like expectimax, it is better that the game has minimal complications such as construction and mortgage so that randomness can be well introduced into the game.
Also, a more object-oriented implementation allows us to better communicate between the artificial intelligence algorithm and the implementation of the game space.
