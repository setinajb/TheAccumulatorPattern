"""

Authors: Jaclyn Setina.
"""

import rosegraphics as rg
window = rg.RoseWindow(350, 400)


np = 4
left_y = 200
start_point = rg.Point(50, left_y)
total_height = 200
first_y = left_y - total_height / 2
y = first_y
for k in range(np):
    end_point = rg.Point(150, y)
    line = rg.Line(start_point, end_point)
    y = y + total_height / (np - 1)
    line.attach_to(window)


start_point = rg.Point(150, 230)

np = 12
left_y = 230
total_height = 200
first_y = left_y - total_height / 2
y = first_y
for k in range(np):
    end_point = rg.Point(250, y)
    line = rg.Line(start_point, end_point)
    y = y + total_height / (np - 1)
    line.attach_to(window)

window.render()
window.close_on_mouse_click()


window2 = rg.RoseWindow(350, 300)

np = 7
left_y = 120
start_point = rg.Point(50, left_y)
total_height = 200
first_y = left_y - total_height / 2
y = first_y
for k in range(np):
    end_point = rg.Point(150, y)
    line = rg.Line(start_point, end_point)
    y = y + total_height / (np - 1)
    line.attach_to(window2)


window2.render()
window2.close_on_mouse_click()