class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        horizontal_fits = self.width // shape.width
        vertical_fits = self.height // shape.height
        return horizontal_fits * vertical_fits

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def set_side(self, side: int):
        self.width = side
        self.height = side

    def set_width(self, width: int):
        self.set_side(width)

    def set_height(self, height: int):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


if __name__ == "__main__":
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