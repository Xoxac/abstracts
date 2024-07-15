import tkinter as tk

root = tk.Tk()
root.geometry('700x150+500+400')
root.title('Калкулатор для богатих')
f = 'Arial 15'


def entryStavka_click(event):
    entryStavka.configure(state=tk.NORMAL)
    entryStavka.delete(0, tk.END)

    # make the callback only work once
    entryStavka.unbind('<Button-1>', entryStavka_click_id)


def click():
    god = int(entryTime.get())
    proc = int(entryStavka.get())/100
    amo = int(entryCash.get())
    cou = 0
    while cou < god:
        amo += amo * proc
        cou += 1
    result = str(round(amo, 2))
    res.configure(text=result)
    res.pack()


frameStavka = tk.Frame(root)
frameStavka.pack(side=tk.LEFT)
labelStavka = tk.Label(frameStavka, text='Годовая ставка:', font=f)
labelStavka.pack(side=tk.LEFT)
entryStavka = tk.Entry(frameStavka, width=3, justify=tk.CENTER, font=f)
entryStavka.pack()
entryStavka.insert(0, "%")
entryStavka.configure(state=tk.DISABLED)
entryStavka_click_id = entryStavka.bind('<Button-1>', entryStavka_click)

frameCash = tk.Frame(root)
frameCash.pack(side=tk.RIGHT)
labelCash = tk.Label(frameCash, text='Взнос:', font=f)
labelCash.pack(side=tk.LEFT)
entryCash = tk.Entry(frameCash, width=10, font=f, justify=tk.CENTER)
entryCash.pack()

frameTime = tk.Frame(root)
frameTime.pack()
labelTime = tk.Label(frameTime, text='Длительность:', font=f)
labelTime.pack()
entryTime = tk.Entry(frameTime, width=2, justify=tk.CENTER, font=f)
entryTime.pack()

button = tk.Button(root, text='<->', font='Arial 10', command=click)
button.pack()
ex = tk.Button(root, text='×', font='Arial 15', command=exit)
ex.place(relx=0.95, rely=0.05)
res = tk.Label(root, font=f)

root.mainloop()
