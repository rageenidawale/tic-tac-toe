logo = """

 ____  __  ___    ____  __    ___    ____  __  ____ 
(_  _)(  )/ __)  (_  _)/ _\  / __)  (_  _)/  \(  __)
  )(   )(( (__     )( /    \( (__     )( (  O )) _) 
 (__) (__)\___)   (__)\_/\_/ \___)   (__) \__/(____)

"""
print(logo)

global game_tile_list
game_tile_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

possible_combinations = [[1, 2, 3], [1, 4, 7], [3, 6, 9], [7, 8, 9],
                         [1, 5, 9], [3, 5, 7], [2, 5, 8], [4, 5, 6]]
tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Create a user class
class User:
    def __init__(self, sign):
        self.sign = sign
        self.moves = []


# Create a function to show the tile
def show():
    game_tile = f' {game_tile_list[0]} | {game_tile_list[1]} | {game_tile_list[2]} \n' \
                f'-----------\n' \
                f' {game_tile_list[3]} | {game_tile_list[4]} | {game_tile_list[5]} \n' \
                f'-----------\n' \
                f' {game_tile_list[6]} | {game_tile_list[7]} | {game_tile_list[8]} \n'
    print(game_tile)


def game(user):
    global game_tile_list
    show()
    tile_number = int(input(f"Where do you want to place {user.sign}? Choose from numbers 1-9: "))

    # Make sure the tile number is in between 1-9
    while True:
        if tile_number not in range(1, 10):
            tile_number = int(input("Please choose numbers from 1-9: "))
        else:
            break

    while True:
        if tile_number in tiles:
            # Replace the X/0 with whichever tile number mentioned
            game_tile_list = [user.sign if ele == tile_number else ele for ele in game_tile_list]
            # Add the tile number to the user moves
            user.moves.append(tile_number)
            # Sort it in ascending order for easier search
            user.moves.sort()
            # Remove the tile number so that it can't be re-written
            tiles.remove(tile_number)
            break
        else:
            tile_number = int(input("Please a valid tile number: "))

    if tiles:
        # Check if all the elements in every list of possible combinations are present in the user.moves
        for lst in possible_combinations:
            result = all(elem in user.moves for elem in lst)
            if result:
                # if elements are present the user wins
                # if not, the game continues till all the tiles are filled or either user wins
                print(f"{user.sign} wins!")
                show()
                global is_game_on
                is_game_on = False
                break
    else:
        # If no tiles are left it's a draw
        print("It's a draw!")
        is_game_on = False


# User 1 gets to choose the sign
user1_sign = input("Enter the sign user 1 wants (X/O): ")
while True:
    if user1_sign == "X":
        user1 = User("X")
        user2 = User("O")
        break
    elif user1_sign == "O":
        user1 = User("O")
        user2 = User("X")
        break
    else:
        user1_sign = input("Please choose between X and O only. Enter the sign user1 wants (X/O): ")

global is_game_on
is_game_on = True

while is_game_on:
    game(user1)
    # if condition makes sure the game is still on
    if is_game_on:
        game(user2)
