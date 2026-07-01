#!/usr/bin/python3
characters = [
    {
        "name": "Raven Queen",
        "parent_story": "The Evil Queen (Snow White)",
        "alignment": "Rebel",
        "secret_heart_desire": "To choose her own path instead of becoming evil",
    },
    {
        "name": "Apple White",
        "parent_story": "Snow White",
        "alignment": "Royal",
        "secret_heart_desire": "To become queen and live happily ever after",
    },
    {
        "name": "Madeline Hatter",
        "parent_story": "The Mad Hatter (Alice in Wonderland)",
        "alignment": "Rebel",
        "secret_heart_desire": "To stay wonderfully herself, riddles and all",
    },
    {
        "name": "Briar Beauty",
        "parent_story": "Sleeping Beauty",
        "alignment": "Royal",
        "secret_heart_desire": "To live life to the fullest before her 100-year sleep",
    },
    {
        "name": "Ashlynn Ella",
        "parent_story": "Cinderella",
        "alignment": "Rebel",
        "secret_heart_desire": "To be with Hunter instead of a prince",
    },
    {
        "name": "Hunter Huntsman",
        "parent_story": "The Huntsman (Snow White)",
        "alignment": "Rebel",
        "secret_heart_desire": "To live freely in the forest, not bound by his story",
    },
    {
        "name": "Cedar Wood",
        "parent_story": "Pinocchio",
        "alignment": "Rebel",
        "secret_heart_desire": "To become a real girl with her own free will",
    },
    {
        "name": "Cerise Hood",
        "parent_story": "Little Red Riding Hood",
        "alignment": "Rebel",
        "secret_heart_desire": "To keep her wolf heritage secret while being herself",
    },
    {
        "name": "Dexter Charming",
        "parent_story": "King Charming",
        "alignment": "Royal",
        "secret_heart_desire": "To win Raven's heart and prove himself charming",
    },
    {
        "name": "Daring Charming",
        "parent_story": "King Charming",
        "alignment": "Royal",
        "secret_heart_desire": "To be the hero of someone else's story, not just his own",
    },
    {
        "name": "Darling Charming",
        "parent_story": "King Charming",
        "alignment": "Rebel",
        "secret_heart_desire": "To be a knight in shining armor, not a damsel",
    },
    {
        "name": "Lizzie Hearts",
        "parent_story": "The Queen of Hearts (Alice in Wonderland)",
        "alignment": "Royal",
        "secret_heart_desire": "To rule fairly, unlike her mother",
    },
    {
        "name": "Kitty Cheshire",
        "parent_story": "The Cheshire Cat (Alice in Wonderland)",
        "alignment": "Rebel",
        "secret_heart_desire": "To cause mischief and choose her own loyalties",
    },
    {
        "name": "Blondie Lockes",
        "parent_story": "Goldilocks",
        "alignment": "Royal",
        "secret_heart_desire": "To report on the best stories as a journalist",
    },
    {
        "name": "Cupid",
        "parent_story": "Eros / Cupid (mythology)",
        "alignment": "Rebel",
        "secret_heart_desire": "To be accepted at the school despite not being from a classic fairytale",
    },
]

def display_all(characters):
    for character in characters:
        print(f"{character['name']} - {character['alignment']}")

def search_by_name(characters, name):
    for character in characters:
        if name.lower() in character["name"].lower():
            return character
    return None

def filter_by_alignment(characters, alignment):
    result = []
    for c in characters:
        if c["alignment"].lower() == alignment.lower():
            result.append(c)
    return result

def main():
    while True:
        print("\n--- Ever After High Character Database ---")
        print("1. View all characters")
        print("2. Search by name")
        print("3. Filter by alignment")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_all(characters)
        elif choice == "2":
            name = input("Enter a name: ")
            result = search_by_name(characters, name)
            print(result if result else "Character not found.")
        elif choice == "3":
            alignment = input("Royal or Rebel? ")
            for c in filter_by_alignment(characters, alignment):
                print(c["name"])
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
