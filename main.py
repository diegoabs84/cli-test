# Python
from dictionary import get_definition

def main():
    print("Welcome to the CLI Dictionary!")
    print("You can use this tool to look up word definitions.")
    while True:
        print("\n1. Look up a word")
        print("2. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            word = input("Enter a word: ")
            definition = get_definition(word)
            print(definition)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()