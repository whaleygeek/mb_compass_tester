# tkphy.py  02/03/2017  D.J.Whale
#
# A physical transmitter using a Tk canvas

try:
    import Tkinter as tk # python2
except ImportError:
    import tkinter as tk # python3

WIDTH, HEIGHT = 400, 400
OFF = "#000000"
ON  = "#FFFFFF"

class TkPhy():
    @staticmethod
    def create_canvas(width=WIDTH, height=HEIGHT, off=OFF, on=ON, left=None, top=None):
        root = tk.Tk()
        root.attributes('-alpha', 0.0) #For icon
        root.iconify()

        window = tk.Toplevel(root)
        if left is not None and top is not None:
            window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        else:
            window.geometry("%dx%d" % (width, height))
        window.overrideredirect(1)

        canvas = tk.Canvas(window, width=width, height=height, bg='white')
        canvas.pack()
        canvas.my_window = window
        canvas.my_window.my_root = root
        canvas.my_window.update() # cause canvas to draw
        return canvas

    def __init__(self, width=WIDTH, height=HEIGHT, off=OFF, on=ON, left=None, top=None):
        self.state = None
        self.canvas = self.create_canvas(width, height, off, on, left, top)
        self.width = width
        self.height = height

    def start(self):
        self.canvas.my_window.update() # cause canvas to draw

    def off(self):
        # prevent glitching if there are multiple transitions to same state
        if self.state is not None and self.state == 0:
            return # nothing to do

        self.canvas.create_rectangle(0, 0, self.width, self.height, fill=OFF)
        self.canvas.my_window.my_root.update_idletasks()
        self.state = 0

    def on(self):
        # prevent glitching if there are multiple transitions to same state
        if self.state is not None and self.state == 1:
            return # nothing to do
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill=ON)
        self.canvas.my_window.my_root.update_idletasks()
        self.state = 1

    def tx(self, state):
        if state == 0: self.off()
        else:          self.on()

    def toggle(self):
        if self.state == 0: self.off()
        else:               self.on()


#----- TEST HARNESS -----------------------------------------------------------

if __name__ == "__main__":
    import time

    tx = TkPhy(left=0, top=500)

    while True:
        tx.off()
        time.sleep(0.125)
        tx.on()
        time.sleep(0.125)

# END
