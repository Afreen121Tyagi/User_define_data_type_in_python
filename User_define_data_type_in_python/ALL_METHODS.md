# All Methods and Conditions in cordination_geo.py

## CLASS: Point

### Special Methods (Dunder Methods)
1. `__init__(x, y)` - Initialize with x, y coordinates
2. `__repr__()` - String representation
3. `__eq__(other)` - Equality comparison with floating-point tolerance
4. `__add__(other)` - Vector addition (p1 + p2)
5. `__sub__(other)` - Vector subtraction (p1 - p2)
6. `__neg__()` - Negation (-p)
7. `__mul__(scalar)` - Scalar multiplication (p * 2)
8. `__rmul__(scalar)` - Right multiplication (2 * p)

### Class Methods
1. `from_tuple(t)` - Create point from tuple (x, y)

### Instance Methods
1. `to_tuple()` - Convert to tuple (x, y)
2. `copy()` - Return a copy of the point
3. `distance_to(other)` - Euclidean distance to another point
4. `distance_from_origin()` - Distance from origin (0, 0)
5. `magnitude()` - Magnitude (length) of vector
6. `normalize()` - Unit vector in same direction
7. `dot(other)` - Dot product with another vector
8. `cross(other)` - 2D cross product (scalar)
9. `angle_between(other)` - Signed angle from self to other
10. `rotate(angle_rad, origin)` - Rotate around origin
11. `midpoint(other)` - Midpoint between two points

### Alias
- `length` - Alias for magnitude()

---

## CLASS: Line

### Special Methods (Dunder Methods)
1. `__init__(A, B, C)` - Initialize with coefficients (Ax + By + C = 0)
2. `__repr__()` - String representation of line equation

### Class Methods
1. `from_points(p1, p2)` - Construct line through two points

### Instance Methods
1. `as_coeffs()` - Return coefficients (A, B, C)
2. `slope()` - Return slope or None if vertical
3. `is_vertical()` - Check if line is vertical (B ≈ 0)
4. `is_horizontal()` - Check if line is horizontal (A ≈ 0)
5. `contains_point(point)` - Check if point lies on line
6. `shortest_distance_to_point(point)` - Perpendicular distance from point
7. `is_parallel(other)` - Check if two lines are parallel
8. `is_perpendicular(other)` - Check if two lines are perpendicular
9. `intersection_with(other)` - Find intersection point or None
10. `project_point(point)` - Project point orthogonally onto line
11. `angle()` - Angle of line direction vector
12. `unit_normal()` - Unit normal vector as Point
13. `offset(distance)` - Parallel line shifted by distance
14. `parallel_through(point)` - Parallel line through point
15. `perpendicular_through(point)` - Perpendicular line through point

---

## SUMMARY

- **Point Class**: 8 dunder methods + 1 class method + 11 instance methods + 1 alias = **21 total**
- **Line Class**: 2 dunder methods + 1 class method + 13 instance methods = **16 total**
- **Grand Total**: **37 methods** across both classes

---

## METHOD CATEGORIES

### Initialization & Representation
- Point: `__init__`, `__repr__`, `to_tuple`, `from_tuple`, `copy`
- Line: `__init__`, `__repr__`, `from_points`, `as_coeffs`

### Arithmetic & Vector Operations
- Point: `__add__`, `__sub__`, `__neg__`, `__mul__`, `__rmul__`, `dot`, `cross`
- Line: (none)

### Comparisons & Checks
- Point: `__eq__`, `distance_to`, `distance_from_origin`
- Line: `is_vertical`, `is_horizontal`, `contains_point`, `is_parallel`, `is_perpendicular`

### Transformations & Projections
- Point: `normalize`, `rotate`, `magnitude`, `angle_between`, `midpoint`
- Line: `offset`, `parallel_through`, `perpendicular_through`, `project_point`

### Geometry & Analysis
- Point: (none - covered in transformations)
- Line: `slope`, `shortest_distance_to_point`, `intersection_with`, `angle`, `unit_normal`

---

## CONDITION CHECKS

### Boolean Returns (Conditions)
1. `Point.__eq__(other)` → boolean (equality)
2. `Line.is_vertical()` → boolean (vertical check)
3. `Line.is_horizontal()` → boolean (horizontal check)
4. `Line.contains_point(point)` → boolean (point on line)
5. `Line.is_parallel(other)` → boolean (parallel check)
6. `Line.is_perpendicular(other)` → boolean (perpendicular check)

### Returns with Conditional Logic (None possible)
1. `Line.slope()` → Optional[float] (None if vertical)
2. `Line.intersection_with(other)` → Optional[Point] (None if parallel)
