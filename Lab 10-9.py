import tkinter
import tkinter.messagebox
window=tkinter.Tk()
window.title('Alert Message GUI')
tkinter.messagebox.showinfo('Alert Message','This is just a Alert Message!')
response=tkinter.messagebox.askquestion('Simple Question','Do you love python?')
if response== 'yes':
    tkinter.Label(window,text='You love python!').pack()
else:
    tkinter.Label(window,text="You don't love python!").pack()
window.mainloop()
