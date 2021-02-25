class Rectangle:
    # When a Rectangle object is created, it should be initialized with
    #`width` and `height` attributes.

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Additionally, if an instance of a Rectangle is represented as a string,
    # it should look like: `Rectangle(width=5, height=10)`
        print(f"Rectangle(width=5{self.width}, height={self.height})")



class Square:
    pass


y = Rectangle(5, 7)
