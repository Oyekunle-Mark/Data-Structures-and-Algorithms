"""
The classic English Ruler problem. The function draw_ruler takes the
numbers of inches to be drawn and the tick_length of the ruler
"""

def draw_line(tick_length, label=''):
    line = '-' * tick_length

    if label:
        line += " " + str(label)

    print(line)


def draw_interval(tick_length):
    if tick_length > 0:
        draw_interval(tick_length - 1)
        draw_line(tick_length)
        draw_interval(tick_length - 1)


def draw_ruler(inches, tick_length):
    draw_line(tick_length, "0")

    for num in range(1, inches + 1):
        draw_interval(tick_length - 1)
        draw_line(tick_length, num)


draw_ruler(2, 3)
