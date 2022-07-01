from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser


class notepad:
    file_name=""
    click=-1

    def select_color(self,op):
        color=colorchooser.askcolor()
        if op=="bg":
            print(color)
            self.NOTEPAD.config(bg=color[1])

        if op=="fg":
            self.NOTEPAD.tag_add("start",'sel.first','sel.last')
            self.NOTEPAD.tag_config("start",foreground=color[1])


    def OPEN(self):
        self.NOTEPAD.delete("1.0","end")
        self.file_name=filedialog.askopenfilename()
        self.window.title(self.file_name)
        self.file = open(self.file_name,"r")
        self.NOTEPAD.insert(INSERT,self.file.read())
        self.file.close()


    def SAVE(self):
        if self.file_name!="":
            self.file = open(self.file_name,"w")
            self.file.write(self.NOTEPAD.get("1.0","end"))
            self.file.close()
            self.window.title(self.file_name)

        else:
            self.SAVEAS()


    def NEW(self):
        if self.file_name!="":
            a=messagebox.askyesnocancel("YES/NO","DO YOU WANT TO SAVE?")
            if a== True:
                self.SAVE()
            elif a == False:
                self.NOTEPAD.delete("1.0","end")
                self.window.title("@B-NOTEPAD")

            else:
                pass


    def SAVEAS(self):
        self.file_name=filedialog.asksaveasfilename(defaultextension='.txt')
        print(self.file_name)
        self.file=open(self.file_name,"w")
        self.file.write(self.NOTEPAD.get("1.0","end"))
        self.file.close()
        self.window.title(self.file_name)


    def move(self):
        self.click=self.click+1
        if self.click%2==0:
            self.label_frame1.place(x=0,y=0)

        else:
            self.label_frame1.place(x=0,y=-100)






    def __init__(self,win):
        self.window=win
        self.window.title("@b-NOTEPAD")
        self.NOTEPAD=Text(self.window,padx=10,pady=20,wrap="word",selectbackground="grey")
        self.NOTEPAD.pack(fill=BOTH,expand=1) #it is use to set the notepad according to the window size

        self.label_frame1=LabelFrame(self.window,text="OPERATION",bg="black",fg="white",font=("elephant","10"))
        self.menu=Button(self.window,text="==",bg="green",command=self.move)
        self.menu.place(x=200,y=-10)
        self.label_frame1.place(x=0,y=-100)
        self.new=Button(self.label_frame1,text="New",command=self.NEW).grid(row=0,column=0,padx=5,pady=5)
        self.open= Button(self.label_frame1, text="open", command=self.OPEN).grid(row=0, column=1, padx=5, pady=5)
        self.save = Button(self.label_frame1, text="Save", command=self.SAVE).grid(row=0, column=2, padx=5, pady=5)
        self.saveas= Button(self.label_frame1, text="Saveas", command=self.SAVEAS).grid(row=0, column=3, padx=5, pady=5)
        self.exit = Button(self.label_frame1, text="Exit", command=self.window.destroy).grid(row=0, column=4, padx=5, pady=5)
        self.notepad_bg= Button(self.label_frame1,text="change bg",command=lambda:self.select_color("bg")).grid(row=1,column=0,padx=5,pady=5,columnspan=2)
        self.notepad_fg = Button(self.label_frame1, text="change fg", command=lambda: self.select_color("fg")).grid(
            row=1, column=3, padx=5, pady=5, columnspan=2)

if __name__=="__main__":
    win=Tk()
    notepad_obj=notepad(win)
    win.mainloop()

