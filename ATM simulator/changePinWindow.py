#window for depositing
#validation to make sure deposit amount is a number
#upon successful deposit, show deposit amount
#and new current balance

import tkinter as t
import tkinter.messagebox as msg
import accountWindow
import os


#constant for filename
FILENAME = "users.txt"

class ChangePin:
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
        self.mainWindow.title("CA-PYTDE ATM: Change PIN")

        #set window header and pack it
        self.header = t.Label(self.mainWindow,
                              text="Change PIN Below:")
        self.header.pack(side="top", pady=15)

        #variable to hold the username used in loginWindow
        self.username = username

        #variable to hold the user dict from loginWindow
        self.users = users

        #frames
        self.inputFrame = t.Frame(self.mainWindow)
        self.buttonFrame = t.Frame(self.mainWindow)

        #variables for inputFrame
        self.oldPinInput = t.StringVar()
        self.newPinInput = t.StringVar()

        #inputFrame widgets
        self.oldLabel = t.Label(self.inputFrame, text="Old PIN:")
        self.oldEntry = t.Entry(self.inputFrame, width=10,
                                textvariable=self.oldPinInput)

        self.newLabel = t.Label(self.inputFrame, text="New PIN:")
        self.newEntry = t.Entry(self.inputFrame, width=10,
                                textvariable=self.newPinInput)

        self.oldLabel.pack()
        self.oldEntry.pack()
        self.newLabel.pack()
        self.newEntry.pack()
        

        #buttonFrame widgets
        self.change = t.Button(self.buttonFrame, text="Submit",
                                command=self.changePin)
        self.exit = t.Button(self.buttonFrame, text="Back",
                             command=self.goToAtm)

        self.change.pack(side='left')        
        self.exit.pack(side='left',padx=10)

        #pack frames
        self.inputFrame.pack(pady=10)
        self.buttonFrame.pack()

        t.mainloop()

    def changePin(self):
        self.oldPin = self.oldEntry.get()
        self.newPin = self.newEntry.get()

        if self.users[self.username] == self.oldPin:
            try:
                inf = open(FILENAME, "r")
                tempFile = open("temp.txt", "w")

                userID = inf.readline()
                while userID != "":                    
                    password = inf.readline()
                    password = password.rstrip('\n')
                    userID = userID.rstrip('\n')

                    if password == self.oldPin:
                        tempFile.write(f"{userID}\n")
                        tempFile.write(f"{self.newPin}\n")
                    else:
                        tempFile.write(f"{userID}\n")
                        tempFile.write(f"{password}\n")
                        
                    userID = inf.readline()

                inf.close()
                tempFile.close()

                os.remove(FILENAME)
                os.rename("temp.txt", FILENAME)

                
                msg.showinfo("Success", "Your PIN has been changed")
                self.oldPinInput.set("")
                self.newPinInput.set("")

            except Exception as err:
                msg.showinfo("Oops!", err)
                self.oldPinInput.set("")
                self.newPinInput.set("")

            except:
                msg.showinfo("Error", "An error has occurred while updating")
                self.oldPinInput.set("")
                self.newPinInput.set("")
                                
        else:
            msg.showinfo("Error", "Your password was not found, try again")
            self.oldPinInput.set("")
            self.newPinInput.set("")
                

    def goToAtm(self):
        self.mainWindow.destroy()
        atm = accountWindow.ATM(self.username, self.top, self.users)

if __name__ == "__main__":
    depo = ChangePin()
