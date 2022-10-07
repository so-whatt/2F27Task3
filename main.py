def on_button_pressed_a():
    global count
    for index in range(6):
        basic.show_number(count)
        basic.pause(1000)
        count += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

count = 0
count = 1

def on_forever():
    pass
basic.forever(on_forever)
