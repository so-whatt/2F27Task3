input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 6; index++) {
        basic.showNumber(count)
        basic.pause(1000)
        count += 1
    }
})
let count = 0
count = 1
basic.forever(function () {
	
})
