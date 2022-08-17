from tkinter import *
from time import strftime

def refresh():
    chour = strftime('%H')
    cmin = strftime('%M')
    csec = strftime('%S')
    timelabel = ''
    chour = int(chour)
    if chour >= 12:
        chour -= 12
        timelabel = 'PM'
    elif chour < 12:
        timelabel ='AM'
    if chour < 10:
        chour = str(chour)
        chour = '0'+chour
    timedisplay.config(text=f'{chour}:{cmin}:{csec} {timelabel}')
    root.after(1000, refresh)

root = Tk()
root.title('Digital Clock')
root.config(bg='black')
timedisplay = Label(root, font=('Terminal', 35), bg='black', fg='limegreen')
timedisplay.pack(padx=5,pady=5)
refresh()
root.mainloop()