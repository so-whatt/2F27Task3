input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 6; index++) {
        basic.showNumber(count)
        basic.pause(1000)
        count += -1
    }
    basic.showNumber(0)
    basic.clearScreen()
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 4500, 0, 255, 0, 3500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        `)
    basic.showLeds(`
        . # . # .
        # . . . #
        . . . . .
        # . . . #
        . # . # .
        `)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1000)
})
let count = 0
count = 6
