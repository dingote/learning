from adafruit_circuitplayground.express import cpx
import time

# Si el switch esta encendido despliega Interruptor ENCENDIDO!!!
# Si el switch esta apagado despliega Interruptor APAGADO!!!

while True:
    if cpx.switch:
        print("Interruptor APAGADO!!!")
    else:
        print("Interruptor ENCENDIDO!!!")
    time.sleep(0.02)
