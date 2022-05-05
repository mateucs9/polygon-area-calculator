class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __repr__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)
  
  def set_width(self, new_width):
    self.width = new_width
  
  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * self.width + 2* self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5
  
  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()
  
  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    
    picture = ''
    for y in range(self.height):
      for x in range(self.width):
        picture += '*'
      picture += '\n'
    
    return picture


class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  
  def __repr__(self):
    return "Square(side={})".format(self.width)

  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side

  def set_width(self, new_width):
    self.width = new_width
    self.height = new_width
  
  def set_height(self, new_height):
    self.height = new_height
    self.width = new_height