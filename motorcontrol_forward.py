import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(31, gpio.OUT)  #IN1
    gpio.setup(33, gpio.OUT)  #IN2
    gpio.setup(35, gpio.OUT)  #IN3
    gpio.setup(37, gpio.OUT)  #IN4

def gameover():
    # Set all pins low
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    gpio.output(37, False)
    
def forward(tf):
    init()
    #Left wheels
    gpio.output(31, True)
    gpio.output(33, False)
    #Right wheels
    gpio.output(35, False)
    gpio.output(37, True)
    #Wait
    time.sleep(tf)
    #Send all pins low & cleanup
    gameover()
    gpio.cleanup()
    
init()
gameover()
gpio.cleanup()
    