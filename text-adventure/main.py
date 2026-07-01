#!/usr/bin/python3
rooms = {
    "front_gate": {
        "description": "The wrought-iron gates of Ever After High stand before you, framed by hedges shaped like storybook creatures.",
        "choices": {
            "hall": "charmitage_hall",
            "forest": "enchanted_forest",
            "leave": "THE_END",
        },
    },
    "charmitage_hall": {
        "description": "A grand entrance hall lined with portraits of legendary Charmings. Students bustle between classes.",
        "choices": {
            "gate": "front_gate",
            "office": "headmaster_grimms_office",
            "castleteria": "castleteria",
            "dorms": "dorm_hallway",
            "garden": "hexcellent_garden",
        },
    },
    "headmaster_grimms_office": {
        "description": "A stern, book-lined office. Headmaster Grimm's desk is covered in scrolls and destiny contracts.",
        "choices": {
            "hall": "charmitage_hall",
            "mirror_class": "mirror_classroom",
        },
    },
    "mirror_classroom": {
        "description": "Rows of enchanted mirrors line the walls, each one a portal to somewhere else in the Storybook of Legends.",
        "choices": {
            "office": "headmaster_grimms_office",
            "prison_mirror": "evil_queens_mirror_prison",
            "muse_ic": "muse_ic_class",
        },
    },
    "evil_queens_mirror_prison": {
        "description": "A dark, glassy realm inside the mirror itself - this is where the Evil Queen, Raven's mother, has been trapped since Legacy Day.",
        "choices": {
            "back": "mirror_classroom",
        },
    },
    "dorm_hallway": {
        "description": "A long hallway of dorm rooms, each door personalized with its resident's crest.",
        "choices": {
            "hall": "charmitage_hall",
            "raven_apple_room": "raven_and_apples_dorm",
            "library": "school_library",
        },
    },
    "raven_and_apples_dorm": {
        "description": "A room split perfectly down the middle - one side dark and moody, the other bright pink and cheerful. Raven Queen and Apple White's shared dorm room.",
        "choices": {
            "hallway": "dorm_hallway",
        },
    },
    "hexcellent_garden": {
        "description": "A garden full of talking flowers and hedges trimmed into shapes from famous fairy tales.",
        "choices": {
            "hall": "charmitage_hall",
            "forest": "enchanted_forest",
            "beach": "mirror_beach",
        },
    },
    "castleteria": {
        "description": "The school cafeteria, where enchanted food serves itself and the tables rearrange by friend group.",
        "choices": {
            "hall": "charmitage_hall",
            "villainy": "general_villainy_class",
            "damsel": "damsel_in_distressing_class",
        },
    },
    "general_villainy_class": {
        "description": "A classroom for learning the finer points of scheming, brooding, and dramatic entrances.",
        "choices": {
            "castleteria": "castleteria",
            "chemythstry": "chemythstry_lab",
        },
    },
    "damsel_in_distressing_class": {
        "description": "A class dedicated to the art of waiting to be rescued - though not everyone agrees it should still be taught.",
        "choices": {
            "castleteria": "castleteria",
            "hatter_class": "mad_hatters_class",
        },
    },
    "chemythstry_lab": {
        "description": "Bubbling potions and mismatched ingredients fill every table - equal parts chemistry and myth.",
        "choices": {
            "villainy": "general_villainy_class",
            "muse_ic": "muse_ic_class",
        },
    },
    "muse_ic_class": {
        "description": "A music room where instruments play themselves and every song seems to have a magical effect.",
        "choices": {
            "mirror_class": "mirror_classroom",
            "chemythstry": "chemythstry_lab",
            "bookstore": "book_end_bookstore",
        },
    },
    "mad_hatters_class": {
        "description": "Nothing here is quite what it seems - clocks run backward and tea never stops pouring.",
        "choices": {
            "damsel": "damsel_in_distressing_class",
            "bookstore": "book_end_bookstore",
        },
    },
    "book_end_bookstore": {
        "description": "A cozy bookstore and cafe where students swap stories over drinks brewed from magic ink.",
        "choices": {
            "muse_ic": "muse_ic_class",
            "hatter_class": "mad_hatters_class",
            "library": "school_library",
        },
    },
    "school_library": {
        "description": "Towering shelves hold every fairytale ever written - and a few that haven't happened yet.",
        "choices": {
            "dorms": "dorm_hallway",
            "bookstore": "book_end_bookstore",
        },
    },
    "dragon_games_stadium": {
        "description": "A massive arena built for the Dragon Games, still scorched in places from the last dragon race.",
        "choices": {
            "forest": "enchanted_forest",
        },
    },
    "enchanted_forest": {
        "description": "A dense, whispering forest just past the school grounds, full of shortcuts and unexpected magic.",
        "choices": {
            "gate": "front_gate",
            "garden": "hexcellent_garden",
            "stadium": "dragon_games_stadium",
            "beach": "mirror_beach",
        },
    },
    "mirror_beach": {
        "description": "A shimmering shoreline where the water reflects like glass - said to be another gateway into the Mirror world.",
        "choices": {
            "garden": "hexcellent_garden",
            "forest": "enchanted_forest",
        },
    },
}


def show_room(room_key, rooms):
    room = rooms[room_key]
    print("\n" + room["description"])
    print("\nWhere do you want to go?")
    for choice in room["choices"]:
        print(f"  - {choice}")


def play(rooms, start_room):
    current_room = start_room

    while True:
        show_room(current_room, rooms)
        choice = input("\n> ").lower().strip()

        room_choices = rooms[current_room]["choices"]

        if choice == "quit":
            print("Thanks for playing!")
            break
        elif choice in room_choices:
            next_room = room_choices[choice]
            if next_room == "THE_END":
                print("\nYou decide to head home for the day. The End!")
                break
            current_room = next_room
        else:
            print("You can't go that way. Try again.")


def main():
    print("=== Ever After High: A Day at School ===")
    print("Type the name of where you want to go. Type 'quit' to leave.")
    play(rooms, "front_gate")


main()
