from machine import Pin
from time import sleep_ms

led = Pin(16, Pin.OUT)
button = Pin(0, Pin.IN)

def func(v):
    led.value(not led.value())

button.irq(trigger=Pin.IRQ_FALLING, handler=func)

while True:
    sleep_ms(500)
    pass