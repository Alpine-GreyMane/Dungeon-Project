# ModuleSixMilestone.py
# Author: [Your Name]

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

def display_room(player_room):
    print(f"You are in the {player_room}.")

def main():
    player_room = 'Great Hall'
    exit_room = 'exit'

    while player_room != exit_room:
        display_room(player_room)

        # Get user input
        user_input = input("Enter your command (e.g., 'go North', 'go South', 'exit'): ")

        # Split the user input into command and direction
        command, direction = user_input.strip().split(' ', 1)

        # Check if the command is valid
        if command.lower() == 'go':
            # Check if the direction is valid for the current room
            if direction in rooms[player_room]:
                # Move to the new room based on the direction
                player_room = rooms[player_room][direction]
            else:
                print("You cannot go in that direction.")
        elif command.lower() == 'exit':
            player_room = exit_room
        else:
            print("Invalid command. Please try again.")

    print("Thank you for playing the game!")

if __name__ == "__main__":
    main()
