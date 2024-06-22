from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

main = Tk()
main.title("Hangman")
main.geometry("800x600")

imageList = []
for i in range(1,8):
    imageList.append( Image.open("./images/hangman0" + str(i) + ".png"))


test = ImageTk.PhotoImage(imageList[0])
label1 = Label(image=test)
label1.image = test
label1.place(x=0, y=0)

max = 6
score = 0

word = "BOOK"
word = word.lower()
print(word)

while True:
   key = simpledialog.askstring("Guess", "Guess a letter: ")
   if key in word:
       messagebox.showinfo("Hangman", "word cointains " + key)
       word = word.replace(key,"")
       print(len(word))
       if len(word) == 0:
           messagebox.showinfo("Hangman", "You win")
           break
   else:
       messagebox.showinfo("Hangman", "wrong")
       score = score + 1
       
       test = ImageTk.PhotoImage(imageList[score])
       label1 = Label(image=test)
       label1.image = test
       label1.place(x=0, y=0)

       if score >= max:
           messagebox.showinfo("Hangman", "You lose")
           break