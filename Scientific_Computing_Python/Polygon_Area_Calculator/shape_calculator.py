class Rectangle:
    # When a Rectangle object is created, it should be initialized with
    #`width` and `height` attributes.

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle: Width: {self.width}\nHeight: {self.height}'

    # Method that reassigns width
    def self(width, width_num):
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
        pass

    def get_amount_inside(self):
        pass

    # Additionally, if an instance of a Rectangle is represented as a string,
    # it should look like: `Rectangle(width=5, height=10)`
    # print(f"Rectangle(width=5{self.width}, height={self.height})")


class Square:
    pass


y = Rectangle(5, 7)
print(y)
print('get_diagonal:', y.get_diagonal())
