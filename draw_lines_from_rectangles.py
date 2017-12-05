"""

Authors: Jaclyn Setina.
"""

import rosegraphics as rg

window = rg.RoseWindow(900, 400)

# making the red outlined rectangle

rectangle = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
rectangle.outline_color = 'red'
rectangle.attach_to(window)

# making the blue outlines rectangle

rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
rectangle2.outline_color = 'blue'
rectangle2.attach_to(window)

start_point_x = 125
start_point_y = 75
end_point_x = 350
end_point_y = (150 + 175)/2

# start_point = rg.Point(start_x, start_y)
# end_point = rg.Point(end_x, end_y)
for k in range(5):
    start_point = rg.Point(start_point_x, start_point_y)
    end_point = rg.Point(end_point_x, end_point_y)
    line = rg.Line(start_point, end_point)
    start_point_x = start_point_x - 25
    start_point_y = start_point_y + 50
    end_point_x = end_point_x - 25
    end_point_y = end_point_y + 50

    line.thickness = 5
    if k % 2 == 0:
        line.color = 'red'
    else:
        line.color = 'blue'

    line.attach_to(window)



# Draw the black rectangle
rectangle3 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
rectangle3.attach_to(window)

# Draw the green rectangle
rectangle4 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
rectangle4.outline_color = 'green'
rectangle4.attach_to(window)



start_point_x = (870 + 750)/2
start_point_y = (100 + 30)/2
end_point_x = (700 + 650)/2
end_point_y = (60 + 90)/2

for k in range(8):
    start_point = rg.Point(start_point_x, start_point_y)
    end_point = rg.Point(end_point_x, end_point_y)
    line = rg.Line(start_point, end_point)
    start_point_x = start_point_x - 60
    start_point_y = start_point_y + 35
    end_point_x = end_point_x - 60
    end_point_y = end_point_y + 35

    line.thickness = 5
    if k % 2 == 0:
        line.color = 'black'
    else:
        line.color = 'green'

    line.attach_to(window)

window.render()
window.close_on_mouse_click()


window2 = rg.RoseWindow(700, 700)

# Draw the brown outlined rectangle
rectangle5 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 250))
rectangle5.outline_color = 'brown'
rectangle5.attach_to(window2)

# Draw the cyan blue
rectangle6 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 50))
rectangle6.outline_thickness = 5
rectangle6.outline_color = 'cyan'
rectangle6.attach_to(window2)

start_point_x = (300 + 400)/2
start_point_y = (150 + 250)/2
end_point_x = (100 + 150)/2
end_point_y = (25 + 50)/2

for k in range(11):
    start_point = rg.Point(start_point_x, start_point_y)
    end_point = rg.Point(end_point_x, end_point_y)
    line = rg.Line(start_point, end_point)
    start_point_x = start_point_x - 50
    start_point_y = start_point_y + 50
    end_point_x = end_point_x - 50
    end_point_y = end_point_y + 50

    line.thickness = 5
    if k % 2 == 0:
        line.color = 'brown'
    else:
        line.color = 'cyan'

    line.attach_to(window2)


window2.render()
window2.close_on_mouse_click()