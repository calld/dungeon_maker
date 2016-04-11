import mazeConst as maze
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.entrythingy = tk.Entry()
        self.entrythingy.pack(side = 'left')

        self.cont = tk.StringVar()

        self.cont.set('this is a variable')

        self.entrythingy['textvariable'] = self.cont

        self.entrythingy.bind('<Key-Return>', self.print_contents)

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def print_contents(self, event):
        print('value of entry thingy', self.cont.get())

    def newMaze(self):
        self.maze = maze.makeDun()
        self.r = 0
        self.c = 0
        self.floor = 0

root = tk.Tk()
app = Application(master=root)
app.master.title('Dungeon Manager')
app.mainloop()
