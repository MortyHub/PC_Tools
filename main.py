from tkinter import *
import os

window = Tk()
window.title("PC Tools")

# Application open

def CPUWATCH():
    os.system('pythonw CPUWatcher.py')

# All The Actions
Lb = Label(window, text="PC Tools", font=("Times New Roman", 16), bg='#121212',fg='white')
Lb.place(x=200, y=50)

CPUWatcher = Button(window, text="CPU Watcher", font=("Times New Roman", 11), bg="#121212",fg='white',bd=0, command=CPUWATCH)
CPUWatcher.place(x=195, y=100)




window.configure(bg='#323232')
window.geometry("500x500")
window.mainloop()
