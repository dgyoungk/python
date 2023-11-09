#window that diplays the atm options to the user
#deposit, withdrawal, show balance, change PIN, and exit
#exit should close the window and go back to the login window

import tkinter as t
import loginWindow
import tkinter.messagebox as msg
import accountTransactWindow
import changePinWindow

class ATM:
    def __init__(self, username, loginWindow, users):

        #constants for dimensions
        self.__WINDOW_WIDTH = 600
        self.__WINDOW_HEIGHT = 600
        
        
        self.accountWindow = t.Toplevel(loginWindow)

        #set default window size
        self.accountWindow.geometry(str(self.__WINDOW_WIDTH) +
                                 "x" + str(self.__WINDOW_HEIGHT))

        #set window title
        self.accountWindow.title("CA-PYTDE ATM")

        #set window header and pack it
        self.header = t.Label(self.accountWindow,
                              text="Welcome\nChoose an option from below:")
        self.header.pack(side="top", pady=15)

        #variable to hold the username used in loginWindow
        self.username = username

        #variable to hold the dict of users from loginWindow
        self.users = users

        #frames
        self.rbFrame = t.Frame(self.accountWindow)
        self.displayFrame = t.Frame(self.accountWindow)
        self.buttonFrame = t.Frame(self.accountWindow)

        #variable for radiobuttons
        self.rbVar = t.IntVar()

        #set rbVar
        self.rbVar.set(5)

        #rbFrame widgets
        self.depoRb = t.Radiobutton(self.rbFrame,
                                    text="Deposit",
                                    variable=self.rbVar,
                                    value=1,
                                    command=self.deposit)

        self.withRb = t.Radiobutton(self.rbFrame,
                                    text="Withdraw",
                                    variable=self.rbVar,
                                    value=2,
                                    command=self.withdraw)

        self.pinRb = t.Radiobutton(self.rbFrame,
                                   text="Change PIN",
                                   variable=self.rbVar,
                                   value=4,
                                   command=self.changePin)

        self.depoRb.pack(pady=10)
        self.withRb.pack(pady=10)
        self.pinRb.pack(pady=10)

        #displayFrame variables
        self.bal = t.StringVar()

        #displayFrame widgets
        self.balLabel = t.Label(self.displayFrame, text="Current Balance: $")
        self.currBal = t.Label(self.displayFrame, textvariable=self.bal)

        self.balLabel.pack()
        self.currBal.pack()


        #buttonFrame widgets
        self.balance = t.Button(self.buttonFrame, text="Show Balance",
                                command=self.displayBal)
        self.exit = t.Button(self.buttonFrame, text="Exit",
                             command=self.goToLogin)
        

        self.balance.pack(side='left', pady=15, padx=5)
        self.exit.pack(side='left', pady=15, padx=5)


        #pack frames
        self.rbFrame.pack()
        self.displayFrame.pack()
        self.buttonFrame.pack()

        t.mainloop()

    def deposit(self):
        depo = accountTransactWindow.Deposit(self.username,
                                             self.accountWindow,
                                             self.users)

    def withdraw(self):
        withdraw = accountTransactWindow.Withdraw(self.username,
                                                  self.accountWindow,
                                                  self.users)

    def displayBal(self):
        inf = open(self.username + ".txt", "r")
    
        balance = inf.readlines()
        for index in range(len(balance)):
            balance[index] = balance[index].rstrip("\n")

        
        self.bal.set(str(balance[len(balance) - 1]))
        

    def changePin(self):
        pin = changePinWindow.ChangePin(self.username,
                                        self.accountWindow,
                                        self.users)
        


    def goToLogin(self):
        self.accountWindow.destroy()
        login = loginWindow.Login()


if __name__ =="__main__":
    atm = ATM()
        
