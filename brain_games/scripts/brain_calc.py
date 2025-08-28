from brain_games.cli import welcome_user
from brain_games.games.calc_game import calc_game
from brain_games.games_engine import start_game


def main():
    user = welcome_user()
    start_game(calc_game, user)


if __name__ == '__main__':
    main()
