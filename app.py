from book import adventure
import json
import time



history_list = []

def mainmenu():
    while True:
        print("Welcome to the game!")
        print("1. Start")
        print("2. Load")
        print("3. Exit")
        choice = input("Enter your choice: ")
        history_list.append(choice)
        if choice == "1":
            break
            main()
        elif choice == "2":
            print("Loading...")
            break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def history_show():
    print("History: ")
    for i, page in enumerate(history_list):
        print(f"{i + 1}. {page}")






def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
    return None

def show_page(page):
    print(page["title"])
    print(page["text"])
    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")


def main():
    mainmenu()
    current_id = 1
    inventory = []
    while True and current_id is not None:
        current_page = get_page(adventure, current_id)
        show_page(current_page)
        history_list.append(current_page["title"])
        if "loot" in current_page:
            print(f"\033[32mYou found {current_page['loot']}!\033[0m")
            inventory.append(current_page["loot"])
        choice = input_int("Enter your choice: ")
        if 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]
        else:
            print("Invalid choice. Please try again.")
            current_id = None



if __name__ == "__main__":
    main()
