from tkinter import *
from tkinter import simpledialog, messagebox

main = Tk()
main.withdraw()

questions =[
    "What does G stands for in Gpay",
    "Which part of the computer is called the brain of the computer"
]

answer =[
    "Google",
    "CPU"
]

score = 0

for i in range(0, len(questions)):
    print(questions[i])
    user_answer = simpledialog.askstring(questions[i], "Answer: ")

    if user_answer == answer[i]:
        messagebox.showinfo("Correct", "Correct")
        score = score + 1
    else:
        messagebox.showinfo("Wrong", "Wrong")

messagebox.showinfo("Score", str(score))