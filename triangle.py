class Triangle:
    __match_args__ = ("x", "y", "z")  

    def __init__(self, x:int | float, y:int | float, z:int | float):
         self.x = x
         self.y = y
         self.z = z
    
    def is_valid(self) -> bool:
        match self:
            case Triangle(x, y, z) if x + y > z and y + z > x and x + z > y:
                return True 
            case Triangle(x, y, z):
                return False 
            case _:
                raise TypeError("Not a valid triangle obj")

if __name__ == "__main__":
    pass