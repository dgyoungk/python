#program that uses checkbuttons to calculate total charges for maintenance

import tkinter as t

class Auto:
    def __init__(self):
        self.mainWindow = t.Tk()

        self.mainWindow.title("Joe's Automotive Estimates")

        self.checkFrame = t.Frame(self.mainWindow)
        self.displayFrame = t.Frame(self.mainWindow)
        self.buttonFrame = t.Frame(self.mainWindow)

        #checkFrame widgets: checkbuttons

        
        #IntVar() declarations to use with checkbuttons
        self.cbOil = t.IntVar()
        self.cbLube = t.IntVar()
        self.cbRadiator = t.IntVar()
        self.cbTransmission = t.IntVar()
        self.cbInspect = t.IntVar()
        self.cbMuffler = t.IntVar()
        self.cbTire = t.IntVar()

        #setting each checkbutton to unchecked state
        self.cbOil.set(0)
        self.cbLube.set(0)
        self.cbRadiator.set(0)
        self.cbTransmission.set(0)
        self.cbInspect.set(0)
        self.cbMuffler.set(0)
        self.cbTire.set(0)
                

        self.oil = t.Checkbutton(self.checkFrame,
                                 text="Oil Change",
                                 variable=self.cbOil)

        self.lube = t.Checkbutton(self.checkFrame,
                                 text="Lube Job",
                                 variable=self.cbLube)

        self.radiator = t.Checkbutton(self.checkFrame,
                                 text="Radiator Flush",
                                 variable=self.cbRadiator)

        self.transmission = t.Checkbutton(self.checkFrame,
                                 text="Transmission Flush",
                                 variable=self.cbTransmission)

        self.inspect = t.Checkbutton(self.checkFrame,
                                 text="Inspection",
                                 variable=self.cbInspect)

        self.muffler = t.Checkbutton(self.checkFrame,
                                 text="Muffler Replacement",
                                 variable=self.cbMuffler)

        self.tire = t.Checkbutton(self.checkFrame,
                                 text="Tire Rotation",
                                 variable=self.cbTire)



        self.oil.pack()
        self.lube.pack()
        self.radiator.pack()
        self.transmission.pack()
        self.inspect.pack()
        self.muffler.pack()
        self.tire.pack()

        #displayFrame widgets

        #StringVar declaration to hold the total charge variable
        self.totalCharge = t.StringVar()

        
        self.total = t.Label(self.displayFrame, text="Total: $")
        self.cost = t.Label(self.displayFrame, textvariable=self.totalCharge)

        self.total.pack(side='left', padx=5, pady=5)
        self.cost.pack(side='right', padx=5, pady=5)

        #buttonFrame widgets

        self.calcButton = t.Button(self.buttonFrame, text="Calculate",
                                   command=self.calcCost)
        self.quitButton = t.Button(self.buttonFrame, text="Quit",
                                   command=self.mainWindow.destroy)

        self.calcButton.pack(side='left', padx=5, pady=5)
        self.quitButton.pack(side='left', padx=5, pady=5)


        self.buttonFrame.pack()
        self.displayFrame.pack()
        self.checkFrame.pack()

        t.mainloop()
        
    #function that uses a series of if statement to determine whether a charge
    #for a service should be added
    def calcCost(self):
        
        #accumulator variable
        self.total = 0

        if self.cbOil.get() == 1:
            self.total += 30
        if self.cbLube.get() == 1:
            self.total += 20
        if self.cbRadiator.get() == 1:
            self.total += 40
        if self.cbTransmission.get() == 1:
            self.total += 100
        if self.cbInspect.get() == 1:
            self.total += 35
        if self.cbMuffler.get() == 1:
            self.total += 200
        if self.cbTire.get() == 1:
            self.total += 20

            
        #sets the value of the StrinVar variable
        self.totalCharge.set(str(self.total))



if __name__ == "__main__":
    Joe = Auto()
























        

        
