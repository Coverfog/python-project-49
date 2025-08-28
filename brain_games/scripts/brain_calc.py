from brain_games.cli import welcome_user as greet
from brain_games.games.calc_game import calc_game


def main():
    user = greet()
    calc_game(user)


if __name__ == '__main__':
    main()
