# RegularPolySeq.py

import regular_poly as rp

"""Regular Polygon iterable class"""
class RegularPolySeq:
    """Class to create a sequence of regular polygon"""

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

    def __getitem__(self, seq):
        """get next item in the sequence"""
        if isinstance(seq, int):
            seq = seq + 3
            if seq - 3 < 0:
                seq = self.vert_count + seq - 3
            if seq  < 3 or seq > self.vert_count:
                raise IndexError
            else:
                if seq >=3:
                    return rp.RegularPoly(seq, self.radius)
        else:
            raise TypeError ('Please provide valid integer value')

    def __len__(self):
        """get length of sequence"""
        return self.vert_count - 2

    def __str__(self):
        """String represnetation"""
        return f"Polygon iterable with seq_len = {self.vert_count - 2} and common cirum_radius = {self.radius}"

    def __repr__(self):
        """ Return string for RegularPolySeq"""
        return (f'RegularPolySeq({self.vert_count}, {self.radius})')

    def __iter__(self):
        """Get the iterable"""
        # return self.PolyIterator(self,
        #                          vert_count = self.vert_count,
        #                          radius=self.radius)
        return self.PolyIterator(self)


    class PolyIterator:
        """Class for iterator"""
        def __init__(self,poly_obj):
            self.vert_count = poly_obj.vert_count
            self.radius = poly_obj.radius
            self.current_poly_count = poly_obj.vert_count

        def __iter__(self):
            """return iterator"""
            return self

        def __next__(self):
            """Get next item in the iterator"""
            if self.current_poly_count < 3:
                raise StopIteration
            else:
                current_poly = rp.RegularPoly(self.current_poly_count, self.radius)
                self.current_poly_count -= 1
                return current_poly

        def __str__(self):
            """String represnetation"""
            return f"Polygon iterator with item count = {self.vert_count - 2} and common cirum_radius = {self.radius}"

        def __repr__(self):
            """ Return string for RegularPolySeq"""
            return (f'RegularPolySeq({self.vert_count}, {self.radius})')
