import socket

s = socket.socket()
print ('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connections')

c , addr = s.accept()

while True:
    
    x = str(c.recv(1024).decode())
    
    if x == 'a' or x == 's' or x == 'd' or x == 'w':
        direction = x
    elif x == '1' or x == '2' or x == '3' or x == '4' or x == '5':
        speed = float(x)
        sp = round(speed * (255/5))
    elif x == 'x':
        break

    if x == 'w':
        for i in range(4): 
            print ("[f"+ str(sp) + "]", end='')
        print("\n")
    elif x == 's':
        for i in range(4): 
             print ("[r"+ str(sp) + "]", end='')
        print("\n")
    elif x == 'a':
        for i in range(2): 
            print ("[r"+ str(sp) + "]", end='')
        for j in range(2): 
            print ("[f"+ str(sp) + "]", end='')
        print("\n")
    elif x == 'd':
        for i in range(2): 
            print ("[f"+ str(sp) + "]", end='')
        for j in range(2): 
            print ("[r"+ str(sp) + "]", end='')
        print("\n")

c.send(bytes('Thanks', 'utf-8'))

c.close()