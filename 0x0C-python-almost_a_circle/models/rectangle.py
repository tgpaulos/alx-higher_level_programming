#!/usr/bin/python3

"""
This is the 'rectangle' class
"""
class Rectangle(Base):
   
   """the rectangle class"""
   
   def __init__(self, width, height, x=0, y=0, id=None):
      """initialises the rectangle class"""
      self.width = width
      self.height = height
      self.x = x
      self.y = y
      super().__init__(id)
   
   
"""define the getters for width,height ,x , y"""

@property
def width(self):
      """get the width of the Rectangle"""
      return (self.__width)
   
@property
def height(self):
     """get the height of the Rectangle"""
     return (self.__height)
   
   
@property
def x (self):
     """x getter"""
     return (self.__height)
   
@property
def y (self):
     """y getter"""
     return (self.__height)


"""define the setters for width,height, x, y"""


@width.setter

def width(self):
     
     def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

@height.setter
   
def height(self, height):
        if type(height) != int:
            raise TypeError("heigth must be an integer")
        if height <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = height
   
@x.setter
   
def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

@y.setter

def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

def update(self, *args, **kwargs):
        
        """Update the Rectangle"""
        
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
