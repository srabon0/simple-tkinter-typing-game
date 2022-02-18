from tkinter import *
from tkinter import messagebox
import random, string
import time
root = Tk()

root.title("Pro Typing")

root.resizable(FALSE, FALSE)
root.geometry("900x500")
root.configure(bg="#D0F5A9")

time_left = 60
score = 0
list1 = [
    "auto", "double", "int", "struct", "break", "else", "long", "switch",
    "case", "enum", "register", "typedef", "char", "extern", "return", 'union',
    "const", "short", "float", "unsigned", "continue", "for", "signed", "void",
    "default", "goto", "sizef", "volatile", "do", "if", "static", "while"
]
global word_as_string, list_as_word_string, entry, word, word_list, var1
word = StringVar()
var1 = StringVar()
word_as_string = StringVar()
entry = StringVar()
event = None


def start_game(event):
    global score

    if word_entry.get() == random_word['text']:
        score += 1
        label2.configure(text=score)

    word_entry.delete(0, END)
    var1 = random.choice(list1)
    word.set(str(var1))


root.bind("<Return>", start_game)


def countdown(count):
    label_time['text'] = count

    if count > 0:
        root.after(1000, countdown, count - 1)


def start():
    var1 = random.choice(list1)
    word.set(str(var1))
    start_game(event)
    countdown(60)


def gamerules():
    global screen2
    screen2 = Toplevel(root)
    screen2.geometry("370x250")
    screen2.title("Rules")
    screen2.resizable(FALSE, FALSE)
    screen2.configure(bg="#D0F5A9")

    Label01 = Label(
        screen2,
        text="1. Click The " + "Start The Game" + " Button ",
        font='arial 12 bold',
        bg="#D0F5A9")
    Label01.pack()
    Label02 = Label(
        screen2, text="2.Insert The words", font='arial 12 bold', bg="#D0F5A9")
    Label02.pack()
    Label03 = Label(
        screen2,
        text="3.After inserting Press " + "Enter" + " on your keyboard",
        font='arial 12 bold',
        bg="#D0F5A9")
    Label03.pack()


#top frame
topFrame = Frame(root, width="800", height="1")
topFrame.pack(side=TOP)
gamerules = Button(
    root,
    width="15",
    height="2",
    font="arial 12 bold",
    text='Game Rules',
    bg="#D7DCD6",
    bd=2,
    command=gamerules)
gamerules.place(x=0, y=10)

label1 = Label(
    topFrame,
    text="Welcome to Pro Typing",
    font="arial 18 bold",
    height="2",
    width="120",
    bg="#808677",
    pady=10,
    bd=4)
label1.pack(side=TOP)

label1 = Label(
    root,
    text="Your Score :",
    font="arial 15 bold",
    width="10",
    bg="#24B2D5",
    bd=4)
label1.place(x=15, y=90)
label2 = Label(
    root, text=score, font="arial 15 bold", width="10", bg="#24B2D5", bd=4)
label2.place(x=200, y=90)

label1 = Label(
    root,
    text="Time Left",
    font="arial 15 bold",
    width="10",
    bg="#24B2D5",
    bd=4)
label1.place(x=515, y=90)
label_time = Label(
    root, text=time_left, font="arial 15 bold", width="10", bg="#24B2D5", bd=4)
label_time.place(x=730, y=90)

label1 = Label(
    root,
    text="Random word chosen by Machine",
    font="arial 15 bold",
    width="30",
    bg="#24B2D5",
    bd=4)
label1.place(x=10, y=170)
random_word = Label(
    root,
    textvariable=word,
    font="arial 15 bold",
    width="30",
    bg="#24B2D5",
    bd=4)
random_word.place(x=500, y=170)
label1 = Label(
    root,
    text="Enter Here",
    font="arial 15 bold",
    width="30",
    bg="#24B2D5",
    bd=4)

label1.place(x=10, y=250)

word_entry = Entry(root, width='50', textvariable=word_as_string, bd=4)
word_entry.place(x=525, y=250)
btn1 = Button(
    root, width="30", text='Start The Game', bg="#E6E6FA", command=start, bd=2)
btn1.place(x=350, y=400)

root.mainloop()
