from time import sleep
import machine
import ssd1306

# Pin 5 is  D1
# Pin 4 is  D2

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

heart_icon = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [ 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [ 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0],
]

def clear_screen():
    oled.fill(0)
    oled.show()

def marry_me():
    oled.fill(0)
    oled.show()
    sleep(0.5)
    
    oled.text("Will",0,0)
    oled.show()
    sleep(0.5)

    oled.text("You",40,0)
    oled.show()
    sleep(0.5)

    # display_heart(70,0)
    # sleep(0.5)

    oled.text("Marry",0,10)
    oled.show()
    sleep(0.5)
    
    oled.text("Me",0,20)
    oled.show()
    sleep(0.5)

    for i in range(20,90,10):
        display_heart(i,20)
        sleep(0.5)

    
def display_heart(X,Y):
    for y, row in enumerate(heart_icon):
        for x, c in enumerate(row):
            oled.pixel(x+X, y+Y, c)
    oled.show()

while True:
    marry_me()
    sleep(1)