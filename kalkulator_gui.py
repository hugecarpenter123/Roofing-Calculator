import tkinter

class Application():
    def __init__(self, master):
        self.master = master
        self.frame1 = tkinter.Frame(master, width=700, height=500, bg='#AC99F2')
        self.frame1.pack()


def main():
    root = tkinter.Tk()
    root.title('Roofing calculator')
    app = Application(root)
    root['padx'] = 5
    root['pady'] = 5
    root.mainloop()

if __name__ == '__main__':
    main()