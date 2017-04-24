import microbit
import time

def process_incoming(msg):
    print(msg)

while True:
    msg = microbit.get_next_message()
    if msg is not None:
        process_incoming(msg)


