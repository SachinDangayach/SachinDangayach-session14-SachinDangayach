# EPAI Session 14 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Sequence Types - 2 ". Here we went through iterators which are objects that implement the \_\_iter__ and \_\_next__ methods while a class only implementing \_\_iter__ is an iterable. We can use iterators to parse through un-ordered types like sets and Dictionary aprt from ordered types like List and Tuple are sequence type.  We have refactored the classes we developed in session13 with following objectives-
1. Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").
2. Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons. Implement both an iterable, and an iterator.

Solution:-

**Class is implemented in Module regular_poly.py**

https://github.com/SachinDangayach/SachinDangayach-session14-SachinDangayach/blob/master/regular_poly.py

**Class is implemented in Module regular_poly.py**

https://github.com/SachinDangayach/SachinDangayach-session14-SachinDangayach/blob/master/regular_poly_seq.py

**Ipynb file to test the above mentioned Modules**

https://github.com/SachinDangayach/SachinDangayach-session14-SachinDangayach/blob/master/session14.ipynb


1. We have implemented a Regular Polygon class which takes number or vertices and circumradius and gives a polygon class object with following properties-
- Create a Polygon Class:
    - 1. where initializer takes in:
        - 1. number of edges/vertices
        - 2. circumradius
    - 2. it provide following properties:
        - 1. number of edges
        - 2. number of  vertices
        - 3. interior angle
        - 4. edge length
        - 5. apothem
        - 6. area
        - 7. perimeter
    - 3. that has these functionalities:
        - 1. a proper \_\_repr__ function
        - 2. implements equality (==) based on # vertices and circumradius (\_\_eq__)
        - 3. implements > based on number of vertices only (\_\_gt__)

### We have implemented the concepts of lazy loading where in the first case, the class properties are evaluated only once till the radius or number of vertices is changed. These are evaluated only when these properties are referenced.

2. Implement a Custom Polygon iterable class which has got a class for iterator:
  - 1. where initializer takes in:
      - 1. number of vertices for largest polygon in the sequence
      - 2. common circumradius for all polygons
  - 2. that has these functionalities:
      - 1. method for iterable (\_\_iter__)
      - 2. class for iterable having the \_\_iter__ and \_\_next__ methods

### We have implemented the concepts of iterable and iterator where the next object is evaluated and returned one by one and objects are not pre-computed and stored.

# Session14.pynb file calls the Modules with above mentioned classes and performs the required tests to check the functionalities.
