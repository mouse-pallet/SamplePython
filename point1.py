# Define a class with two instance attributes (x, y) and one class attribute (colour).
class Point2D:
  colour = 'red'
  def __init__(self, x, y):
    self.x = x
    self.y = y
 
# Create two objects that are points, with different initial (x, y) values.
p1 = Point2D(2, 4)
p2 = Point2D(3, 5)
print(p1.x, p1.y, p1.colour)
print(p2.x, p2.y, p2.colour)
# Change the value of the class attribute. The class attribute of all objects
# also change.
Point2D.colour = 'green'
print(p1.x, p1.y, p1.colour)
print(p2.x, p2.y, p2.colour)
