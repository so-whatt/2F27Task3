def on_button_pressed_a():
    global count
    for index in range(6):
        basic.show_number(count)
        basic.pause(1000)
        count += -1
    basic.show_number(0)
    basic.clear_screen()
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            4500,
            0,
            255,
            0,
            3500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
    """)
    basic.show_leds("""
        . # . # .
                # . . . #
                . . . . .
                # . . . #
                . # . # .
    """)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

count = 0
count = 6