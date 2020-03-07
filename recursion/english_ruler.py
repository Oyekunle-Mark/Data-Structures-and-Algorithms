"""
The classic English Ruler problem. The function draw_ruler takes the
numbers of inches to be drawn and the tick_length of the ruler
"""

from typing import Optional


def draw_line(tick_length: int, label: Optional[str] = '') -> None:
    line = '-' * tick_length

    if label:
        line += " " + str(label)

    print(line)


def draw_interval(tick_length: int) -> None:
    if tick_length > 0:
        draw_interval(tick_length - 1)
        draw_line(tick_length)
        draw_interval(tick_length - 1)


def draw_ruler(inches: int, tick_length: int) -> None:
    draw_line(tick_length, "0")

    for num in range(1, inches + 1):
        draw_interval(tick_length - 1)
        draw_line(tick_length, num)


draw_ruler(2, 3)
