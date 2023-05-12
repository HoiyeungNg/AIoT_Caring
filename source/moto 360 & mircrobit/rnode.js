radio.onReceivedString(function (receivedString) {

    if (receivedString == "handshake") {
        basic.showString("H")
        if (state == 0) {
            state = 1
            randomWait()
            radio.sendString("enrol=" + control.deviceName())
        }
    } else {
        basic.showString("R")
        if (state == 1) {
            buffer = receivedString.split('=')
            commandKey = buffer[0]
            commandValue = buffer[1]

            if (commandKey == "sensor") {
                if (commandValue == "temp") {
                    randomWait()
                    radio.sendString("" + control.deviceName() + "=" + input.temperature())
                    basic.showString("T")
                }
            }
            
        }
    }
})
function randomWait() {
    randomWaitPeriod = Math.randomRange(100, 4900)
    basic.pause(randomWaitPeriod)
}

function showStatus() {
    //light for connection
    basic.clearScreen()
    if (state == 1) {
        led.plot(4, 2)
        led.plot(4, 3)
    }

    //temp for 20-60
    for (let i = 0; i < (temp - 20) / 4; i++) {
        if (i < 5) led.plot(0, i);
        else led.plot(1, i - 5);
    }
    //light for 0-255
    for (let i = 0; i < lightlevel / 26; i++) {
        if (i < 5) led.plot(2, i);
        else led.plot(3, i - 5);
    }
}

input.onButtonPressed(Button.A, function () {
    basic.showString("[" + commandKey + "=" + commandValue + "]")
})


input.onButtonPressed(Button.AB, function () {
    basic.showString("DN:" + control.deviceName())
})

let commandKey = ""
let commandValue = ""
let state = 0
let randomWaitPeriod = 0
let buffer: string[] = []
randomWaitPeriod = 0
let temp = 0
let lightlevel = 0
let localFirebreak = false
let deactive = false
let fireNotion = false
let globalDeactive = false
let globalFirebreak = false
let globalLed = false
radio.setGroup(8)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)

basic.forever(function () {
})
