# ModuleSixMilestone.py
# Author: [Your Name]

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms and descriptions.
rooms = {
    'Great Hall': {'South': 'Bedroom', 'Description': 'You are in a grand hall with a large chandelier.'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar', 'Description': 'You are in a cozy bedroom with a comfortable bed.'},
    'Cellar': {'West': 'Bedroom', 'Description': 'You are in a dimly lit cellar with barrels and crates.'}
}

def display_room(player_room):
    description = rooms[player_room]['Description']
    print(description)
    print(f"Possible directions: {', '.join(rooms[player_room].keys() - ['Description'])}")

def main():
    player_room = 'Great Hall'
    exit_room = 'exit'

    print("Welcome to the Dragon Text Game!")
    print("Type 'help' for a list of commands.")

    while player_room != exit_room:
        display_room(player_room)

        user_input = input("Enter your command: ").lower()

        if user_input == 'help':
            print("Commands: go [Direction], look, exit, help")
        elif user_input.startswith('go '):
            _, direction = user_input.split(' ', 1)
            if direction in rooms[player_room]:
                player_room = rooms[player_room][direction]
            else:
                print("You cannot go in that direction.")
        elif user_input == 'look':
            display_room(player_room)
        elif user_input == 'exit':
            player_room = exit_room
        else:
            print("Invalid command. Type 'help' for a list of commands.")

    print("Thank you for playing the game!")

if __name__ == "__main__":
    main()
