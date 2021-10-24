import socket
from pynput.keyboard import *

keyboard = Controller()

c = socket.socket()

c.connect(('localhost', 9999))

def press_on(key):
    x = str.encode(key.char)
    print(x.decode())
    c.send(x)

def press_off(key):
    if key.char == ('x'):
        return False

with Listener(on_press = press_on, on_release=press_off) as listener:
    listener.join()
    

print(c.recv(1024).decode())