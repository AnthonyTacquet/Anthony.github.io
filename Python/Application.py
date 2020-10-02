from tkinter import *
import os
import sys
os.system('clear')

root = Tk()
root.title('Jarvis - Anthon Tacquet')
root.geometry("400x300")
root.iconbitmap('Anthon.ico')

def jarvis():
    os.system('Desktop-assistant.py')

def Jar():
    os.system('Jarvis.py')

myLabel = Label(root, text="Sart Jarvis assistant")
myLabel.pack()

myButton = Button(root, text= "Jarvis", command=jarvis)
myButton.pack()

myLabel = Label(root, text="Sart Jarvis text box")
myLabel.pack()

myButton = Button(root, text= "Jarvis", command=Jar)
myButton.pack()

myLabel = Label(root, text="You can follow me on github -Anthony Tacquet-")
myLabel.pack()

root.mainloop()
