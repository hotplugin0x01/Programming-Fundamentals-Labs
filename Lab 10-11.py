import tkinter
window=tkinter.Tk()
window.title('Image or Logo on GUI')
icon=tkinter.PhotoImage(file='logo.png')
label=tkinter.Label(window,image=icon).pack()
window.mainloop()
