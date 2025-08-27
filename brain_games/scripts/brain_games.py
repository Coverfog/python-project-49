from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    user = welcome_user()
    print(f"Hello, {user}!")

if __name__ == '__main__':
    main()
