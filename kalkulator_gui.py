import tkinter
from PIL import ImageTk, Image
from tkinter import ttk
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

        # output Frame -------------------------------------------------------
        self.outputFrameBd = tkinter.Frame(master, bg='grey', padx=1, pady=1)
        self.outputFrameBd.place(x=20, y=280)
        # self.outputFrame1 = ttk.Treeview(self.outputFrameBd)
        self.outputFrame1 = None
        # --------------------------------------------------------------------

        self.languageVar = tkinter.StringVar()
        self.languageBox = ttk.Combobox(master, textvariable=self.languageVar, values=('EN', 'PL'), width=3,
                                        state='readonly')
        self.languageBox.set("EN")
        self.languageBox.place(relx=0.92, rely=0.02)
        self.languageBox.bind('<<ComboboxSelected>>', self.callbackComboBox)
        self.languageDict = {'PL': ['Zatwierdź', 'Ilość Krokwi', 'Dystans "d" [cm]', "Znaczenie [cm]"],
                             "EN": ['Submit', "Rafters needed", 'Distance "d" [cm]', 'Marking [cm]']}

        master.bind('<Key>', self.keyCallback)



    def submit1(self):
        try:
            args = [
                float(self.p_entry.get()),
                float(self.w_entry.get()),
                float(self.d_min_entry.get()),
                float(self.d_max_entry.get()),
            ]
            self.outcome = RozmieszczenieKrokwi(args)
        except:
            return

        self.clearOutputFrame()
        self.fillData()

    def clearOutputFrame(self):
        # if 'self.outputFrame1' is already on the screan, destroy and create new one
        # otherwise no need to destroy
        if self.outputFrame1:
            self.outputFrame1.destroy()

        lang = self.languageBox.get()
        rows_num = len(self.outcome.wymiary)
        height = rows_num if rows_num <= 10 else 10

        self.outputFrame1 = ttk.Treeview(self.outputFrameBd, height=height)
        self.outputFrame1['columns'] = ('rafters', 'distance', 'marking')
        self.outputFrame1.column("#0", width=0, stretch='no')
        self.outputFrame1.column("rafters", anchor='center', width=100)
        self.outputFrame1.column("distance", anchor='center', width=110)
        self.outputFrame1.column("marking", anchor='center', width=90)

        self.outputFrame1.heading("#0", text="", anchor='center')
        self.outputFrame1.heading("rafters", text=self.languageDict[lang][1], anchor='center')
        self.outputFrame1.heading("distance", text=self.languageDict[lang][2], anchor='center')
        self.outputFrame1.heading("marking", text=self.languageDict[lang][3], anchor='center')
        self.outputFrame1.pack(fill='both')

        # color configuration ------
        self.outputFrame1.tag_configure('evenrow', background='#e9e9e9')
        style = ttk.Style()
        style.map('Treeview', background=[('selected', '#008ce2')])
        # --------------------------

        # scrollbar ----------------
        if rows_num > 10:
            scroll = tkinter.Scrollbar(self.outputFrameBd)
            scroll.config(command=self.outputFrame1.yview)
            # position hardcoded...
            scroll.place(relx=0.942, rely=0.11, relheight=0.88)
            self.outputFrame1['yscrollcommand'] = scroll.set
        # --------------------------
        # calling function which fills the rows from self.outcome
        self.fillData()

    def fillData(self):
        counter = 0
        for key, value in self.outcome.wymiary.items():
            dist = round(value[0], 2)
            draw = round(value[1], 2)
            if counter % 2 == 0:
                self.outputFrame1.insert(parent='', index='end', values=(key, dist, draw), tags = ('evenrow',))
            else:
                self.outputFrame1.insert(parent='', index='end', values=(key, dist, draw))
            counter += 1

    def callbackComboBox(self, event):
        lang = self.languageBox.get()
        self.master.focus()
        self.submitBtn['text'] = self.languageDict[lang][0]
        
        # if outputFrame1 already exists, change its headings
        if self.outputFrame1:
            self.outputFrame1.heading('rafters', text=self.languageDict[lang][1])
            self.outputFrame1.heading('distance', text=self.languageDict[lang][2])
            self.outputFrame1.heading('marking', text=self.languageDict[lang][3])

    def keyCallback(self, event):
        if event.keysym == 'Return':
            self.submit1()

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