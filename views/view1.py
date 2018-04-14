from tkinter import *
from tkinter import messagebox

class ATM:
    def __init__(self,master):
        self.color1 = '#000447'
        self.color2 = '#e2fbff'
        self.login = False
        self.master = master
        self.header = Label(self.master,text="JANALA BANK",bg=self.color1 ,fg="white",font=("arial",15,"bold"))
        self.header.pack(fill=X)


        self.frame = Frame(self.master, bg="#e2fbff", width=600, height=400)
        self.frame.pack()
        self.Login()

    def Login(self):
        self.Clear()
        self.frame = Frame(self.master,bg="#e2fbff",width=600,height=400)
        #create elements
        self.userlabel =Label(self.frame,text="Account Number",bg=self.color2)
        self.uentry = Entry(self.frame)

        #events
        self.loginBut = Button(self.frame,text="LOGIN",bg=self.color1,fg="white",command=self.Password)

        #place on frame
        self.userlabel.place(x=125,y=150,width=120,height=20)
        self.uentry.place(x=250,y=150,width=200,height=20)
        self.loginBut.place(x=325,y=230,width=120,height=20)
        self.frame.pack()

    def Password(self):
        self.Clear()
        self.frame = Frame(self.master, bg="#e2fbff", width=600, height=400)
        # create elements
        self.passLabel = Label(self.frame, text="Password", bg=self.color2)
        self.passInp = Entry(self.frame, show="*")

        # events
        self.loginBut = Button(self.frame, text="LOGIN", bg=self.color1, fg="white", command=self.SelectAcount)
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)

        # place on frame
        self.passLabel.place(x=125, y=150, width=120, height=20)
        self.passInp.place(x=250, y=150, width=200, height=20)
        self.loginBut.place(x=325, y=230, width=120, height=20)
        self.quitBut.place(x=450, y=360, width=120, height=20)
        self.frame.pack()



    def MainMenu(self):
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=250)
        #make
        self.detailBut = Button(self.frame, text="Account Details", bg=self.color1, fg="white", command=self.Details)
        self.logBut = Button(self.frame, text="Transaction Log", bg=self.color1, fg="white", command=self.Logs)
        self.depositBut = Button(self.frame, text="Deposit Money", bg=self.color1, fg="white", command=self.Deposit)
        self.withdrawBut = Button(self.frame, text="Withdraw Money", bg=self.color1, fg="white" ,command=self.Withdraw)
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        #place
        self.detailBut.place(x=25, y=25, width=200, height=50)
        self.logBut.place(x=25, y=125, width=200, height=50)
        self.depositBut.place(x=375, y=25, width=200, height=50)
        self.withdrawBut.place(x=375, y=125, width=200, height=50)
        self.quitBut.place(x=240, y=225, width=120, height=20)
        self.frame.pack()

    def Withdraw(self):
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=250)
        #master.geometry("800x400")
        # make
        self.WBut20 = Button(self.frame, text="$20", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.WBut40 = Button(self.frame, text="$40", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.WBut60 = Button(self.frame, text="$60", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.WBut80 = Button(self.frame, text="$80", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.WBut100 = Button(self.frame, text="$100", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.WBut150 = Button(self.frame, text="$150", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.WBut200 = Button(self.frame, text="$200", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.WButChoice = Button(self.frame, text="Other", bg=self.color1, fg="white", command=self.WithdrawOther)

        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        self.backBut = Button(self.frame, text="Back", bg=self.color1, fg="white", command=self.MainMenu)
        # place
        self.WBut20.place(x=25, y=60, width=200, height=30)
        self.WBut40.place(x=25, y=100, width=200, height=30)
        self.WBut60.place(x=25, y=140, width=200, height=30)
        self.WBut80.place(x=25, y=180, width=200, height=30)
        self.WBut100.place(x=375, y=60, width=200, height=30)
        self.WBut150.place(x=375, y=100, width=200, height=30)
        self.WBut200.place(x=375, y=140, width=200, height=30)
        self.WButChoice.place(x=375, y=180, width=200, height=30)

        self.quitBut.place(x=25, y=10, width=100, height=25)
        self.backBut.place(x=475, y=10, width=100, height=25)
        self.frame.pack()

    def Deposit(self):
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=250)
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor=self.color1)
        self.submitButton = Button(self.frame, text="Submit", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        self.backBut = Button(self.frame, text="Back", bg=self.color1, fg="white", command=self.MainMenu)
        #place
        self.money_box.place(x=200, y=100, width=200, height=20)
        self.submitButton.place(x=445, y=100, width=55, height=20)
        self.quitBut.place(x=25, y=10, width=100, height=25)
        self.backBut.place(x=475, y=10, width=100, height=25)

        self.frame.pack()

    def Logs(self, logs='string'):
        #last 20
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=400)
        #create
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        self.backBut = Button(self.frame, text="Back", bg=self.color1, fg="white", command=self.MainMenu)
        self.logs = Label(self.frame, text=logs, bg=self.color2, fg="Black")
        #place
        self.quitBut.place(x=25, y=10, width=100, height=25)
        self.backBut.place(x=475, y=10, width=100, height=25)
        self.logs.place(x=100, y=75, width=400, height=300)

        self.frame.pack()

    def Details(self, description='string'):
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=400)

        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        self.backBut = Button(self.frame, text="Back", bg=self.color1, fg="white", command=self.MainMenu)
        self.details = Label(self.frame, text=description, bg=self.color2, fg="Black")

        self.quitBut.place(x=25, y=10, width=100, height=25)
        self.backBut.place(x=475, y=10, width=100, height=25)
        self.details.place(x=100, y=75, width=400, height=300)

        self.frame.pack()

    def WithdrawOther(self):
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=250)
        #create
        self.money_box = Entry(self.frame, bg="honeydew", highlightcolor=self.color1)
        self.submitButton = Button(self.frame, text="Submit", bg=self.color1, fg="white", command=self.GoToConfirm)
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        self.backBut = Button(self.frame, text="Back", bg=self.color1, fg="white", command=self.MainMenu)
        # place
        self.money_box.place(x=200, y=100, width=200, height=20)
        self.submitButton.place(x=445, y=100, width=55, height=20)
        self.quitBut.place(x=25, y=10, width=100, height=25)
        self.backBut.place(x=475, y=10, width=100, height=25)

        self.frame.pack()

    def SelectAcount(self):
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=300)
        #create
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        self.savingsBut = Button(self.frame, text="Savings", bg=self.color1, fg="white", command=self.MainMenu)
        self.chequingBut = Button(self.frame, text="chequing", bg=self.color1, fg="white", command=self.MainMenu)
        # place
        self.quitBut.place(x=25, y=10, width=100, height=25)
        self.savingsBut.place(x=250, y=100, width=100, height=25)
        self.chequingBut.place(x=250, y=200, width=100, height=25)

        self.frame.pack()

    def Confirm(self, message):
        self.Clear()
        self.frame = Frame(self.master, bg=self.color2, width=600, height=250)
        # create
        self.text_widget = Label(self.frame, font=75, text=message, bg=self.color2, highlightcolor=self.color1)
        self.continueBut = Button(self.frame, text="Continue Banking", bg=self.color1, fg="white", command=self.MainMenu)
        self.quitBut = Button(self.frame, text="Quit", bg=self.color1, fg="white", command=self.Login)
        # place
        self.text_widget.place(x=200, y=100, width=200, height=40)
        self.continueBut.place(x=445, y=200, width=125, height=20)
        self.quitBut.place(x=25, y=200, width=75, height=20)

        self.frame.pack()

    def Clear(self):
        self.frame.destroy()

    def GoToConfirm(self):
        message = 'string'
        self.Confirm(message)


if __name__ == '__main__':
    master = Tk()
    master.title("Sign In")
    #master.geometry("600x420")
    # icon = PhotoImage(file="icon.png")
    # master.tk.call("wm",'iconphoto',master._w,icon)
    obj = ATM(master)
    master.mainloop()