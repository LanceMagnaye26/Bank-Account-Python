from tkinter import *
from tkinter import messagebox

class Bank:
    def __init__(self,master):
        self.color1 = '#000447'
        self.color2 = '#e2fbff'
        self.login = False
        self.master = master
        self.header = Label(self.master,text="JANALA BANK",bg=self.color1 ,fg="white",font=("arial",15,"bold"))
        self.header.pack(fill=X)
        self.Login()

    def Login(self):
        self.frame = Frame(self.master,bg="#e2fbff",width=600,height=400)
        #create elements
        self.userlabel =Label(self.frame,text="Account Number",bg=self.color2)
        self.uentry = Entry(self.frame)
        self.passLabel = Label(self.frame, text="Password",bg=self.color2)
        self.passInp = Entry(self.frame,show="*")

        #events
        self.loginBut = Button(self.frame,text="LOGIN",bg=self.color1,fg="white",command=self.verify)
        self.quitBut = Button(self.frame,text="Quit",bg=self.color1,fg="white",command = self.master.quit)

        #place on frame
        self.userlabel.place(x=125,y=120,width=120,height=20)
        self.uentry.place(x=250,y=120,width=200,height=20)
        self.passLabel.place(x=125,y=180,width=120,height=20)
        self.passInp.place(x=250,y=180,width=200,height=20)
        self.loginBut.place(x=325,y=230,width=120,height=20)
        self.quitBut.place(x=450,y=360,width=120,height=20)
        self.frame.pack()

    def verify(self):
        message = "Login SucessFull"
        messagebox._show("Login Info", message)
        self.frame.destroy()
        self.MainMenu()

    def MainMenu(self):
        self.frame = Frame(self.master, bg=self.color2, width=600, height=250)
        #make
        self.detailBut = Button(self.frame, text="Account Details", bg=self.color1, fg="white")
        self.logBut = Button(self.frame, text="Transaction Log", bg=self.color1, fg="white")
        self.depositBut = Button(self.frame, text="Deposit Money", bg=self.color1, fg="white")
        self.withdrawBut = Button(self.frame, text="Withdraw Money", bg=self.color1, fg="white")
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.master.quit)
        #place
        self.detailBut.place(x=25, y=25, width=200, height=50)
        self.logBut.place(x=25, y=125, width=200, height=50)
        self.depositBut.place(x=375, y=25, width=200, height=50)
        self.withdrawBut.place(x=375, y=125, width=200, height=50)
        self.quitBut.place(x=240, y=225, width=120, height=20)
        self.frame.pack()

    def Withdraw(self):
        pass

    def Deposit(self):
        pass

    def Logs(self):
        pass

    def details(self):
        pass

master = Tk()
master.title("Sign In")
#master.geometry("600x420")
icon = PhotoImage(file="icon.png")
master.tk.call("wm",'iconphoto',master._w,icon)
obj = Bank(master)
master.mainloop()