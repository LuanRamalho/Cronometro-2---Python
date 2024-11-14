from tkinter import *
import time


class StopWatch(Frame):
    """ Implements a stop watch frame widget. """

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr, font=('Helvetica', 36), bg="#282C34", fg="#61DAFB")
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=10, padx=10)

    def _update(self):
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 1000)
        self.timestr.set('%02d:%02d:%03d' % (minutes, seconds, hseconds))

    def Start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        """ Reset the stopwatch. """
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


def main():
    root = Tk()
    root.title("Stopwatch")
    root.configure(bg="#282C34")
    
    sw = StopWatch(root)
    sw.pack(side=TOP, pady=20)

    button_style = {'font': ('Helvetica', 14), 'bg': "#61DAFB", 'fg': "#282C34", 'width': 8, 'relief': 'solid'}

    Button(root, text='Start', command=sw.Start, **button_style).pack(side=LEFT, padx=5, pady=10)
    Button(root, text='Stop', command=sw.Stop, **button_style).pack(side=LEFT, padx=5, pady=10)
    Button(root, text='Reset', command=sw.Reset, **button_style).pack(side=LEFT, padx=5, pady=10)
    Button(root, text='Quit', command=root.quit, **button_style).pack(side=LEFT, padx=5, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
