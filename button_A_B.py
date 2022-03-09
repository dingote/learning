import digitalio
import board
import time

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.switch_to_input(pull=digitalio.Pull.DOWN)

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if buttonA.value:  # button is pushede
        print('Boton A presionado')
    elif buttonB.value:
        print('Boton B presionado')
    else:
        print('Ningun boton presionado')

    time.sleep(0.02)
