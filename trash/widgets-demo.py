# A more complex example showing the use of classes in GUI programming

from tkinter import *

class GUIExample:

    def __init__(self, master):
        self.master = master # for showInfo()

        # Create frame to hold widgets
        frame = Frame(master)

        # Create label for header
        self.headLbl = Label(frame, text="Widget Demo Program", relief=RIDGE)
        self.headLbl.pack(side=TOP, fill=X)

        # Dummy frame for border
        spacerFrame = Frame(frame, borderwidth=10)

        # Create frame to hold center part of the form
        centerFrame = Frame(spacerFrame)
        leftColumn = Frame(centerFrame, relief=GROOVE, borderwidth=10)
        rightColumn = Frame(centerFrame, relief=GROOVE, borderwidth=10)

        # Some colorful widgets
        self.colorLabel = Label(rightColumn, text="Select a color")
        self.colorLabel.pack(expand=YES, fill=X)

        entryText = StringVar(master)
        entryText.set("Select a color")
        self.colorEntry = Entry(rightColumn, textvariable=entryText)
        self.colorEntry.pack(expand=YES, fill=X)

        # Create some radio buttons
        self.radioBtns = []
        self.radioVal = StringVar(master)
        btnList = ("black", "red", "green", "blue", "white", "yellow")

        for color in btnList:
            self.radioBtns.append(Radiobutton(leftColumn, text=color, value=color, \
            indicatoron=TRUE, variable=self.radioVal, command=self.updateColor))
        else:
            if (len(btnList) > 0):
                self.radioVal.set(btnList[0])
                self.updateColor()

        for btn in self.radioBtns:
            btn.pack(anchor=W)

        # Make the frames visible
        leftColumn.pack(side=LEFT, expand=YES, fill=Y)
        rightColumn.pack(side=LEFT, expand=YES, fill=BOTH)
        centerFrame.pack(side=TOP, expand=YES, fill=BOTH)

        # Create an indicator checkbutton
        self.indicVal = BooleanVar(master)
        self.indicVal.set(TRUE)
        self.updateIndic()
        Checkbutton(spacerFrame, text="Show indicator", command=self.updateIndic, \
                variable=self.indicVal).pack(side=TOP, fill=X)

        # Create the Info button
        Button(spacerFrame, text="Info", command=self.showInfo).pack(side=TOP, fill=X)

        # Create the Quit button
        Button(spacerFrame, text="Quit", command=self.quit).pack(side=TOP, fill=X)

        frame.pack()
        spacerFrame.pack()

    def quit(self):
        self.master.destroy()

    def updateColor(self):
        self.colorLabel.configure(fg=self.radioVal.get())
        self.colorEntry.configure(fg=self.radioVal.get())

    def updateIndic(self):
        for btn in self.radioBtns:
            btn.configure(indicatoron=self.indicVal.get())

    def updateColorPrev(self):
        if (self.colorprevVal.get()):
            for btn in self.radioBtns:
                color = btn.cget("text")
                btn.configure(fg=color)
        else:
            for btn in self.radioBtns:
                btn.configure(fg="black")

    def showInfo(self):
        toplevel = Toplevel(self.master, bg="white")
        toplevel.transient = self.master
        toplevel.title("Program info")
        Label(toplevel, text="A simple Tkinter demo", fg="navy", bg="white").pack(pady=20)
        Label(toplevel, text="Written by Bruno Dufour", bg = "white").pack()
        Label(toplevel, text="http://www.cs.mcgill.ca/ ̃bdufou1/", bg="white").pack()
        Button(toplevel, text="Close", command=toplevel.withdraw).pack(pady=30)

root = Tk()
ex = GUIExample(root)
root.title("A simple widget demo")
root.mainloop()