from tkinter import*
import tkinter.font as font
import random

game_window = Tk()
game_window.title("Rock Paper Scissors")

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]
app_font = font.Font(size=12)

def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text="Computer Wins!")
    computer_score_label.config(text="Computer Score : " + str(computer_score))
    player_score_label.config(text="Player Score : " + str(player_score))

def player_wins():
    global computer_score, player_score
    player_score +=1
    winner_label.config(text="Player Wins!")
    computer_score_label.config(text="Computer_score : " +str(computer_score))
    player_score_label.config(text="Player Score : " + str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text="It's a Tie!")
    computer_score_label.config(text="Computer Score : " + str(computer_score))
    player_score_label.config(text="Player Score : " + str(player_score))

def player_choice(player_input):
    global player_score, computer_score
    print(player_input)

    computer_input = get_computer_choice()
    print(computer_input)
    player_choice_label.config(text="Your Selected : " + player_input[0])
    computer_choice_label.config(text="Computer Selected : " + computer_input[0])

    if player_input[1] == computer_input[1]:
        tie()
    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            computer_wins()
        if(computer_input[1] == 2):
            player_wins()

    elif(player_input[1] == 1):
        if(computer_input[1] == 0):
            player_wins()
        if(computer_input[1] == 2):
            computer_wins()
    
    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_wins()
        if(computer_input[1] == 1):
            player_wins()
            
def get_computer_choice()
    return random.choice(options)

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

scissors_btn = Button(input_frame, text="Scissors", width=15, bd=0, background="green", pady=5)
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