import itertools


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # Horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally")
            return True
    # Vertical
    for col in range(len(current_game)):
        check = []

    for row in current_game:
        check.append(row[col])

    if all_same(check):
        print(f"Player {row[0]} is the winner vertically")
        return True
   # Diagonal
    diags = []

    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)")
        return True

    diags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position has already been played. Try another!")
            return False

        print("   a  b  c")

        if not just_display:
            game_map[row][column] = player

        for row, count in enumerate(game):
            print(row, count)

        return game_map, True
    except IndexError as e:
        print("Error: Make sure you input row/column as 0-2", e)
        return game_map, False
    except Exception as e:
        print("You really fucked up!")
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(
                input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(
                input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(
                game, current_player, row_choice, column_choice)

            if win(game):
                game_won = True
                again = input(
                    "The game is over, would you like to pay again? (y/n) ")
                if again.lower() == "y":
                    print("Reloading...")
                elif again.lower() == "n":
                    print("BYE")
                    play = False
                else:
                    print(
                        "Not a valid answer. You don't deserve to pay again. Seeee ya!")
                    play = False
