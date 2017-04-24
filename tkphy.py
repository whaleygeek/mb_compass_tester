# tkphy.py  02/03/2017  D.J.Whale
#
# A physical transmitter using a Tk canvas

import math

try:
    import Tkinter as tk # python2
except ImportError:
    import tkinter as tk # python3

WIDTH, HEIGHT = 400, 400
OFF = "#000000"
ON  = "#FFFFFF"

class TkPhy():
    @staticmethod
    def create_canvas(width=WIDTH, height=HEIGHT, left=None, top=None):
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

    def __init__(self, width=WIDTH, height=HEIGHT, left=None, top=None):
        self.canvas = self.create_canvas(width, height, left, top)
        self.width  = width
        self.height = height
        self.mid_x  = width/2
        self.mid_y  = height/2
        self.size   = self.width/3

    def start(self):
        self.canvas.my_window.update() # cause canvas to draw
        self.draw_backdrop()

    def update(self):
        self.canvas.my_window.my_root.update_idletasks()

    #def stop


    def draw_backdrop(self):
        print("draw backdrop")
        top    = self.mid_y - self.size
        left   = self.mid_x - self.size
        right  = self.mid_x + self.size
        bottom = self.mid_y + self.size
        midx   = self.mid_x
        midy   = self.mid_y

        # circle
        self.canvas.create_oval(top, left, bottom, right)
        # horizontal line
        #self.canvas.create_line(left, midx, right, midy)
        # vertical line
        #self.canvas.create_line(midx, top, midx, bottom)

        self.update()

    @staticmethod
    def circle_point(cx, cy, radius, angle):
        rads = math.radians(angle-90)
        x = cx + math.sin(rads) * radius
        y = cy + math.cos(rads) * radius
        x = int(round(x, 0))
        y = int(round(y, 0))
        return (x,y)

    def update_heading(self, heading):
        print("update heading:%d" % heading)
        midx   = self.mid_x
        midy   = self.mid_y
        x,y    = self.circle_point(midx, midy, self.size, heading)
        self.canvas.create_line(midx, midy, y, x)
        self.update()

    #def off(self):
    #    # prevent glitching if there are multiple transitions to same state
    #    if self.state is not None and self.state == 0:
    #        return # nothing to do
    #
    #    self.canvas.create_rectangle(0, 0, self.width, self.height, fill=OFF)
    #    self.canvas.my_window.my_root.update_idletasks()
    #    self.state = 0

    #def on(self):
    #    # prevent glitching if there are multiple transitions to same state
    #    if self.state is not None and self.state == 1:
    #        return # nothing to do
    #    self.canvas.create_rectangle(0, 0, self.width, self.height, fill=ON)
    #    self.canvas.my_window.my_root.update_idletasks()
    #    self.state = 1

    #def tx(self, state):
    #    if state == 0: self.off()
    #    else:          self.on()

    #def toggle(self):
    #    if self.state == 0: self.off()
    #    else:               self.on()


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
