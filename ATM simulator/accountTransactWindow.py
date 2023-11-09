#window for depositing
#validation to make sure deposit amount is a number
#upon successful deposit, show deposit amount
#and new current balance

import tkinter as t
import tkinter.messagebox as msg
import accountWindow

class Deposit:
    def __init__(self, username, accountWindow, users):

        #constants for dimensions
        self.__WINDOW_WIDTH = 200
        self.__WINDOW_HEIGHT = 200

        self.top = accountWindow
        
        self.mainWindow = t.Toplevel(self.top)

        

        #set default window size
        self.mainWindow.geometry(str(self.__WINDOW_WIDTH) +
                                 "x" + str(self.__WINDOW_HEIGHT))

        #set window title
        self.mainWindow.title("CA-PYTDE ATM: Deposit")

        #set window header and pack it
        self.header = t.Label(self.mainWindow,
                              text="Enter Deposit Amount Below:")
        self.header.pack(side="top", pady=10)

        #variable to hold the username used in loginWindow
        self.username = username

        #variable to hold the dict of users from loginWindow
        self.users = users

        #frames
        self.inputFrame = t.Frame(self.mainWindow)
        self.buttonFrame = t.Frame(self.mainWindow)

        #variable for inputFrame Entry widget
        self.depAmt = t.StringVar()

        #inputFrame widgets
        self.depLabel = t.Label(self.inputFrame, text="Amount:")
        self.depEntry = t.Entry(self.inputFrame, width=10,
                                textvariable=self.depAmt)

        self.depLabel.pack()
        self.depEntry.pack()

        #buttonFrame widgets
        self.deposit = t.Button(self.buttonFrame, text="Deposit",
                                command=self.makeDeposit)
        self.exit = t.Button(self.buttonFrame, text="Back",
                             command=self.goToAtm)

        self.deposit.pack(side='left')        
        self.exit.pack(side='left',padx=10)

        #pack frames
        self.inputFrame.pack(pady=10)
        self.buttonFrame.pack()

        t.mainloop()

    def makeDeposit(self):
        self.amount = self.depEntry.get()
        try:

            output = open(self.username + ".txt", "a")
            inf = open(self.username + ".txt", "r")

            balance = inf.readlines()

            if balance == "":
                output.write(self.amount + "\n")
                self.depAmt.set("")
                msg.showinfo("Success", "Transaction Complete")
                                              
            else:
                for index in range(len(balance)):
                    balance[index] = balance[index].rstrip('\n')

                depositAmt = float(self.amount)
                currBal = float(balance[-1])

                updatedBal = currBal + depositAmt

                output.write(str(updatedBal) + "\n")
                self.depAmt.set("")

                msg.showinfo("Success", "Transaction Complete")

                
            output.close()
            inf.close()
            self.mainWindow.destroy()
        except:
            msg.showinfo("Error", "An error occurred during the transaction")
             

    def goToAtm(self):
        atm = accountWindow.ATM(self.username, self.top, self.users)


class Withdraw:
    def __init__(self, username, accountWindow, users):
        
        #constants for dimensions
        self.__WINDOW_WIDTH = 200
        self.__WINDOW_HEIGHT = 200
        
        
        self.top = accountWindow
        
        self.mainWindow = t.Toplevel(self.top)

        #set default window size
        self.mainWindow.geometry(str(self.__WINDOW_WIDTH) +
                                 "x" + str(self.__WINDOW_HEIGHT))

        #set window title
        self.mainWindow.title("CA-PYTDE ATM: Withdrawal")

        #set window header and pack it
        self.header = t.Label(self.mainWindow,
                              text="Enter Withdrawal Amount Below:")
        self.header.pack(side="top", pady=10)

        #variable to hold the username used in loginWindow
        self.username = username

        #variable to hold the dict of users from loginWindow
        self.users = users

        #frames
        self.inputFrame = t.Frame(self.mainWindow)
        self.buttonFrame = t.Frame(self.mainWindow)

        #variable for inputFrame Entry widget
        self.drawAmt = t.StringVar()

        #inputFrame widgets
        self.drawLabel = t.Label(self.inputFrame, text="Amount:")
        self.drawEntry = t.Entry(self.inputFrame, width=10,
                                 textvariable=self.drawAmt)

        self.drawLabel.pack()
        self.drawEntry.pack()

        #buttonFrame widgets
        self.withdraw = t.Button(self.buttonFrame, text="Withdraw",
                                command=self.withdrawMoney)
        self.exit = t.Button(self.buttonFrame, text="Back",
                             command=self.goToAtm)

        self.withdraw.pack(side='left')        
        self.exit.pack(side='left',padx=10)

        #pack frames
        self.inputFrame.pack(pady=10)
        self.buttonFrame.pack()

        t.mainloop()

    def withdrawMoney(self):
        self.amount = self.drawEntry.get()
        withdrawAmt = float(self.amount)
        inf = open(self.username + ".txt", "r")
        
        output = open(self.username + ".txt", "a")

        balance = inf.readlines()
        if balance == "":
            msg.showinfo("Warning", "You have no balance in this account\n" +
                                     "Make a deposit first")
        else:
            for index in range(len(balance)):
                balance[index] = balance[index].rstrip('\n')
            currBal = float(balance[-1])
        
            if withdrawAmt % 10 != 0:
                msg.showinfo("Warning", "The withdrawal amount must be in multiples of 10")
                self.drawAmt.set("")
            elif withdrawAmt > 1000:
                msg.showinfo("Warning", "The maximum amount per withdrawal is $1000")
                self.drawAmt.set("")
            elif withdrawAmt > currBal:
                msg.showinfo("Warning", "The amount exceeds the current account balance")
                self.drawAmt.set("")
            else:
                updatedBal = currBal - withdrawAmt

                output.write(str(updatedBal) + '\n')
                self.drawAmt.set("")

                msg.showinfo("Success", "Transaction Complete")

        output.close()
        inf.close()
                 

    def goToAtm(self):
        self.mainWindow.destroy()
        atm = accountWindow.ATM(self.username, self.top, self.users)

if __name__ == "__main__":
    draw = Withdraw()
