import tkinter
from time import strftime
from tkinter import Label, Tk
from tkinter import *
# Configuring Main Window for App
print("welcome > form Tanvir Islam Baizid " )
# looks Good
# Very Cool
# dev-with-Python

window = Tk()
window.title("Tanvir digital-Clock")
window.geometry("600x300")
window.configure(bg="black")
window.resizable(False, False)


clock_label = Label(window, bg="black", fg="white", font = ("Times", 90, 'bold'), relief='flat')
clock_label.place(x = 20, y = 20)

label = Label(window, text="Tanvir Clock DEV-By---> Tanvir Islam Baizid", fg="black",   font = ("Times", 20, 'bold'), relief='flat')
label.place(x = 4,  y = 230)

text1= Label(window,text="About Me" )
text1.place(x=4,y=200)


def btn1():
  print("Show","Good Data")

button1 =  Button(window, text="Show on terminal", command=btn1)
button1.pack()



def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()