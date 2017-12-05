"""

Authors: Jaclyn Setina.
"""

import rosegraphics as rg

window = rg.RoseWindow(600, 350)

start_point_x = 50
start_point_y = 200
end_point_x = 350
end_point_y = 200

for k in range(4):
    start_point = rg.Point(start_point_x, start_point_y)
    end_point = rg.Point(end_point_x, end_point_y)
    line = rg.Line(start_point, end_point)
    # start_point_x = start_point_x - 25
    start_point_y = start_point_y + 40
    # end_point_x = end_point_x - 25
    end_point_y = end_point_y + 40
    line.attach_to(window)

start_point_x = 400
start_point_y = 50
end_point_x = 500
end_point_y = 50

for k in range(7):
    start_point = rg.Point(start_point_x, start_point_y)
    end_point = rg.Point(end_point_x, end_point_y)
    line = rg.Line(start_point, end_point)
    # start_point_x = start_point_x - 25
    start_point_y = start_point_y + 40
    # end_point_x = end_point_x - 25
    end_point_y = end_point_y + 40
    line.attach_to(window)

window.render()
window.close_on_mouse_click()


window2 = rg.RoseWindow(500, 400)

start_point_x = 20
start_point_y = 20
end_point_x = 490
end_point_y = 20

for k in range(12):
    start_point = rg.Point(start_point_x, start_point_y)
    end_point = rg.Point(end_point_x, end_point_y)
    line = rg.Line(start_point, end_point)
    # start_point_x = start_point_x - 25
    start_point_y = start_point_y + 30
    # end_point_x = end_point_x - 25
    end_point_y = end_point_y + 30
    line.attach_to(window2)

window2.render()
window2.close_on_mouse_click()