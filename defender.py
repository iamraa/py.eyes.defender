from tkinter import *
from tkinter import ttk
from tkinter import font
import time


POSITIONS = ['tl', 'tr', 'br', 'bl']


class FullScreen(object):
    timer = 15
    rect = (None, None)
    rect_position = 'tl'
    width = 0
    height = 0

    def quit(self, *args):
        self.root.destroy()

    def show_time(self):
        self.timer -= 1
        self.txt.set(time.strftime("%H:%M:%S") + " ({0}:{1})".format(self.timer // 60, self.timer % 60))
        self.root.after(1000, self.show_time)

        if self.rect[0] is None:
            if self.rect_position == 'tl':
                x, y = 0, 0
                self.rect_position = 'tr'

            elif self.rect_position == 'tr':
                x, y = self.width - 100, 0
                self.rect_position = 'br'

            elif self.rect_position == 'br':
                x, y = self.width - 100, self.height - 100
                self.rect_position = 'bl'

            elif self.rect_position == 'bl':
                x, y = 0, self.height - 100
                self.rect_position = 'tl'

            self.rect = (
                self.canvas.create_rectangle(x + 49, y + 0, x + 51, y + 100, fill="white"),
                self.canvas.create_rectangle(x + 0, y + 49, x + 100, y + 51, fill="white")
            )
        else:
            for r in self.rect:
                if r is not None:
                    self.canvas.delete(r)
            self.rect = (None, None)

        if self.timer < 0:
            self.quit()

    def show_clock(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')
        self.root.bind("<Escape>", self.quit)
        self.root.bind("x", self.quit)
        self.root.after(1000, self.show_time)

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(),
            bg="black", highlightbackground="black")
        self.canvas.grid(row=0, column=0, pady=0, ipady=10, sticky=(S,E))
        self.canvas.canvasx(0)
        self.canvas.canvasy(0)

        # draw clock
        fnt = font.Font(family='Helvetica', size=12, weight='normal')
        self.txt = StringVar()
        self.txt.set(time.strftime("%H:%M:%S") + " ({0}:{1})".format(self.timer // 60, self.timer % 60))
        lbl = ttk.Label(self.root, textvariable=self.txt, font=fnt, foreground="green", background="black")
        lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.root.mainloop()


def main():
    i = 0
    #FullScreen().show_clock()
    #return

    while True:
        time.sleep(1)
        i += 1

        if i > 10:
            print('Showtime!')
            i = 0
            FullScreen().show_clock()

main()