let transmitting = false
basic.forever(() => {
    if (transmitting) {
        led.plot(2, 2)
        radio.sendNumber(input.compassHeading())
        basic.pause(100)
        led.unplot(2, 2)
    } else {
        basic.pause(100)
    }
})
input.onButtonPressed(Button.A, () => {
    transmitting = true
})
radio.onDataPacketReceived(({receivedNumber}) => {
    led.plot(2, 2)
    serial.writeNumber(receivedNumber)
    serial.writeLine("")
    led.unplot(2, 2)
})
input.onButtonPressed(Button.B, () => {
    transmitting = false
})
radio.setGroup(1)
