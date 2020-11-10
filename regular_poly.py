# regular_poly.py

import math

"""Regular Polygon class"""
class RegularPoly:
    """Class to create a regular polygon"""
    def __init__(self, vert_count, radius):
        """Initialize the RegulaPoly class attributes"""

        self.vert_count = vert_count # Number of vertices of polygon
        self.radius     = radius # Circumradius

    @property
    def vert_count(self):
        """Get count of vertices"""
        return self._vert_count

    @vert_count.setter
    def vert_count(self, vert_count):
        """Set the number of vertices of polygon"""
        if not isinstance(vert_count, int):
            raise TypeError(f'Number of vertices should be of type integer')
        if vert_count < 3:
            raise ValueError(f'Number of vertices should be greater than or equal to 3')

        self._vert_count = vert_count

        self._edge_length = None
        self._interior_angle = None
        self._apothem = None
        self._area = None
        self._perimeter = None



    @property
    def radius(self):
        """Get circumradius"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the circumradius of polygon"""
        if not isinstance(radius, int):
            raise TypeError(f'Radius should be of type integer')
        if radius < 0:
            raise ValueError(f'Radius should be greater than 0')

        self._radius = radius

        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def edge_count(self):
        """Get edge count"""
        return(self._vert_count) # same as vertices count hence no need to check

    @property
    def interior_angle(self):
        """Get interior angle value"""
        if self._interior_angle is None:
            self._interior_angle = ((self.vert_count - 2)*180)/math.pi
        return(self._interior_angle)

    @property
    def edge_length(self):
        """Get edge length value"""
        if self._edge_length is None:
            self._edge_length = 2 * self.radius * math.sin(math.pi / self.vert_count)
        return(self._edge_length)

    @property
    def apothem(self):
        """Get apothem value"""
        if self._apothem is None:
            self._apothem = self.radius * math.cos(math.pi / self.vert_count)
        return(self._apothem)

    @property
    def area(self):
        """Get area value"""
        if self._area is None:
            self._area  = 1 / 2 * (self.vert_count * self.edge_length * self.apothem)
        return(self._area)

    @property
    def perimeter(self):
        """Get perimeter value"""
        if self._perimeter is None:
            self._perimeter = self.vert_count * self.edge_length
        return(self._perimeter)

    def __repr__(self):
        """ Return string for RegularPoly"""
        return (f'RegularPoly({self.vert_count}, {self.radius})')

    def __str__(self):
        """ String representation for RegularPoly"""
        return(f'Regular Polygon:-\n number of vertices = {self.vert_count},\n radius = {self.radius}, \
                 \n interior angle = {self.interior_angle}, \n edge length = {self.edge_length}, \
                 \n apothem = {self.apothem}, \n area = {self.area}, \n perimeter = {self.perimeter}')

    def __eq__(self,other):
        """ Check for the equality of RegularPoly"""
        if isinstance(other, RegularPoly):
            return(self.vert_count == other.vert_count and self.radius == other.radius)
        else:
            raise NotImplementedError('Incorrect data type')

    def __gt__(self,other):
        """ Check for the greater than ineqaulity for RegularPoly"""
        if isinstance(other, RegularPoly):
            return(self.vert_count > other.vert_count)
        else:
            raise NotImplementedError('Incorrect data type')
