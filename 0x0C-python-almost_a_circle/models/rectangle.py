#!/usr/bin/python3
"""This module creates the Rectangle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """
    A class named Rectangle
    Attributes:
             attr1(id): id of object
             attr2(width): rectangle width
             attr3(height): rectangle height
             attr4(x): number of spaces before rectangle
             attr5(y): number of newlines before rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """dispaly the rectangle"""
        for row in range(self.__y):
            print()
        for row in range(self.__height):
            for column in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the informal representation of the object"""
        return"[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update attributes"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'width':
                        self.__width = kwargs['width']
                    if i == 'height':
                        self.__height = kwargs['height']
                    if i == 'x':
                        self.__x = kwargs['x']
                    if i == 'y':
                        self.__y = kwargs['y']

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    @property
    def width(self):
        """Returns width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of class instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of class instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x of instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x of class instance"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y of instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y of class instance"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def to_dictionary(self):
        """
        retrieves a dictionary representation
        of a rectangle
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y}
