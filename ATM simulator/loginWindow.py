#the login GUI; upon successful login, will display either the user
#or admin GUI window

import tkinter as t
import tkinter.messagebox as msg
import adminWindow
import accountWindow

#constant for filename (I/O)
FILENAME = "users.txt"

#attempt tracker
attempts = 0

class Login:
    def __init__(self):

        #constants for dimensions
        self.__WINDOW_WIDTH = 600
        self.__WINDOW_HEIGHT = 600
        
        
        self.loginWindow = t.Tk()

        #set default window size
        self.loginWindow.geometry(str(self.__WINDOW_WIDTH) +
                                 "x" + str(self.__WINDOW_HEIGHT))

        #set window title
        self.loginWindow.title("CA-PYTDE ATM Simulator")

        #set window header and pack it
        self.header = t.Label(self.loginWindow,
                              text="ATM Simulator\nPlease login below")
        self.header.pack(side="top", pady=40)    

        #FRAMES
        self.mainFrame = t.Frame(self.loginWindow)
        self.buttonFrame = t.Frame(self.loginWindow)

        #variables for username and password values
        self.username = t.StringVar()
        self.password = t.StringVar()

        #LABELS AND ENTRIES FOR USERNAME AND PASSWORD
        self.user = t.Label(self.mainFrame, text="Username:")
        self.userEntry = t.Entry(self.mainFrame, width=10, textvariable=self.username)
        
        self.pw = t.Label(self.mainFrame, text="Password:")
        self.pwEntry = t.Entry(self.mainFrame, width=10, textvariable=self.password)

        self.user.pack()
        self.userEntry.pack(pady=10)
        self.pw.pack()
        self.pwEntry.pack(pady=10)

        #login and quit buttons
        self.login = t.Button(self.buttonFrame, text="Login",
                              command=self.attemptLogin)
        self.quit = t.Button(self.buttonFrame, text="Quit",
                             command=self.loginWindow.destroy)

        self.login.pack(side='left', padx=5, pady=5)
        self.quit.pack(side='left', padx=5, pady=5)


        #pack frames
        self.mainFrame.pack()
        self.buttonFrame.pack()

        t.mainloop()

    def attemptLogin(self):

        global attempts

        adminUser = "SysAdmin"
        adminPw = "1357"

        self.loginUser = self.userEntry.get()
        self.loginPw = self.pwEntry.get()

            
        userList = []
        self.userDict = {}

        try:
            userFile = open(FILENAME, "r")

            validUsers = userFile.readlines()

            #append all file content to a list
            for user in validUsers:
                userList.append(user.rstrip("\n"))

            #create a dictionary from list for validation
            for index in range(0, len(userList), 2):
                self.userDict[userList[index]] = userList[index + 1]

        
            if (len(self.loginUser) != 0 and len(self.loginPw) != 0):
                #validtation process
                if self.loginUser in self.userDict:
                    if self.userDict[self.loginUser] == self.loginPw:
                        self.account = accountWindow.ATM(self.loginUser,
                                                         self.loginWindow,
                                                         self.userDict)
                    else:
                        msg.showinfo("Error", "Invalid Username/Password\nTry again")
                        attempts += 1
                        self.username.set("")
                        self.password.set("")
                elif self.loginUser == adminUser and self.loginPw == adminPw:
                    self.loginWindow.destroy()
                    admin = adminWindow.Admin()
                else:
                    msg.showinfo("Error", "Invalid Username/Password\nTry again")
                    attempts += 1
                    self.username.set("")
                    self.password.set("")

                if attempts == 3:
                    msg.showinfo("Warning",
                                 "Maximum attempts reached\nProgram closing")
                    self.loginWindow.destroy()

            userFile.close()
                    
        except ValueError as err:
            msg.showinfo("ValueError", err)
            self.username.set("")
            self.password.set("")
        

if __name__ =="__main__":
    login = Login()
        
        
        
