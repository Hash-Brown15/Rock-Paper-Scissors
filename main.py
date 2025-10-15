from tkinter import*
import tkinter.font as font

my_window = Tk()
my_window.geometry("500x500")

decription = Label(my_window, text="Rock, paper, scissors", font=font.Font(size=20,fg="grey"))
decription.pack()

fame = Frame
frame.pack(pady=20)

title = Label(frame, text="Rock Paper Scissors", font=font.Font(size=15))
title.grid(row=0, column=0)

options = Label(frame, text="Your Options:" ,font=font.Font(size=15))
options.grid(row=1, column=0)

score = Label(frame, text="Score:", font=font.Font(size=15))
score.grid(row=2, column=0)

rock = Button(frame, text="Rock", font=font.Font(size=15), bg="red", fg="white", padx=20, pady=10)
rock.grid(row=1, column=1, columnspan = 2, padx=10)

paper = Button(frame, text="Paper", font=font.Font(size=15), bg="blue", fg="white", padx=20, pady=10)
paper.grid(row=1, column=3, columnspan = 2, padx=10)

scissors = Button(frame, text="Scissors", font=font.Font(size=15), bg="green", fg="white", padx=20, pady=10)
scissors.grid(row=1, column=5, columnspan = 2, padx=10)