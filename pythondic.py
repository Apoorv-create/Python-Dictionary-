from tkinter import *
root=Tk()
root.title("Dictionary")
root.geometry("600x400")

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)

dictionary = { 'Mutable' : 'Values that can be changed like a list',
              'Immutable': 'Value that can not be changed like a tuple', 
              'Tkinter' : 'It is the GUI library in python'
            }

def mutable():
     label_of_mutable["text"] = dictionary['Mutable']
     
def immutable():
    label_of_immutable["text"] = dictionary['Immutable']

def Tkinter():
    label_of_tkinter["text"] = dictionary['Tkinter']

button_mutable = Button(root, text = "The Defination Of Mutable is..", command =mutable)
button_mutable.place(relx  = 0.5, rely = 0.2, anchor=CENTER)

label_of_mutable.place(relx = 0.5, rely = 0.3, anchor=CENTER)

button_immutable = Button(root, text = "The Defination Of Immutable is..", command=immutable)
button_immutable.place(relx = 0.5, rely = 0.4, anchor=CENTER)

label_of_immutable.place(relx = 0.5, rely = 0.5, anchor=CENTER)

button_tkinter = Button(root, text = "The Defination Of Tkinter is...", command=Tkinter)
button_tkinter.place(relx = 0.5, rely = 0.6, anchor=CENTER)

label_of_tkinter.place(relx = 0.5, rely = 0.7, anchor=CENTER)

root.mainloop()