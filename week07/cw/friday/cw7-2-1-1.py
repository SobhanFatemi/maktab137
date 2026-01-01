class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.__z = z
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, position):
        self._x = position

    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, position):
        self._y = position

    
    @property
    def z(self):
        return self.__z
    
    
    @z.setter
    def z(self, position):
        self.__z = position

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            raise ValueError("Value must be a Vector3D!")
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        if not isinstance(other, Vector3D):
            raise ValueError("Value must be a Vector3D!")
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __iadd__(self, other):
        if not isinstance(other, Vector3D):
            raise ValueError("Value must be a Vector3D!")
        
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
        return self
    
    def __radd__(self, value):
        if not isinstance(value, int):
            raise TypeError("The value must be an int")
        
        return Vector3D(self.x + value, self.y + value, self.z + value)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __len__():
        return 3
    
    def __str__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}"
    
    def __repr__(self):
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"
    

v1 = Vector3D(0, 0, 0)
v2 = Vector3D(1, 1, 1)

v3 = v1 + v2
v3 += v2

print(10 + v3)
print(v3)

v1 = 2 + v1
print(v3 == v1)