import tkinter as tk


class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('DB fill')
        self.geometry('800x600')

        self.label1 = tk.Label(self, text='Wybierz tabele:', font=('Arial', 18))
        self.label1.grid(row=0, column=0, columnspan=2)

        var = tk.IntVar()
        self.chk = tk.Checkbutton(self, text='krwiodawcy', font=('Arial', 16))
        self.chk.grid(row=1, column=1)
len
