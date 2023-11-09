#program that asseses property taxes based on the assessment value of a property
#assessment value: 60% of actual property value
#tax rate: $.75 for every $100 of the assess. value, so 0.0075 for every dollar

#get actual property value as input using Entry, then display assess. value
#and property tax


import tkinter as t

class PropertyTax:
    def __init__(self):
        self.mainWindow = t.Tk()

        self.mainWindow.title("Property Assessment")

        #frames for input, display, and buttons
        self.inputFrame = t.Frame(self.mainWindow)
        self.displayFrame = t.Frame(self.mainWindow)
        self.buttonFrame = t.Frame(self.mainWindow)


        #inputFrame widgets: a label and an entry
        self.valueLabel = t.Label(self.inputFrame, text="Enter the property value:")
        self.valueEntry = t.Entry(self.inputFrame, width=10)

        #packing widgets for display
        self.valueLabel.pack(side='left', ipadx=2, ipady=2, pady=5)
        self.valueEntry.pack(side='right', ipadx=1, ipady=1, pady=5)

        #displayFrame widgets: 4 labels, 2 headers, 2 data display

        #StringVars to hold the calculated values
        self.assessment = t.StringVar()
        self.taxes = t.StringVar()
        
        self.assess = t.Label(self.displayFrame, text="Assessment Value: $")
        self.assessValue = t.Label(self.displayFrame, textvariable=self.assessment)

        self.tax = t.Label(self.displayFrame, text="Property Tax: $")
        self.taxValue = t.Label(self.displayFrame, textvariable=self.taxes)

        #pack widgets for display
        self.assess.pack()
        self.assessValue.pack()
        self.tax.pack()
        self.taxValue.pack()

        #buttonFrame widgets: 3 buttons, 1 for assess, 1 for tax, 1 for quit

        self.assessButton = t.Button(self.buttonFrame, text="Assess",
                                     command=self.calcAssess)
        self.taxButton = t.Button(self.buttonFrame, text="Calculate Tax",
                                  command=self.calcTax)
        self.quitButton = t.Button(self.buttonFrame, text="Quit",
                                   command=self.mainWindow.destroy)

        #pack widgets for display
        self.assessButton.pack(side='left', padx=5)
        self.taxButton.pack(side='left', padx=5)
        self.quitButton.pack(side='right')


        #pack frames for display
        self.inputFrame.pack()
        self.displayFrame.pack()
        self.buttonFrame.pack()

        #loop to keep the window running
        t.mainloop()

    #function to calculate assessment value
    def calcAssess(self):
        self.propValue = float(self.valueEntry.get())

        self.assessmentValue = self.propValue * 0.6

        #set assess value StringVar
        self.assessment.set(str(self.assessmentValue))

    #function to calculate the property tax
    def calcTax(self):
        self.assValue = float(self.assessment.get())

        self.taxAmt = self.assValue * 0.0075
        
        #set tax StringVar
        self.taxes.set(str(self.taxAmt))


if __name__ == "__main__":
    Dan = PropertyTax()

        

        
        
