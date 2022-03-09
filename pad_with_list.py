import time
import board
import touchio

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)

lista = ['uno','dos','tres','cuatro','cinco','seis']
pressed = 'El pad presionado fue: '
    
while True:
    if touch_A1.value:
        print(pressed + lista[0])
    if touch_A2.value:
        print(pressed + lista[1])
    if touch_A3.value:
        print(pressed + lista[2])
    if touch_A4.value:
        print(pressed + lista[3])
    if touch_A5.value:
        print(pressed + lista[4])
    if touch_A6.value:
        print(pressed + lista[5])
    time.sleep(0.3)
