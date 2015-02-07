class Point2D:
  colour = 'red'
  def __init__(self, x, y):
    self.x = x
    self.y = y
 
  def AddValue(self, value):
    self.x += value
    self.y += value
 
  def AddPoint(self, point):
    self.x += point.x
    self.y += point.y
 
  def IsEqual(self, point):
    if self.x == point.x and self.y == point.y:
		return True
    return False
 
p1 = Point2D(2, 4)
print(p1.x, p1.y)
p1.AddValue(- 5)
print(p1.x, p1.y)
p2 = Point2D(3, 5)
p1.AddPoint(p2)
print(p1.x, p1.y)
print(p1.IsEqual(p2))
p3 = Point2D(0, 4)
print(p1.IsEqual(p3))
