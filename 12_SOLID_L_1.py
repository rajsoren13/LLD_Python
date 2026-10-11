#violate LSP
class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height


class Square(Rectangle):

  def __init__(self, side_length):
    super().__init__(side_length, side_length)

  def set_width(self, width):
    self.width = width
    self.height = width  # Forces height to match width

  def set_height(self, height):
    self.width = height
    self.height = height  # Forces width to match height

  def get_area(self):
    return self.width * self.height


# --- Just a regular function (No class or @staticmethod needed!) ---
def resize_and_test(rect: Rectangle):
  rect.set_width(5)  # Set width to 5
  rect.set_height(4)  # Set height to 4

  area = rect.get_area()
  print(f"Calculated Area: {area}")


# --- Execution ---
print("--- Test 1: Passing a real Rectangle ---")
my_rect = Rectangle(2, 2)
resize_and_test(my_rect)  # Outputs: Calculated Area: 20

print("\n--- Test 2: Passing a Square (LSP Violation) ---")
my_sqr = Square(2)
resize_and_test(my_sqr)  # Outputs: Calculated Area: 16