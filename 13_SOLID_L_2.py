class Shape:
    def get_area(self):
        raise NotImplementedError

class Rectangle(Shape):       
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
class Square(Shape):
    def __init__(self,side_length):
        self.side_length=side_length
    def get_area(self):
        return self.side_length * self.side_length


def resize_and_test(sp:Shape):
  area = sp.get_area()
  print(f"Calculated Area: {area}")

# --- Execution ---
print("--- Test 1: Passing a real Rectangle ---")
my_rect = Rectangle(5, 4)
resize_and_test(my_rect)  

print("\n--- Test 2: Passing a Square (LSP) ---")
my_sqr = Square(2)
resize_and_test(my_sqr) 