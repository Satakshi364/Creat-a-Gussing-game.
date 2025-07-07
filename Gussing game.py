#create a Guessing Game
import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f0f0")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        # Introduction label
        self.intro_label = tk.Label(master, text="Guess a number between 1 and 100", font=("Arial", 14), bg="#f0f0f0")
        self.intro_label.pack(pady=10)

      
        self.entry = tk.Entry(master, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

       
        self.check_btn = tk.Button(master, text="Check", command=self.check_guess, font=("Arial", 12))
        self.check_btn.pack(pady=10)

       
        self.feedback_label = tk.Label(master, text="", font=("Arial", 12), fg="blue", bg="#f0f0f0")
        self.feedback_label.pack(pady=10)

        
        self.reset_btn = tk.Button(master, text="Reset Game", command=self.reset_game, font=("Arial", 10), state="disabled")
        self.reset_btn.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if guess.isdigit():
            guess = int(guess)
            self.attempts += 1
            if guess < self.target_number:
                self.feedback_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.feedback_label.config(text="Correct! You can reset the game now.")
                self.reset_btn.config(state="normal")
        else:
            messagebox.showwarning("Invalid input", "Please enter a valid number.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.reset_btn.config(state="disabled")


if __name__ == '__main__':
    root = tk.Tk()
    game = GuessingGameGUI(root)
    root.mainloop()
