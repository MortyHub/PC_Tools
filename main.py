from tkinter import *
from tkinter import messagebox
import os, psutil

window = Tk()
window.title("PC Tools")

# Application open

def CPUWATCH():
    os.system('pythonw CPUWatcher.py')

def DisplayCPU():
    return messagebox.showinfo('PC Tools', f'Your current CPU usage is {str(psutil.cpu_percent())}%')

# All The Actions
Lb = Label(window, text="PC Tools", font=("Times New Roman", 16), bg='#121212',fg='white')
Lb.place(x=200, y=50)

CPUWatcher = Button(window, text="CPU Watcher", font=("Times New Roman", 11), bg="#121212",fg='white',bd=0, command=CPUWATCH)
CPUWatcher.place(x=195, y=100)

CPUDisplayer = Button(window, text="CPU Displayer", font=("Times New Roman", 11), bg="#121212", fg='white', bd=0, command=DisplayCPU)
CPUDisplayer.place(x=192, y=150)



window.configure(bg='#323232')
window.geometry("500x500")
window.mainloop()
