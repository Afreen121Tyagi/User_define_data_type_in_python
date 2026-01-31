# User-Defined Data Types in Python

A comprehensive collection of professional-grade custom data types.

## Included Data Types

### 1. Coordinate Geometry: Point and Line Classes
Complete implementation of 2D Euclidean geometry with vector and line operations.

**Files:** `cordination_geo.py`, `test_cordination_geo.py`

#### Point Class
A 2D Euclidean point with full vector-like operations.

**Basic Operations:**
- `Point(x, y)` – initialize with coordinates
- `p1 + p2` – vector addition
- `p1 - p2` – vector subtraction
- `p * scalar` – scalar multiplication
- `-p` – negation
- `p1 == p2` – equality (with floating-point tolerance)

**Distance & Magnitude:**
- `p.distance_to(other)` – Euclidean distance to another point
- `p.distance_from_origin()` – distance from origin (0,0)
- `p.magnitude()` or `p.length` – magnitude as a vector
- `p.normalize()` – return unit vector

**Vector Operations:**
- `p1.dot(p2)` – dot product
- `p1.cross(p2)` – 2D cross product (scalar)
- `p1.angle_between(p2)` – signed angle between vectors (radians)

**Geometric Operations:**
- `p.rotate(angle, origin=None)` – rotate around a point
- `p1.midpoint(p2)` – midpoint between two points
- `p.to_tuple()` / `Point.from_tuple((x, y))` – conversions
- `p.copy()` – create a copy

#### Line Class
A line in implicit form: **Ax + By + C = 0**

**Initialization:**
- `Line(A, B, C)` – create line from coefficients
- `Line.from_points(p1, p2)` – create line through two points

**Line Properties:**
- `line.slope()` – return slope or `None` if vertical
- `line.is_vertical()` – check if vertical
- `line.is_horizontal()` – check if horizontal
- `line.unit_normal()` – unit normal vector
- `line.angle()` – direction angle (radians)

**Point Relationships:**
- `line.contains_point(p)` – check if point on line
- `line.shortest_distance_to_point(p)` – perpendicular distance
- `line.project_point(p)` – orthogonal projection of point onto line

**Line Relationships:**
- `l1.is_parallel(l2)` – check if lines are parallel
- `l1.is_perpendicular(l2)` – check if lines are perpendicular
- `l1.intersection_with(l2)` – find intersection point (or `None` if parallel)

**Line Transformations:**
- `line.offset(distance)` – create parallel line shifted by distance
- `line.parallel_through(point)` – create parallel line through point
- `line.perpendicular_through(point)` – create perpendicular line through point

---

### 2. Fraction Data Type
Complete rational number implementation with automatic reduction and comprehensive arithmetic.

**Files:** `fraction_data_type.py`, `test_fraction_data_type.py`

#### FractionDataType Class
Represents fractions in reduced form (e.g., 3/4 automatically reduces 6/8).

**Initialization:**
- `FractionDataType(num, den)` – create fraction (auto-reduces)
- `FractionDataType(5)` – create integer as fraction (5/1)
- Automatic GCD reduction and normalization (denominator always positive)
- Zero denominator validation

**Arithmetic Operations:**
- `f1 + f2` – addition
- `f1 - f2` – subtraction
- `f1 * f2` – multiplication
- `f1 / f2` – division
- `f1 ** n` – power (supports negative exponents)
- `f1 // f2` – floor division (returns int)
- `f1 % f2` – modulo operation
- `-f` – negation
- `+f` – positive (no-op)
- `abs(f)` – absolute value

**Mixed Arithmetic (with integers):**
- `f + 2`, `2 + f` – addition
- `f - 2`, `2 - f` – subtraction
- `f * 3`, `3 * f` – multiplication
- `f / 2`, `2 / f` – division

**Comparison Operations:**
- `f1 == f2` – equality
- `f1 != f2` – inequality
- `f1 < f2` – less than
- `f1 <= f2` – less than or equal
- `f1 > f2` – greater than
- `f1 >= f2` – greater than or equal
- Works with both fractions and integers

**Type Conversions:**
- `float(f)` – convert to decimal
- `int(f)` – convert to integer (truncates)
- `str(f)` – readable string ("3/4")
- `repr(f)` – formal representation
- `hash(f)` – for use in sets/dicts

**Utility Methods:**
- `f.reciprocal()` – return 1/f
- `f.simplify()` – explicit simplification (already auto-done)
- `f.as_mixed_number()` – return (whole, numerator, denominator)
- `f.is_proper()` – check if |numerator| < denominator
- `f.is_improper()` – check if |numerator| >= denominator

**Class Methods:**
- `FractionDataType.from_float(0.75)` – create fraction from decimal
- `FractionDataType.from_mixed(2, 1, 3)` – create from mixed number (2 1/3 = 7/3)

## Examples

### Coordinate Geometry

```python
from cordination_geo import Point, Line

# Points
p1 = Point(3, 4)
p2 = Point(6, 8)
print(p1.distance_to(p2))      # 5.0
print((p1 + p2) / 2)           # Midpoint operations

# Lines
line = Line.from_points(Point(0, 0), Point(1, 1))  # y = x
print(line.contains_point(Point(2, 2)))            # True
print(line.shortest_distance_to_point(Point(1, 0)))# ~0.707

# Line operations
l_horiz = Line(0, 1, -2)       # y = 2
l_vert = Line(1, 0, -3)        # x = 3
print(l_horiz.intersection_with(l_vert))  # (3.0, 2.0)
```

### Fractions

```python
from fraction_data_type import FractionDataType

f1 = FractionDataType(3, 4)
f2 = FractionDataType(2, 5)

print(f1 + f2)                 # 23/20
print(f1 * f2)                 # 3/10
print(f1 / f2)                 # 15/8

# Mixed with integers
print(f1 + 2)                  # 11/4
print(3 - f1)                  # 9/4

# Comparisons
print(f1 > f2)                 # True
print(f1 == FractionDataType(6, 8))  # True (auto-reduced)

# Conversions
print(float(f1))               # 0.75
print(FractionDataType.from_float(0.75))  # 3/4
```

## Running Tests

```bash
# Test coordinate geometry
python test_cordination_geo.py

# Test fraction data type
python test_fraction_data_type.py
```

All tests pass ✅

## Implementation Highlights

**Cordination Geometry:**
- Uses `math.isclose()` for robust floating-point comparisons
- Type hints throughout for IDE support
- Comprehensive docstrings
- Proper error handling (e.g., normalizing zero vectors)

**Fraction:**
- Automatic GCD reduction for all operations
- Denominator always positive (consistent representation)
- Mixed arithmetic with both fractions and integers
- Reverse operators for expressions like `2 + Fraction(1,3)`
- Hashable (can use in sets/dicts)
- Proper mathematical semantics (e.g., division by zero raises ValueError)
