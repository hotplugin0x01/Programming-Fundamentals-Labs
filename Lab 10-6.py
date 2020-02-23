import tkinter
window=tkinter.Tk()
window.title('Capturing Mouse Events on GUI')
def left_click(event):
    tkinter.Label(window,text='Left Click!').pack()
def mid_click(event):
    tkinter.Label(window,text='Middle Click!').pack()
def right_click(event):
    tkinter.Label(window,text='Right Click!').pack()
window.bind('<Button-1>',left_click)
window.bind('<Button-2>',mid_click)
window.bind('<Button-3>',right_click)
window.mainloop()
