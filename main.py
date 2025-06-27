# Brandon Hazelton
# Instructions for user
def instructions():
    print("Welcome to the Evil Wizard's lair text based game")
    print('You have been hired by the local townsfolk to')
    print("defeat the evil wizard Nodnarb, who is kidnapping")
    print("the townsfolk's daughters for his youth potion.")
    print('You must navigate his tower and defeat him.')
    print('To navigate his tower you will use the')
    print('cardinal directions - North, East, South, and West.')
    print('Luckily for you, the wizard has left magical')
    print('artifacts in the various rooms of his tower.')
    print('Collect all 6 artifacts before entering his lair')
    print('to defeat him. Enter his lair without them and perish.')
    print('--------------------------------------------------')
# Dictionary of rooms available to the player
rooms = {
    'Tower Entrance': {'South': 'Garden', 'item': None},
    'Garden': {'North': 'Tower Entrance', 'West': 'Library', 'item': 'Herbs'},
    'Library': {'North': 'Observatory', 'West': 'Bedroom',
                'South': 'Alchemy Lab', 'East': 'Garden', 'item' : 'Tome of Ancient Magick' },
    'Bedroom': {'East': 'Library', 'item': 'Robe of Protection'},
    'Alchemy Lab': {'North': 'Library', 'East': 'Dungeon', 'item': 'Potion of Health'},
    'Dungeon': {'West': 'Alchemy Lab', 'item': 'Magick Imbued Staff'},
    'Observatory': {'East': "Wizard's Lair", 'South': 'Library', 'item': 'Telescope of Future Sight'},
    "Wizard's Lair": {'West': 'Observatory', 'item': None}
}


# List of directions the user can take
directions: set[str] = {'North', 'South', 'East', 'West', 'north', 'south', 'east', 'west'}

#Items needed to win
total_items = {'Herbs', 'Tome of Ancient Magick', 'Potion of Health', 'Magick Imbued Staff',
               'Robe of Protection', 'Telescope of Future Sight'}
# Runs the instructions
instructions()

def main():
    location = 'Tower Entrance'  # Starting point
    inventory = set()  # Player's inventory

    def show_status():
        print(f'You are currently in the {location}.')
        room_item = rooms[location].get('item')
        if room_item and room_item not in inventory:
            print(f'This room contains: {room_item}')
        print(f'Your inventory: {", ".join(inventory) if inventory else "Empty"}')

    while True:
        show_status()
        possible_moves = rooms.get(location, {})
        command = input('Enter a direction (North, South, East, West) or "Get [item]": ').capitalize().strip()
        print('-------------------------------')

        # Handle direction commands
        if command in directions:
            if command not in possible_moves:
                print('You cannot go that way. Try again.')
            else:
                location = possible_moves[command]  # Update the location here

                # Check for game-ending conditions
                if location == "Wizard's Lair":
                    if inventory == total_items:
                        print('You have collected all the items and defeated the evil wizard Nodnarb!')
                        print('Congratulations! You win!')
                        break
                    else:
                        print('You entered the Wizard\'s Lair without all the items.')
                        print('The wizard overpowered you. You lose!')
                        break

        # Handle item pickup commands
        elif command.lower().startswith("get "):
            item_name = command[4:].strip()
            room_item = rooms[location].get('item')
            if room_item and room_item.lower() == item_name.lower() and room_item not in inventory:
                inventory.add(room_item)
                print(f'You picked up {room_item}.')
            else:
                print('There is nothing like that to pick up here.')

        else:
            print('Invalid input. Please enter a valid direction (North, South, East, West) or "Get [item]".')

if __name__ == '__main__':
    main()