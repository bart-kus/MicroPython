import machine
import utime

led = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(14, machine.Pin.OUT)
led3 = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.on()
    led2.off()
    led3.off()
    utime.sleep(2)
    led.off()
    led2.on()
    led3.off()
    utime.sleep(2)
    led.off()
    led2.off()
    led3.on()
    utime.sleep(2)
