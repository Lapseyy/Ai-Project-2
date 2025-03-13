from game_of_nim import GameOfNim
from games import query_player, alpha_beta_player

if __name__ == '__main__':
    print("Welcome to the Game of Nim!")
    initial_board = [7, 5, 3, 1]  # You can modify this to test different configurations

    # Initialize and play
    game = GameOfNim(initial_board)
    result = game.play_game(query_player, alpha_beta_player)  # Human vs. AI

    # Display result
    if result == 1:
        print("MAX won the game")
    elif result == -1:
        print("MIN won the game")
    else:
        print("Game ended in a draw")
