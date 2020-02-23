import tkinter
window=tkinter.Tk()
window.title('Binding Functions')
def say_Assalam_o_Alaikum():
    tkinter.Label(window,text='Assalam o Alaikum').pack()
tkinter.Button(window,text='Click Me!',command=say_Assalam_o_Alaikum).pack()
window.mainloop()
