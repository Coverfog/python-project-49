from brain_games.cli import welcome_user
from brain_games.games.gcd_game import gcd_game
from brain_games.games_engine import start_game


def main():
    user = welcome_user()
    start_game(gcd_game, user)


if __name__ == '__main__':
    main()
