class Rectangle():

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** (1/2)

  def get_picture(self):

    output = ""

    if self.width > 50 or self.height > 50:
      
      output += "Too big for picture."
      return output

    for i in range(0, self.height):

      for j in range(0, self.width):

        output += "*"

      output += "\n"

    return output

  def get_amount_inside(self, instance):

    times_fit = int()

    inst_width = instance.width
    inst_height = instance.height

    times_fit = self.width // inst_width
    times_fit *= self.height // inst_height

    return times_fit

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    super().__init__(self.side, self.side)

  def set_side(self, side):
    self.__init__(side)

  def __str__(self):
    return f"Square(side={self.side})"

  def set_width(self, side):
    self.set_side(side)
    super().set_width(side)
    super().set_height(side)

  def set_height(self, side):
    self.set_side(side)
    super().set_width(side)
    super().set_height(side)


# Testing
rect = Rectangle(width=4, height=8)
rect2 = Rectangle(width=4, height=4)

print(rect.get_amount_inside(rect2))

sq = Square(side=5)
sq.set_side(side=9)
# sq.set_width(5)
print(sq.side, sq.width, sq.height, sq.get_area())
print(rect)
print(sq)
# print(rect.get_area())
# print(rect.get_diagonal())
# print(rect.get_perimeter())
# print(rect.get_picture())
