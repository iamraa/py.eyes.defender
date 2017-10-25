#!/usr/bin/python3
import os
import time
from tkinter import *
from tkinter import font, ttk

import yaml

from tools.setup import setup

WORK_PERIOD = 20
REST_PERIOD = 2
POSITIONS = ['tl', 'tr', 'br', 'bl']


class FullScreen(object):
    timer = REST_PERIOD * 60
    rect = (None, None)
    rect_position = 'tl'
    width = 0
    height = 0

    def __init__(self, config):
        self.timer = config['rest_period'] * 60

    def quit(self, *args):
        self.root.destroy()

    def show_time(self):
        self.timer -= 1
        self.txt.set(
            time.strftime("%H:%M:%S") + " ({0:02d}:{1:02d})".format(
                self.timer // 60, self.timer % 60))
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
                self.canvas.create_rectangle(
                    x + 49, y + 0, x + 51, y + 100, fill="white"),
                self.canvas.create_rectangle(
                    x + 0, y + 49, x + 100, y + 51, fill="white")
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

        self.canvas = Canvas(self.root,
                             width=self.root.winfo_screenwidth(),
                             height=self.root.winfo_screenheight(),
                             bg="black", highlightbackground="black")
        self.canvas.grid(row=0, column=0, pady=0, ipady=10, sticky=(S, E))
        self.canvas.canvasx(0)
        self.canvas.canvasy(0)

        # draw clock
        fnt = font.Font(family='Helvetica', size=12, weight='normal')
        self.txt = StringVar()
        self.txt.set(
            time.strftime("%H:%M:%S") + " ({0:02d}:{1:02d})".format(
                self.timer // 60, self.timer % 60))
        lbl = ttk.Label(self.root, textvariable=self.txt, font=fnt, foreground="green", background="black")
        lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.root.mainloop()


def config(filename):
    """
    Try to read settings from config file

    :param filename:
    :return:
    """
    conf = dict()
    if os.path.isfile(filename):
        with open(filename, 'rt') as f:
            conf = yaml.load(f)

    defender = conf.get('defender', dict())

    conf = {
        'work_period': defender.get('work_period', WORK_PERIOD),
        'rest_period': defender.get('rest_period', WORK_PERIOD),
    }

    return conf


def main():
    conf = config('config.yaml')

    if len(sys.argv) >= 2:
        if setup(sys.argv):
            exit(0)

    print(
        "Eyes.Defender started. Work: {work_period} min. "
        "Rest: {rest_period} min.".format(**conf))

    while True:
        time.sleep(conf['work_period'] * 60)
        print('Showtime!')
        FullScreen(conf).show_clock()


try:
    main()
except KeyboardInterrupt:
    print("Good Bye!")
except Exception as ex:
    print("Error: {0}\nGood bye!".format(ex))
