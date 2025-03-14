from games import *

class GameOfNim(Game):
    def __init__(self, board):
        """Initialize the Game of Nim with the given board."""
        self.initial = GameState(
            to_move='MAX',
            utility=0,
            board=board,
            moves=self.actions_from_board(board)
        )

    def actions_from_board(self, board):
        """Generate all possible actions from the current board."""
        actions = []
        for row_idx, count in enumerate(board):
            for num in range(1, count + 1):
                actions.append((row_idx, num))
        return actions

    def actions(self, state):
        """Return a list of valid actions in the given state."""
        return state.moves

    def result(self, state, move):
        """Return the resulting state after applying a move."""
        row, num = move
        new_board = list(state.board) 
        new_board[row] -= num  
        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        moves = self.actions_from_board(new_board)
        utility = self.compute_utility(new_board, state.to_move) if self.terminal_test(GameState(next_player, 0, new_board, moves)) else 0
        return GameState(to_move=next_player, utility=utility, board=new_board, moves=moves)

    def terminal_test(self, state):
        """Return True if the game is over (all piles are empty)."""
        return all(pile == 0 for pile in state.board)

    def utility(self, state, player):
        """Return the utility of the state from the perspective of player."""
        return state.utility if player == 'MAX' else -state.utility

    def compute_utility(self, board, player):
        """Compute utility for terminal state. The player who makes the last move loses."""
        return -1 if player == 'MAX' else +1

    def display(self, state):
        """Display the current board."""
        print("board: ", state.board)

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) 
    print(nim.initial.board) 
    print(nim.initial.moves) 
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player)  
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")

    # Test Cases
    assert nim.initial.board == [0, 5, 3, 1], "Initialization failed"
    assert nim.initial.moves == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)], "Actions failed"

    new_state = nim.result(nim.initial, (1, 3))
    assert new_state.board == [0, 2, 3, 1], "Result function failed"
    assert new_state.to_move == 'MIN', "Turn change failed"

    empty_state = GameState(to_move='MAX', utility=0, board=[0, 0, 0], moves=[])
    assert nim.terminal_test(empty_state) == True, "Terminal test failed"

    assert nim.utility(empty_state, 'MAX') == -1, "Utility calculation failed"
    assert nim.utility(empty_state, 'MIN') == 1, "Utility calculation failed"

    print("All test cases passed")

  
