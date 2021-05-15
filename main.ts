function motorACoast() {
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 0)
}

function setmotorASpeed(speed: number) {
    if (speed < 0) {
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.analogWritePin(AnalogPin.P0, 0 - speed * 15)
    } else if (speed == 0) {
        motorACoast()
    } else {
        //  speed has to be positive to get here
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.analogWritePin(AnalogPin.P1, speed * 15)
    }
    
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    speed = 0
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P0, 1)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    speed += -1
})
input.onButtonPressed(Button.B, function on_button_pressed_B() {
    
    speed += 1
})
let speed = 0
motorACoast()
basic.forever(function on_forever() {
    basic.showNumber(speed)
    setmotorASpeed(speed)
})