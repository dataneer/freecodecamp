class Rectangle:
    # When a Rectangle object is created, it should be initialized with
    #`width` and `height` attributes.

    def __init__(self, width, height):
        if type(width) == int and type(height) == int:
            self.width = width
            self.height = height
        else:
            raise TypeError("Width and height have to be integers.")

    # Additionally, if an instance of a Rectangle is represented as a string,
    # it should look like: `Rectangle(width=5, height=10)`
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    # Method that reassigns width
    def set_width(self, width_num):
        self.width = width_num

    # Method that reassigns height
    def set_height(self, height_num):
        self.height = height_num

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        # check if self.width or self.height is greater than 50
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            pic_width = self.width * '*'
            # Append pic_width as a list item n times based on the value
            # of self.height
            picture_lst = [pic_width] * self.height
            # Combine picture_lst into a string with new lines using .join()
            picture_shape = '\n'.join(picture_lst)
            return picture_shape

    # * `get_amount_inside`: Takes another shape (square or rectangle) as an
    # argument. Returns the number of times the passed in shape could fit inside
    # the shape (with no rotations). For instance, a rectangle with a width of
    # 4 and a height of 8 could fit in two squares with sides of 4.
    def get_amount_inside(self, shape):
        # first d
        if self.width > shape.width and self.height > shape.height:
            # Use flat division to compare whole numbers
            compare_w = self.width // shape.width
            compare_h = self.height // shape.height
            inside_shape = compare_w * compare_h
            return inside_shape
        else:
            return "Shape too large."

    # Additionally, if an instance of a Rectangle is represented as a string,
    # it should look like: `Rectangle(width=5, height=10)`
    # print(f"Rectangle(width=5{self.width}, height={self.height})")


class Square(Rectangle):

    def __init__(self, side):
        if type(side) == int:
            self.width = side
            self.height = side
        else:
            raise TypeError("Side has to be a integer.")

    # If an instance of a Square is represented as a string, it should
    # look like: `Square(side=9)
    def __repr__(self):
        return f'Square(side={self.width})'

    # The Square class should be able to access the Rectangle class methods but
    # should also contain a `set_side` method.`
    def set_side(self, side_num):
        self.width = side_num
        self.height = side_num





rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
