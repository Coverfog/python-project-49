from brain_games.games.even_game import even_game
from brain_games.cli import welcome_user as greet


def main():
    user = greet()
    even_game(user)


if __name__ == '__main__':
    main()
