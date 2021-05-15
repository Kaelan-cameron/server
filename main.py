def motorACoast() :
     pins.digital_write_pin(DigitalPin.P0, 0)
     pins.digital_write_pin(DigitalPin.P1, 0)


def setmotorASpeed (speed) :
    if (speed < 0):
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.analog_write_pin(AnalogPin.P0,  (0- speed  * 15))
    elif (speed ==0):
        motorACoast()
    else:
        # speed has to be positive to get here
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.analog_write_pin(AnalogPin.P1, speed * 15)

def on_button_pressed_ab():
    global speed 
    speed = 0
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P0, 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_a():
    global balance
    balance -= 0.1
    if balance <0:
        balance =0


input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_B():
    global balance
    balance += 1
input.on_button_pressed(Button.B, on_button_pressed_B)

speed = 0
balance = 0.5
motorACoast ()





def on_forever():
    basic.show_number(speed)
    setmotorASpeed (speed)
basic.forever(on_forever)


