import math
import random
import time

class Player:
    def __init__(self, letter):
        # Letter x or o and name of player
        self.letter = letter
    def get_move(self, game):
        pass

class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)  #using super() to call attributes from superclass, the letter will continue and get move will be inherited

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square 

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False # Because square has no value
        val = None # No value in there yet from user
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we can check if this is a correct value by trying to cast it into an integer.if not an integer or spot already taken = invalid
            try:
                val = int(square) #user input should be able to turn into an intiger
                if val not in game.available_moves(): # If entry is not in available moves, it is not valid, raise error
                    raise ValueError
                valid_square = True # If these are successful, then we are good
            except ValueError:
                print('Invalid square. Try again.')
        return val 

class GeniusComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly chooses
        else:
            square = self.minimax(game, self.letter)['position'] # get the square based off minimax algorithm
        return square

    def minimax(self, state, player):
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X'
    
    # first we check for current winner also serves as base case
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1*(state.num_empty_squares() +1)}

        elif not state.empty_squares(): 
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf} # Each score should maximize 
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize
        
        for possible_move in state.available_moves():
            # 1 make a move
            state.make_move(possible_move, player)

            # 2 recurse using minimax to simulate a game after making move
            sim_score = self.minimax(state, other_player) # alternate players

            # 3 undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # 4 update in dictionaries
            if player == max_player: # maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # uses next best move
        return best



class TicTacToe:
    def __init__(self):
        self.board = [' ' for num in range(9)] # Can use a list to represent a 3x3 board. Lists print one row at a time. 
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # This will print indicies in rows of 3
            print('| ', ' | '.join(row) + ' |') # Prints boarder for board
        
    @staticmethod # Don't need self argument in static method
    def print_board_nums():
        # 0 | 1 | 2 (tells us what number corresponds to which space)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] # Prints a list of our current game. Print indicies for each row.
        for row in number_board:
            print('| ', ' | '.join(row) + ' |')
    
    def available_moves(self):
        # return []
        moves = []
        for (i,spot) in enumerate(self.board): # Gives what is available 
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid, make move, if not, then error
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Column Winner
        col_ind = square % 3 # % gives us the remainder after division, want it to be 0
        column = [self.board[col_ind+i*3] for i in range(3)] # Checks every 3 index
        if all([spot == letter for spot in column]):
            return True

        # Diagonal winner [0/4/8 or 2/4/6
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]] 
            if all([spot == letter for spot in diagonal_1]):
                return True 
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_2]):
                return True

        return False # If no winner


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # Starting letter
    while game.empty_squares: # This will iterate while the game has empty spots, break once we have winner
        if letter == 'O':
            square = o_player.get_move(game)
        else: 
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

                # after move, we alternate letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(1.5)

    if print_game: # indenting bc it needs to be out of while loop
            print('It\'s a tie!')


if __name__ == '__main__':
    x_player = Human('X')
    o_player = GeniusComputer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)