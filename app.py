from book import adventure
import json
import time
import os

history_list = []
inventory = []
SAVE_FILE = "save.json"

current_id = 1

def save_game():
    data = {
        "history": history_list,
        "current_id": current_id,
        "inventory": inventory
    }
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file)
    print("\033[34m[Game Saved]\033[0m")

def load_game():
    global history_list, current_id, inventory
    if not os.path.exists(SAVE_FILE) or os.path.getsize(SAVE_FILE) == 0:
        print("\033[31m[No save file found]\033[0m")
        return False  

    try:
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
            history_list = data.get("history", [])
            current_id = data.get("current_id", 1)
            inventory = data.get("inventory", [])
        
        print("\033[32m[Game Loaded Successfully]\033[0m")
        return True
    except (json.JSONDecodeError, KeyError):
        print("\033[31m[Error loading save file]\033[0m")
        return False

def delete_save():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
        print("\033[31m[Save file deleted]\033[0m")
    else:
        print("\033[31m[No save file found]\033[0m")

def load():
    while True:
        print("\n1. Load game")
        print("2. Delete save")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            if load_game():
                return True  # Load was successful
        elif choice == "2":
            delete_save()
        elif choice == "3":
            return False  # Go back to main menu
        else:
            print("\033[31m[Invalid choice]\033[0m")

def mainmenu():
    while True:
        print("Welcome to the game!")
        print("1. Start")
        print("2. Load")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            main()
            break
        elif choice == "2":
            if load():  # If load returns True, proceed to game
                main()  # Start the main game after loading
                break
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def reset_progress():
    global current_id, history_list, inventory
    current_id = 1
    history_list = []
    inventory = []
    save_game()

def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None

def show_page(page):
    for char in page["title"]:
        if char == '\n':
            print()
        else:
            print(char, end="", flush=True)
            time.sleep(0.05)
    print("\n" + "-" * len(page["title"]))
    time.sleep(1)
    for char in page["text"]:
        if char == '\n':
            print()
        else:
            print(char, end="", flush=True)
            time.sleep(0.05)
    
    print("\n")

    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")
    
    


def main():
    global current_id, inventory

    while current_id is not None:
        current_page = get_page(adventure, current_id)
        if not current_page:
            print("\033[31m[Error: Page not found!]\033[0m")
            break
        
        show_page(current_page)
        history_list.append(current_page["title"])

        if "loot" in current_page:
            print(f"\033[32mYou found {current_page['loot']}!\033[0m")
            inventory.append(current_page["loot"])

        choice = input_int("Enter your choice: ")
        if 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
            save_game()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    mainmenu()
