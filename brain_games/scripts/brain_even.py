from brain_games.cli import welcome_user
from brain_games.games.even_game import even_game
from brain_games.games_engine import start_game


def main():
    user = welcome_user()
    start_game(even_game, user)


if __name__ == '__main__':
    main()
