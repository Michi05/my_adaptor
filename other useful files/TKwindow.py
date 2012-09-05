
#GUI libraries for testing
import Tkinter
from Tkinter import *



class TKWindow(Frame):
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.command1 = Button(self)
        self.command1["text"] = "show_accel",
        self.command1["command"] = lambda: method2("show_accel")
        self.command1.pack
        self.command1.pack({"side": "bottom"})
        self.command1.pack({"side": "left"})

        self.command2 = Button(self)
        self.command2["text"] = "show_status",
        self.command2["command"] = method1
        self.command2.pack({"side": "bottom"})
        self.command2.pack({"side": "left"})
        
        
        self.can = Canvas(self.master, width=500, height=250)
        self.can.grid(row=2, column=1)
        self.can.create_line(0,0,500,200)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.grid()
        self.createWidgets()




#    root = Tk()
#    app = Application(master=root)
#    app.mainloop()
#    root.destroy()

