import tkinter
window=tkinter.Tk()
window.title('Playing with GUI')
tkinter.Label(window,text='Sufficient Width',fg='white',bg='purple').pack()
tkinter.Label(window,text='Taking all available X width',fg='white',bg='green').pack(fill='x')
tkinter.Label(window,text='Taking all available Y width',fg='white',bg='black').pack(side='left',fill='y')
window.mainloop()
