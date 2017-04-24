import microbit
import tkphy

vis = None

def start():
    global vis
    vis = tkphy.TkPhy()
    vis.start()

def update(heading):
    vis.update_heading(heading)

# MAIN

start()
while True:
    msg = microbit.get_next_message()
    if msg is not None:
        try:
            heading = int(msg)
            update(heading)
        except ValueError:
            pass

# END
