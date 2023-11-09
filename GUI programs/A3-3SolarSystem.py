#program that draws the solar system using create_oval and create_line
#use X and Y constants for each planet?
#set the canvas size long and wide

import tkinter as t
import tkinter.font

class SolarSystem:
    def __init__(self):

        #constants
        #canvas dimensions
        self.__CAN_WIDTH = 1800
        self.__CAN_HEIGHT = 700

        #sun coords
        self.__SUN_X1 = 10
        self.__SUN_Y1 = 390
        self.__SUN_X2 = 210
        self.__SUN_Y2 = 590
        #mercury coords
        self.__MER_X1 = 250
        self.__MER_Y1 = 480
        self.__MER_X2 = 280
        self.__MER_Y2 = 510
        #venus coords
        self.__VEN_X1 = 320
        self.__VEN_Y1 = 470
        self.__VEN_X2 = 370
        self.__VEN_Y2 = 520
        #mars coords
        self.__MARS_X1 = 520
        self.__MARS_Y1 = 475
        self.__MARS_X2 = 560
        self.__MARS_Y2 = 515
        #jupiter coords
        self.__JUP_X1 = 680
        self.__JUP_Y1 = 410
        self.__JUP_X2 = 830
        self.__JUP_Y2 = 560
        #saturn coords
        self.__SAT_X1 = 950
        self.__SAT_Y1 = 420
        self.__SAT_X2 = 1080
        self.__SAT_Y2 = 550
        #uranus coords
        self.__URA_X1 = 1200
        self.__URA_Y1 = 435
        self.__URA_X2 = 1300
        self.__URA_Y2 = 535
        #neptune coords
        self.__NEP_X1 = 1350
        self.__NEP_Y1 = 435
        self.__NEP_X2 = 1450
        self.__NEP_Y2 = 535
        #pluto coords: =
        self.__PLT_X1 = 1500
        self.__PLT_Y1 = 475
        self.__PLT_X2 = 1520
        self.__PLT_Y2 = 495
        
        self.__DISTANCE = 100

        
        self.mainWindow = t.Tk()

        self.mainWindow.title("The Solar System")

        self.canvas = t.Canvas(self.mainWindow, width=self.__CAN_WIDTH,
                               height=self.__CAN_HEIGHT)

        #draws the sun
        self.canvas.create_oval(self.__SUN_X1,
                                self.__SUN_Y1,
                                self.__SUN_X2,
                                self.__SUN_Y2,
                                fill='yellow')
        #draws mercury
        self.canvas.create_oval(self.__MER_X1,
                                self.__MER_Y1,
                                self.__MER_X2,
                                self.__MER_Y2,
                                fill='orange')

        #draws venus
        self.canvas.create_oval(self.__VEN_X1,
                                self.__VEN_Y1,
                                self.__VEN_X2, 
                                self.__VEN_Y2,
                                fill='light blue')
        #draws earth
        self.canvas.create_oval(self.__VEN_X1 + self.__DISTANCE,
                                self.__VEN_Y1,
                                self.__VEN_X2 + self.__DISTANCE, 
                                self.__VEN_Y2,
                                fill='blue')

        #draws mars
        self.canvas.create_oval(self.__MARS_X1,
                                self.__MARS_Y1,
                                self.__MARS_X2, 
                                self.__MARS_Y2,
                                fill='red')

        #draws jupiter
        self.canvas.create_oval(self.__JUP_X1,
                                self.__JUP_Y1,
                                self.__JUP_X2, 
                                self.__JUP_Y2,
                                fill='maroon')

        #draws saturn
        self.canvas.create_oval(self.__SAT_X1,
                                self.__SAT_Y1,
                                self.__SAT_X2, 
                                self.__SAT_Y2,
                                fill='bisque')

        #draws uranus
        self.canvas.create_oval(self.__URA_X1,
                                self.__URA_Y1,
                                self.__URA_X2, 
                                self.__URA_Y2,
                                fill='light sky blue')

        #draws neptune
        self.canvas.create_oval(self.__NEP_X1,
                                self.__NEP_Y1,
                                self.__NEP_X2, 
                                self.__NEP_Y2,
                                fill='light gray')

        #draws pluto
        self.canvas.create_oval(self.__PLT_X1,
                                self.__PLT_Y1,
                                self.__PLT_X2, 
                                self.__PLT_Y2,
                                fill='dark green')
        
        #draws left arc on saturn
        self.canvas.create_arc(self.__SAT_X1 - self.__DISTANCE / 1.2,
                                self.__SAT_Y1 + 30,
                                self.__SAT_X2 + self.__DISTANCE * 4, 
                                self.__SAT_Y2 - 30, start=135, extent=90, style=t.ARC)

        #draws right arc on saturn
        self.canvas.create_arc(self.__SAT_X1 + self.__DISTANCE * 2.09,
                                self.__SAT_Y1 + 30,
                                self.__SAT_X2 - self.__DISTANCE * 5, 
                                self.__SAT_Y2 - 30, start=315, extent=90, style=t.ARC)

        #font variable
        myfont = tkinter.font.Font(family="Helvetica", size="16", weight="bold")


        #draws text on planets
        #sun
        self.canvas.create_text((self.__SUN_X2 / 2) + (self.__SUN_X1 / 2),
                                self.__SUN_Y2, text="Sun",
                                anchor=t.N, font=myfont)
        #mercury
        self.canvas.create_text((self.__MER_X2 / 2) + (self.__MER_X1 / 2),
                                self.__MER_Y2, text="Mercury",
                                anchor=t.N, font=myfont)

        #venus
        self.canvas.create_text((self.__VEN_X2 / 2) + (self.__VEN_X1 / 2),
                                self.__VEN_Y2, text="Venus",
                                anchor=t.N, font=myfont)

        #earth
        self.canvas.create_text(((self.__VEN_X2 + self.__DISTANCE) / 2) + ((self.__VEN_X1 + self.__DISTANCE) / 2),
                                self.__VEN_Y2, text="Earth",
                                anchor=t.N, font=myfont)

        #mars
        self.canvas.create_text((self.__MARS_X2 / 2) + (self.__MARS_X1 / 2),
                                self.__MARS_Y2, text="Mars",
                                anchor=t.N, font=myfont)

        #jupiter
        self.canvas.create_text((self.__JUP_X2 / 2) + (self.__JUP_X1 / 2),
                                self.__JUP_Y2, text="Jupiter",
                                anchor=t.N, font=myfont)

        #saturn
        self.canvas.create_text((self.__SAT_X2 / 2) + (self.__SAT_X1 / 2),
                                self.__SAT_Y2, text="Saturn",
                                anchor=t.N, font=myfont)

        #uranus
        self.canvas.create_text((self.__URA_X2 / 2) + (self.__URA_X1 / 2),
                                self.__URA_Y2, text="Uranus",
                                anchor=t.N, font=myfont)

        #neptune
        self.canvas.create_text((self.__NEP_X2 / 2) + (self.__NEP_X1 / 2),
                                self.__NEP_Y2, text="Neptune",
                                anchor=t.N, font=myfont)

        #pluto
        self.canvas.create_text((self.__PLT_X2 / 2) + (self.__PLT_X1 / 2),
                                self.__PLT_Y2, text="Pluto",
                                anchor=t.N, font=myfont)
        

        #packs the canvas
        self.canvas.pack()

        t.mainloop()

if __name__ == "__main__":
    graphic = SolarSystem()
        
