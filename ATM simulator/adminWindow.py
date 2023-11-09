#window for the admins, functions: add user, delete user, exit
#radio buttons with callback function in each button for add/delete
#button for exit function


import tkinter as t
import tkinter.messagebox as msg
import adminAddUserWindow
import adminDelUserWindow
import loginWindow

class Admin:
    def __init__(self):

        #constants for window dimensions
        self.__WINDOW_WIDTH = 600
        self.__WINDOW_HEIGHT = 600

        self.mainWindow = t.Tk()

        
        #set default window size
        self.mainWindow.geometry(str(self.__WINDOW_WIDTH) +
                                 "x" + str(self.__WINDOW_HEIGHT))

        #set window title
        self.mainWindow.title("ATM Simulator: Admin Page")

        #set window header and pack it
        self.header = t.Label(self.mainWindow,
                              text="Welcome, Admin\nPlease Choose An Option")

        self.header.pack(side="top", pady=15)

        #frames
        self.radioFrame = t.Frame(self.mainWindow)
        self.buttonFrame = t.Frame(self.mainWindow)

        #variables for radio buttons
        self.rbVar = t.IntVar()

        #set rbVar
        self.rbVar.set(0)

        #radiobutton widgets
        self.addRb = t.Radiobutton(self.radioFrame,
                                   text="Add User",
                                   variable=self.rbVar,
                                   value=1,
                                   command=self.newUser)
        self.delRb = t.Radiobutton(self.radioFrame,
                                   text="Delete User",
                                   variable=self.rbVar,
                                   value=2,
                                   command=self.removeUser)

        self.addRb.pack(pady=5)
        self.delRb.pack(pady=5)

        #button widgets
        self.exit = t.Button(self.buttonFrame, text="Exit",
                             command=self.goToLogin)

        self.exit.pack(side='left', pady=15)

        #pack frames
        self.radioFrame.pack()
        self.buttonFrame.pack()

        t.mainloop()

    def newUser(self):
        self.mainWindow.destroy()
        newUser = adminAddUserWindow.NewUser()

    def removeUser(self):
        self.mainWindow.destroy()
        delUser = adminDelUserWindow.DelUser()

    def goToLogin(self):
        self.mainWindow.destroy()
        login = loginWindow.Login()
                                   





if __name__ == "__main__":
    admin = Admin()
