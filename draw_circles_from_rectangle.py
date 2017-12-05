"""

Authors: Jaclyn Setina.
"""

import rosegraphics as rg

window = rg.RoseWindow(720, 500)

rectangle = rg.Rectangle(rg.Point(400, 250), rg.Point(440, 325))
rectangle.fill_color = 'green'
rectangle.outline_thickness = 5
rectangle.attach_to(window)

x = 360
y = 287.5
radius = 37.5
diameter = radius * 2
for k in range(4):
    center = rg.Point(x, y)
    circle = rg.Circle(center, radius)
    circle.fill_color='green'
    circle.attach_to(window)
    x = x - diameter

x = 420
y = 231.25
radius = 18.75
diameter = radius * 2
for n in range(5):
    center = rg.Point(x, y)
    circle2 = rg.Circle(center, radius)
    circle2.attach_to(window)
    y = y - diameter

# Drawing the blue rectangle
rectangle2 = rg.Rectangle(rg.Point(500, 450), rg.Point(600, 400))
rectangle2.fill_color = 'blue'
rectangle2.outline_thickness = 3
rectangle2.outline_color = 'red'
rectangle2.attach_to(window)


# Drawing the blue circles
x = 475
y = 425
radius = 25
diameter = radius * 2
for k in range(8):
    center = rg.Point(x, y)
    circle3 = rg.Circle(center, radius)
    circle3.fill_color = 'blue'
    circle3.attach_to(window)
    x = x - diameter

# Drawing the red outlined circles
x = 550
y = 350
radius = 50
diameter = radius * 2
for k in range(3):
    center = rg.Point(x, y)
    circle4 = rg.Circle(center, radius)
    circle4.outline_color = 'red'
    circle4.attach_to(window)
    y = y - diameter

window.render()
window.close_on_mouse_click()


# Drawing the yellow rectangle
window2 = rg.RoseWindow(620, 380)

# Drawing the yellow rectangle
rectangle3 = rg.Rectangle(rg.Point(350, 280), rg.Point(375, 330))
rectangle3.fill_color = 'yellow'
rectangle3.outline_thickness = 5
rectangle3.outline_color = 'brown'
rectangle3.attach_to(window2)

# Drawing the yellow circles
x = 325
y = 305
radius = 25
diameter = radius * 2
for k in range(6):
    center = rg.Point(x, y)
    circle = rg.Circle(center, radius)
    circle.fill_color = 'yellow'
    circle.attach_to(window2)
    x = x - diameter

# Drawing the brown outlined circles
x = 362.5
y = 267.5
radius = 12.5
diameter = radius * 2
for k in range(10):
    center = rg.Point(x, y)
    circle = rg.Circle(center, radius)
    circle.outline_color = 'brown'
    circle.attach_to(window2)
    y = y - diameter


window2.render()
window2.close_on_mouse_click()


