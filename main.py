import tkinter as tk
import random
from tkinter import messagebox

words = [
    "Novak Djokovic",
    "Rafael Nadal",
    "Roger Federer",
    "Carlos Alcaraz",
    "Daniil Medvedev",
    "Stefanos Tsitsipas",
    "Alexander Zverev",
    "Dominic Thiem",
    "Andrey Rublev",
    "Jannik Sinner"
]

root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x400")

label = tk.Label(root, text='Guess the word game', font=('Helvetica', 16))
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check", command=lambda: check())
button.pack()

lives_label = tk.Label(root, text="Lives remaining: 6", font=("Helvetica", 16))
lives_label.pack()

canvas = tk.Canvas(width=200, height=200)
canvas.pack()

def draw_hangman(lives):
    canvas.delete("all")
    if lives <= 5:
        canvas.create_line(50, 50, 150, 50)  # top bar
    if lives <= 4:
        canvas.create_line(100, 50, 100, 100)  # vertical bar
    if lives <= 3:
        canvas.create_oval(90, 100, 110, 120)  # head
    if lives <= 2:
        canvas.create_line(100, 120, 100, 170)  # body
    if lives <= 1:
        canvas.create_line(100, 120, 130, 150)  # right arm
    if lives == 0:
        canvas.create_line(100, 120, 70, 150)  # left arm

chosen_word = random.choice(words).upper()
guessed_word = ['_'] * len(chosen_word)
lives = 6

word_label = tk.Label(root, text=' '.join(guessed_word), font=('Helvetica', 16))
word_label.pack()

def check():
    global lives
    guess = entry.get().upper()
    entry.delete(0, "end")

    if guess and guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess

        word_label.config(text=' '.join(guessed_word))

        if ''.join(guessed_word) == chosen_word:
            messagebox.showinfo('You won!', "Congratulations, you guessed the word!")
            root.destroy()
    else:
        lives -= 1
        lives_label.config(text=f'Lives remaining: {lives}')
        draw_hangman(lives)

        if lives == 0:
            messagebox.showinfo('You lost', f'The word was {chosen_word}')
            root.destroy()

root.mainloop()
