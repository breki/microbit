from microbit import button_a, button_b, display, Image

while True:
    if button_a.is_pressed():
        display.show(Image.YES)
    elif button_b.is_pressed():
        display.show(Image.NO)
    else:
        display.show(Image.ASLEEP)
