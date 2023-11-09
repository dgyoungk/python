#window that adds a user, only accessed from adminWindow.py
#label and entry for username and password
#open a text file for appending to, get the values from entry
#and append them to the text file


import tkinter as t
import tkinter.messagebox as msg


#filename constant
FILENAME = "users.txt"

class NewUser:
    def __init__(self):
        #constants for window dimensions
        self.__WINDOW_WIDTH = 600
        self.__WINDOW_HEIGHT = 600

        self.mainWindow = t.Tk()

        
        #set default window size
        self.mainWindow.geometry(str(self.__WINDOW_WIDTH) +
                                 "x" + str(self.__WINDOW_HEIGHT))

        #set window title
        self.mainWindow.title("ATM Simulator: Add User (Admin Only)")

        #set window header and pack it
        self.header = t.Label(self.mainWindow,
                              text="Enter Username and Password to add")

        self.header.pack(side="top", pady=15)

        #frames
        self.inputFrame = t.Frame(self.mainWindow)
        self.buttonFrame = t.Frame(self.mainWindow)

        #variables for username and password
        self.username = t.StringVar()
        self.password = t.StringVar()

        #LABELS AND ENTRIES FOR USERNAME AND PASSWORD
        self.user = t.Label(self.inputFrame, text="Username:")
        self.userEntry = t.Entry(self.inputFrame, textvariable=self.username)
        
        self.pw = t.Label(self.inputFrame, text="Password:")
        self.pwEntry = t.Entry(self.inputFrame, textvariable=self.password)

        self.user.pack()
        self.userEntry.pack(pady=10)
        self.pw.pack()
        self.pwEntry.pack(pady=10)

        #add and quit buttons
        self.add = t.Button(self.buttonFrame, text="Add",
                              command=self.addUser)
        self.exit = t.Button(self.buttonFrame, text="Exit",
                             command=self.mainWindow.destroy)

        self.add.pack(side='left', padx=5, pady=5)
        self.exit.pack(side='left', padx=5, pady=5)


        #pack frames
        self.inputFrame.pack()
        self.buttonFrame.pack()


        t.mainloop()

    def addUser(self):
        userList = []
        try:
            output = open(FILENAME, "a")
            inf = open(FILENAME, "r")

            self.newUser = self.userEntry.get()
            self.newPw = self.pwEntry.get()

            users = inf.readlines()

            for user in users:
                userList.append(user.rstrip("\n"))
            
            if self.newUser in userList:
                msg.showinfo("Error", "That user already exists")
                self.username.set("")
                self.password.set("")
            else:
                output.write(self.newUser + "\n")
                output.write(self.newPw + "\n")
                msg.showinfo("Success", "New User Successfully Added")
                self.username.set("")
                self.password.set("")

            

            output.close()
            inf.close()
            
        except IOError as err:
            msg.showInfo("IOError", err)


if __name__ == "__main__":
    new = NewUser()

        

        
        
