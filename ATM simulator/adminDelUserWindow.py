#window that deletes a user, only accessed from adminWindow.py
#label and entry for username and password
#open a text file for writing to, get the values from entry
#create a temporary file to replace the file contents except the one to delete
#delete the original file and rename the temp file

import tkinter as t
import tkinter.messagebox as msg
import os

#filename constant
FILENAME = "users.txt"

class DelUser:
    def __init__(self):
        #constants for window dimensions
        self.__WINDOW_WIDTH = 600
        self.__WINDOW_HEIGHT = 600

        self.mainWindow = t.Tk()

        
        #set default window size
        self.mainWindow.geometry(str(self.__WINDOW_WIDTH) +
                                 "x" + str(self.__WINDOW_HEIGHT))

        #set window title
        self.mainWindow.title("ATM Simulator: Delete User (Admin Only)")

        #set window header and pack it
        self.header = t.Label(self.mainWindow,
                              text="Enter User to remove")

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

        self.user.pack()
        self.userEntry.pack(pady=10)

        #remove and quit buttons
        self.remove = t.Button(self.buttonFrame, text="Delete",
                              command=self.removeUser)
        self.exit = t.Button(self.buttonFrame, text="Exit",
                             command=self.mainWindow.destroy)

        self.remove.pack(side='left', padx=5, pady=5)
        self.exit.pack(side='left', padx=5, pady=5)


        #pack frames
        self.inputFrame.pack()
        self.buttonFrame.pack()

        t.mainloop()

    def removeUser(self):
        try:
            found = False

            self.search = self.userEntry.get()
            
            userFile = open(FILENAME, "r")
            tempFile = open("temp.txt", "a")

            fileUsername = userFile.readline()

            while fileUsername != "":
                filePassword = userFile.readline()
                filePassword = filePassword.rstrip("\n")
                fileUsername = fileUsername.rstrip("\n")

                if fileUsername != self.search:
                    tempFile.write(f"{fileUsername}\n")
                    tempFile.write(f"{filePassword}\n")
                else:
                    found = True

                fileUsername = userFile.readline()

            userFile.close()
            tempFile.close()

            os.remove(FILENAME)
            os.rename("temp.txt", FILENAME)

            if found:
                msg.showinfo("Success", "The user has been removed")
            else:
                msg.showinfo("Error", "The user was not found")

        except IOError as err:
            msg.showinfo("IOError", err)
            

if __name__ == "__main__":
    remove = DelUser()
