"""

Authors: Jaclyn Setina.
"""

import rosegraphics as rg

window = rg.RoseWindow(650, 350)

# Drawing the Green Circle
x = 100
y = 100
radius = 20

center = rg.Point(x, y)
circle = rg.Circle(center, radius)
circle.fill_color='green'
circle.attach_to(window)

# Draw the squares
x = 100
y = 100
length_side = 40
for k in range(7):
    center = rg.Point(x, y)
    square = rg.Square(center, length_side)
    square.attach_to(window)
    x = x + 20
    y = y + 20

# Draw the hollow circle
x = 350
y = 70
radius = 50

center = rg.Point(x, y)
circle2 = rg.Circle(center, radius)
circle2.attach_to(window)

# Draw the squares
x = 350
y = 70
length_side = 100
for k in range(4):
    center = rg.Point(x, y)
    square = rg.Square(center, length_side)
    square.attach_to(window)
    x = x + 50
    y = y + 50


window.render()
window.close_on_mouse_click()


window2 = rg.RoseWindow(525, 300)

# Draw the blue circle
x = 50
y = 50
radius = 10

center = rg.Point(x, y)
circle = rg.Circle(center, radius)
circle.fill_color='blue'
circle.attach_to(window2)



# Draw the squares
x = 50
y = 50
length_side = 20
for k in range(20):
    center = rg.Point(x, y)
    square2 = rg.Square(center, length_side)
    square2.attach_to(window2)
    x = x + 10
    y = y + 10

window2.render()
window2.close_on_mouse_click()
