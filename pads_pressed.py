import time
import board
import touchio

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)

while True:
    
    i = 1
    r1, r2, r3, r4, r5, r6, r7 = 0,0,0,0,0,0,0
    pressed = 'Los pads presionados fueron: '
    
    while i <= 3:
        if touch_A1.value and r1 == 0:
            i = i+1
            r1 = r1 + 1
            pressed = pressed + 'A1 '
        if touch_A2.value and r2 == 0:
            i = i+1
            r2 = r2 + 1
            pressed = pressed + 'A2 '
        if touch_A3.value and r3 == 0:
            i = i+1
            r3 = r3 + 1
            pressed = pressed + 'A3 '
        if touch_A4.value and r4 == 0:
            i = i+1
            r4 = r4 + 1
            pressed = pressed + 'A4 '
        if touch_A5.value and r5 == 0:
            i = i+1
            r5 = r5 + 1
            pressed = pressed + 'A5 '
        if touch_A6.value and r6 == 0:
            i = i+1
            r6 = r6 + 1
            pressed = pressed + 'A6 '
    print(pressed)
    time.sleep(3)
    print('Presione de nuevo los pads.')
