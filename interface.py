import tkinter as tk
from game.logic import decide_winner
from game.computer import get_computer_choice

class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stone Paper Scissor")
        self.root.geometry("420x500")
        self.root.config(bg="#1e1e2f")

        self.user_score = 0
        self.comp_score = 0

        # Title
        tk.Label(self.root, text="STONE PAPER SCISSOR",
                 font=("Arial", 18, "bold"),
                 fg="#00ffcc", bg="#1e1e2f").pack(pady=15)

        # Score
        self.score_label = tk.Label(self.root,
                                    text="You: 0  |  Computer: 0",
                                    font=("Arial", 13, "bold"),
                                    fg="white", bg="#1e1e2f")
        self.score_label.pack(pady=10)

        # Result box
        self.result_label = tk.Label(self.root,
                                     text="Make your move!",
                                     font=("Arial", 12),
                                     fg="yellow", bg="#1e1e2f")
        self.result_label.pack(pady=20)

        # Buttons frame
        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=20)

        # Stylish buttons
        self.create_button(btn_frame, "Stone", "#ff6b6b")
        self.create_button(btn_frame, "Paper", "#4ecdc4")
        self.create_button(btn_frame, "Scissor", "#ffe66d")

        # Reset button
        tk.Button(self.root, text="Reset Game",
                  font=("Arial", 11, "bold"),
                  bg="#ff4757", fg="white",
                  width=15,
                  command=self.reset_game).pack(pady=25)

    def create_button(self, frame, text, color):
        tk.Button(frame, text=text,
                  font=("Arial", 12, "bold"),
                  bg=color, fg="black",
                  width=12, height=2,
                  relief="raised",
                  command=lambda: self.play(text)).pack(pady=8)

    def play(self, user_choice):
        computer_choice = get_computer_choice()
        result = decide_winner(user_choice, computer_choice)

        if result == "You Win!":
            self.user_score += 1
        elif result == "Computer Wins!":
            self.comp_score += 1

        self.score_label.config(
            text=f"You: {self.user_score}  |  Computer: {self.comp_score}"
        )

        self.result_label.config(
            text=f"You: {user_choice}   |   Computer: {computer_choice}\n{result}"
        )

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.config(text="You: 0  |  Computer: 0")
        self.result_label.config(text="Game Reset! Play again.")

    def run(self):
        self.root.mainloop()