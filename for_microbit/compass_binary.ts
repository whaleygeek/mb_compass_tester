basic.forever(() => {
    led.plot(2, 2)
    serial.writeString(String.fromCharCode(input.compassHeading()))
    led.unplot(2, 2)
    basic.pause(100)
})
