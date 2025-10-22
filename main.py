from tkinter import*
import tkinter.font as font
import random

game_window = Tk()
game_window.title("Rock Paper Scissors")

app_font = font.Font(size=12)

game_title = Label(game_window, text="Rock, paper, scissors", font=font.Font(size=20),fg="grey")
game_title.pack()

winner_label = Label(game_window, text="", fg = "green", font= font.Font (size = 8))
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack(pady=20)

rock_btn = Button(input_frame, text="Rock", width=15, bd=0, bg="pink", pady=5)
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text="Paper", width=15, bd=0, bg="blue", pady=5)
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text="Scissors", width=15, bd=0, bg="green", pady=5)
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

score_label = Label(input_frame, text="Score :", font = app_font, fg = "grey")
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text="Your Selected :---", font=app_font)
player_choice_label.grid(row=3, column=1, pady = 5)

player_score_label = Label(input_frame, text="Your Score :---", font=app_font)
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text="Computer Selected :---", font=app_font, fg = "black")
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text="Computer Score :---", font=app_font, fg = "black")
computer_score_label.grid(row=4, column=2, padx=(10,0), pady=5)

game_window.geometry("700x300")
game_window.mainloop()