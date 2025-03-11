class Game():
    def __init__(self, turn='X', tie=False, winner=None, board={
                'a1': None, 'b1': None, 'c1': None,
                'a2': None, 'b2': None, 'c2': None,
                'a3': None, 'b3': None, 'c3': None
            }):
        
            
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board

    def play_game(self):
        print('Welcome to tic-tac-toe game!')

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] == None:
                self.board[move] = self.turn
                return  
            else:
                print('Invalid input, try again.')

    def check_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            self.winner = self.turn
        elif self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
            self.winner = self.turn
        elif self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
            self.winner = self.turn    
        elif self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
            self.winner = self.turn 
        elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
            self.winner = self.turn 
        elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            self.winner = self.turn
        elif self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
            self.winner = self.turn    
        elif self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1']):
            self.winner = self.turn 

    def check_tie(self):
        empty= False
        for move in self.board:
            if self.board[move]== None :
                empty=True
                break
        if not empty and self.winner==None:
            self.tie=True



    def switch_turn(self):
        self.check_winner()
        self.check_tie()
        if self.winner or self.tie:
            return 
        if self.turn=='X':
            self.turn='O'
        else:
            self.turn='X'    

    def play_game(self):
        print("Shall we play a game??")
        while self.winner == None and self.tie==False:
            self.render()
            self.get_move()
            self.switch_turn()
        self.render()

game_instance = Game()
game_instance.play_game()
