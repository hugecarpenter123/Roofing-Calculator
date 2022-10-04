import tkinter
from PIL import ImageTk, Image
from tkinter import font
from obliczenia_dekarskie import RozmieszczenieKrokwi


class Application():
    def __init__(self, master):
        self.master = master

        self.img = Image.open("images/rozstaw_krokiew_resized.png")
        self.bg = ImageTk.PhotoImage(self.img)
        self.label1 = tkinter.Label(master, image=self.bg, bd=0)
        self.label1.place(x=0, y=0, relwidth=1, relheight=1)
        self.bd = tkinter.Frame(master ,bg='grey', padx=1, pady=1)
        self.bd.place(x=20, y=20)
        # self.inputFrame1 = tkinter.Frame(master, height=20, width=20, padx=10, pady=10)
        # self.inputFrame1.place(x=20, y=20)
        self.inputFrame1 = tkinter.Frame(self.bd, height=20, width=20, padx=10, pady=10)
        self.inputFrame1.pack(fill='both')

        self.p_label = tkinter.Label(self.inputFrame1, font=('Arial', 15, 'normal'), text='p', anchor='w')
        self.p_label.grid(row=0, column=0, sticky='ew')
        self.p_entry = tkinter.Entry(self.inputFrame1, font=('Arial', 13, 'normal'), width=6)
        self.p_entry.grid(row=0, column=1)

        self.w_label = tkinter.Label(self.inputFrame1, font=('Arial', 15, 'normal'), text='w', anchor='w')
        self.w_label.grid(row=1, column=0, sticky='ew')
        self.w_entry = tkinter.Entry(self.inputFrame1, font=('Arial', 13, 'normal'), width=6)
        self.w_entry.grid(row=1, column=1)

        self.d_min_label = tkinter.Label(self.inputFrame1, font=('Arial', 15, 'normal'), text='d-min', anchor='w',)
        self.d_min_label.grid(row=2, column=0, sticky='ew', padx=(0,30))
        self.d_min_entry = tkinter.Entry(self.inputFrame1, font=('Arial', 13, 'normal'), width=6, bg='white')
        self.d_min_entry.grid(row=2, column=1)

        self.d_max_label = tkinter.Label(self.inputFrame1, font=('Arial', 15, 'normal'), text='d-max', anchor='w')
        self.d_max_label.grid(row=3, column=0, sticky='ew')
        self.d_max_entry = tkinter.Entry(self.inputFrame1, font=('Arial', 13, 'normal'), width=6)
        self.d_max_entry.grid(row=3, column=1)

        #adding 'cm' label to all 4 rows with loop
        for i in range(4):
            tkinter.Label(self.inputFrame1 ,font=('Arial', 13, 'normal'), text='cm').grid(row=i, column=2)

        self.submitBtn = tkinter.Button(self.inputFrame1, text='Submit', cursor='hand2', font=('Helvetica',12),
                                        activebackground='#e80202', bg='#d31633', fg='white', activeforeground='white',
                                        command=self.submit1)
        self.submitBtn.grid(row=4, column=0, columnspan=3, sticky='ew', pady=(10,0), padx=20)

        self.outputFrameBd = tkinter.Frame(master, bg='grey', padx=1, pady=1)
        self.outputFrameBd.place(x=20, y=270)
        self.outputFrame1 = tkinter.Frame(self.outputFrameBd, width=50, height=50)
        self.outputFrame1.pack(fill='both', expand=True)
        self.clearOutputFrame()



    def submit1(self):
        # self.d_calkowita, self.s_krokwi, self.o_przedzial_dolny, self.o_przedzial_gorny
        args = [
            float(self.p_entry.get()),
            float(self.w_entry.get()),
            float(self.d_min_entry.get()),
            float(self.d_max_entry.get()),
        ]
        self.outcome = RozmieszczenieKrokwi(args)
        self.clearOutputFrame()
        self.fillData()

    def clearOutputFrame(self):
        self.outputFrame1.destroy()
        self.outputFrame1 = tkinter.Frame(self.outputFrameBd)
        self.outputFrame1.pack(fill='both', expand=True)
        tkinter.Label(self.outputFrame1, font=('Arial', 10, 'normal'), text='Rafters needed', padx=4).grid(row=0, column=0)
        tkinter.Label(self.outputFrame1, font=('Arial', 10, 'normal'), text='Distance \'d\'', bg='lightgrey', padx=4).grid(row=0, column=1)
        tkinter.Label(self.outputFrame1, font=('Arial', 10, 'normal'), text='Drawing', padx=4).grid(row=0, column=2)

    def fillData(self):
        base_row = 1
        for key, value in self.outcome.wymiary.items():
            print('key: ', key, 'value:', value)




def main():
    root = tkinter.Tk()
    root.title('Roofing calculator')
    root.geometry('900x529')
    root.resizable(False, False)
    root['padx'] = 5
    root['pady'] = 5
    root['bg'] = 'white'

    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()