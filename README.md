# R3-SoftwareTask2-MohammedShaikh

There are two python files, one of which is the client and the other is the server.

Key presses are detectected from the client and sent to the server with TCP sockets.

I used pynput to detect the key presses from the keyboard.

Once the server recieves, it checks whether or not the client is setting a direction or setting a speed.

If a number is entered, it will check if it is within the range (between 1 - 5) then it will be set into a variable called "sp".

If a letter is entered then it will first check whether or not it is a, s, d or f (directions). Then it will check which direction it is.

After knowing the direction and speed, it will output the speed and directions of the motors.

If a number which is out of the range is entered or if a letter which isn't a valid direction is entered then nothing will be displayed.

To stop the program from running, the letter 'x' can be pressed.

Video link: https://drive.google.com/file/d/1wtfmUCHuFOPVYYeIV_FCPPXoeVqym1Ll/view?usp=sharing

Note: In the video I would sometimes intentionally enter random numbers or random letters to show that if a proper speed or direction is not entered then it would not output anything. Also, the video was sped up a bit to fit the 30 second limit.
