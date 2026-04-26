from gui.interface import GameGUI

def main():
    while True:
        print("\n1. Start Game")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            game = GameGUI()
            game.run()
        elif choice == "2":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()