"""
Comprehensive demonstration of all methods in Point and Line classes.
Calls every method and prints the results.
"""

import math
from cordination_geo import Point, Line

print("=" * 80)
print("COMPREHENSIVE DEMONSTRATION OF ALL POINT AND LINE METHODS")
print("=" * 80)

# ==================== POINT CLASS DEMONSTRATIONS ====================
print("\n" + "=" * 80)
print("POINT CLASS - ALL METHODS")
print("=" * 80)

# Create sample points
p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(6, 8)
origin = Point(0, 0)

print("\n1. __init__(x, y) - Initialize Point")
print(f"   p1 = Point(3, 4)")
print(f"   p1.x = {p1.x}, p1.y = {p1.y}")

print("\n2. __repr__() - String Representation")
print(f"   repr(p1) = {repr(p1)}")
print(f"   repr(p2) = {repr(p2)}")

print("\n3. __eq__(other) - Equality Comparison")
p1_copy = Point(3, 4)
p_different = Point(3, 5)
print(f"   p1 == Point(3, 4) → {p1 == p1_copy}")
print(f"   p1 == Point(3, 5) → {p1 == p_different}")

print("\n4. __add__(other) - Vector Addition (p1 + p2)")
result_add = p1 + p2
print(f"   Point(3, 4) + Point(1, 2) = {result_add}")

print("\n5. __sub__(other) - Vector Subtraction (p1 - p2)")
result_sub = p1 - p2
print(f"   Point(3, 4) - Point(1, 2) = {result_sub}")

print("\n6. __neg__() - Negation (-p1)")
result_neg = -p1
print(f"   -Point(3, 4) = {result_neg}")

print("\n7. __mul__(scalar) - Scalar Multiplication (p1 * 2)")
result_mul = p1 * 2
print(f"   Point(3, 4) * 2 = {result_mul}")

print("\n8. __rmul__(scalar) - Right Multiplication (3 * p1)")
result_rmul = 3 * p1
print(f"   3 * Point(3, 4) = {result_rmul}")

print("\n9. to_tuple() - Convert to Tuple")
tuple_result = p1.to_tuple()
print(f"   Point(3, 4).to_tuple() = {tuple_result}")

print("\n10. from_tuple(t) - Create Point from Tuple")
p_from_tuple = Point.from_tuple((5, 7))
print(f"   Point.from_tuple((5, 7)) = {p_from_tuple}")

print("\n11. copy() - Create a Copy")
p1_copy = p1.copy()
print(f"   Point(3, 4).copy() = {p1_copy}")
print(f"   Are they equal? {p1 == p1_copy}")
print(f"   Are they the same object? {p1 is p1_copy}")

print("\n12. distance_to(other) - Euclidean Distance to Another Point")
distance = p1.distance_to(p2)
print(f"   Point(3, 4).distance_to(Point(1, 2)) = {distance}")

print("\n13. distance_from_origin() - Distance from Origin (0, 0)")
dist_origin = p1.distance_from_origin()
print(f"   Point(3, 4).distance_from_origin() = {dist_origin}")

print("\n14. magnitude() - Magnitude (Length) of Vector")
magnitude = p1.magnitude()
print(f"   Point(3, 4).magnitude() = {magnitude}")

print("\n15. length - Alias for magnitude()")
length = p1.magnitude()
print(f"   Point(3, 4).length (via magnitude()) = {length}")

print("\n16. normalize() - Unit Vector in Same Direction")
p_normalized = p1.normalize()
print(f"   Point(3, 4).normalize() = {p_normalized}")
print(f"   Magnitude of normalized: {p_normalized.magnitude()}")

print("\n17. dot(other) - Dot Product")
dot_product = p1.dot(p2)
print(f"   Point(3, 4).dot(Point(1, 2)) = {dot_product}")

print("\n18. cross(other) - 2D Cross Product (scalar)")
cross_product = p1.cross(p2)
print(f"   Point(3, 4).cross(Point(1, 2)) = {cross_product}")

print("\n19. angle_between(other) - Signed Angle from self to other (radians)")
p_right = Point(1, 0)
p_up = Point(0, 1)
angle = p_right.angle_between(p_up)
angle_degrees = math.degrees(angle)
print(f"   Point(1, 0).angle_between(Point(0, 1)) = {angle} rad = {angle_degrees}°")

print("\n20. rotate(angle_rad, origin) - Rotate Point by Angle")
p_rotate = Point(1, 0)
p_rotated = p_rotate.rotate(math.pi / 2)  # 90 degrees
print(f"   Point(1, 0).rotate(π/2) = {p_rotated}")

print("\n21. midpoint(other) - Midpoint Between Two Points")
mid = p1.midpoint(p2)
print(f"   Point(3, 4).midpoint(Point(1, 2)) = {mid}")

# ==================== LINE CLASS DEMONSTRATIONS ====================
print("\n" + "=" * 80)
print("LINE CLASS - ALL METHODS")
print("=" * 80)

# Create sample lines
line1 = Line(2, -3, 6)
line2 = Line(1, 1, -4)
line3 = Line(2, -3, 0)  # Parallel to line1
line4 = Line(3, 2, 5)   # Perpendicular to line1 (2*3 + (-3)*2 = 0)

print("\n1. __init__(A, B, C) - Initialize Line (Ax + By + C = 0)")
print(f"   line1 = Line(2, -3, 6)  →  2x - 3y + 6 = 0")
print(f"   line1.A = {line1.A}, line1.B = {line1.B}, line1.C = {line1.C}")

print("\n2. __repr__() - String Representation")
print(f"   repr(Line(2, -3, 6)) = {repr(line1)}")
print(f"   repr(Line(1, 1, -4)) = {repr(line2)}")

print("\n3. from_points(p1, p2) - Construct Line Through Two Points")
p_a = Point(0, 0)
p_b = Point(1, 1)
line_from_points = Line.from_points(p_a, p_b)
print(f"   Line.from_points(Point(0, 0), Point(1, 1)) = {line_from_points}")

print("\n4. as_coeffs() - Return Coefficients (A, B, C)")
coeffs = line1.as_coeffs()
print(f"   Line(2, -3, 6).as_coeffs() = {coeffs}")

print("\n5. slope() - Return Slope or None if Vertical")
slope1 = line1.slope()
print(f"   Line(2, -3, 6).slope() = {slope1}")
line_vertical = Line(1, 0, -5)
slope_vert = line_vertical.slope()
print(f"   Line(1, 0, -5).slope() = {slope_vert} (vertical line)")

print("\n6. is_vertical() - Check if Line is Vertical (B ≈ 0)")
is_vert1 = line1.is_vertical()
is_vert2 = line_vertical.is_vertical()
print(f"   Line(2, -3, 6).is_vertical() = {is_vert1}")
print(f"   Line(1, 0, -5).is_vertical() = {is_vert2}")

print("\n7. is_horizontal() - Check if Line is Horizontal (A ≈ 0)")
line_horiz = Line(0, 1, -3)
is_horiz1 = line1.is_horizontal()
is_horiz2 = line_horiz.is_horizontal()
print(f"   Line(2, -3, 6).is_horizontal() = {is_horiz1}")
print(f"   Line(0, 1, -3).is_horizontal() = {is_horiz2}")

print("\n8. contains_point(point) - Check if Point Lies on Line")
line_test = Line(1, -1, 0)  # x - y = 0
p_on_line = Point(5, 5)
p_off_line = Point(1, 2)
contains1 = line_test.contains_point(p_on_line)
contains2 = line_test.contains_point(p_off_line)
print(f"   Line(1, -1, 0).contains_point(Point(5, 5)) = {contains1}")
print(f"   Line(1, -1, 0).contains_point(Point(1, 2)) = {contains2}")

print("\n9. shortest_distance_to_point(point) - Perpendicular Distance")
line_dist = Line(3, 4, -12)  # 3x + 4y - 12 = 0
p_dist = Point(2, 3)
distance = line_dist.shortest_distance_to_point(p_dist)
print(f"   Line(3, 4, -12).shortest_distance_to_point(Point(2, 3)) = {distance}")

print("\n10. is_parallel(other) - Check if Two Lines are Parallel")
are_parallel = line1.is_parallel(line3)
not_parallel = line1.is_parallel(line2)
print(f"    Line(2, -3, 6).is_parallel(Line(2, -3, 0)) = {are_parallel}")
print(f"    Line(2, -3, 6).is_parallel(Line(1, 1, -4)) = {not_parallel}")

print("\n11. is_perpendicular(other) - Check if Two Lines are Perpendicular")
are_perp = line1.is_perpendicular(line4)
not_perp = line1.is_perpendicular(line2)
print(f"    Line(2, -3, 6).is_perpendicular(Line(3, 2, 5)) = {are_perp}")
print(f"    Line(2, -3, 6).is_perpendicular(Line(1, 1, -4)) = {not_perp}")

print("\n12. intersection_with(other) - Find Intersection Point")
inter = line1.intersection_with(line2)
inter_parallel = line1.intersection_with(line3)
print(f"    Line(2, -3, 6).intersection_with(Line(1, 1, -4)) = {inter}")
print(f"    Line(2, -3, 6).intersection_with(Line(2, -3, 0)) = {inter_parallel} (parallel)")

print("\n13. project_point(point) - Project Point onto Line")
line_proj = Line(1, 0, -5)  # x = 5
p_proj = Point(2, 3)
projected = line_proj.project_point(p_proj)
print(f"    Line(1, 0, -5).project_point(Point(2, 3)) = {projected}")

print("\n14. angle() - Angle of Line Direction Vector (in radians)")
angle_rad = line1.angle()
angle_deg = math.degrees(angle_rad)
print(f"    Line(2, -3, 6).angle() = {angle_rad} rad = {angle_deg}°")

print("\n15. unit_normal() - Unit Normal Vector as Point")
unit_norm = line1.unit_normal()
print(f"    Line(2, -3, 6).unit_normal() = {unit_norm}")
print(f"    Magnitude of normal: {unit_norm.magnitude()}")

print("\n16. offset(distance) - Parallel Line Shifted by Distance")
line_offset = Line(1, 0, -5)
offset_result = line_offset.offset(3)
print(f"    Line(1, 0, -5).offset(3) = {offset_result}")

print("\n17. parallel_through(point) - Parallel Line Through Point")
p_parallel = Point(1, 1)
parallel_line = line1.parallel_through(p_parallel)
print(f"    Line(2, -3, 6).parallel_through(Point(1, 1)) = {parallel_line}")
print(f"    Is parallel? {line1.is_parallel(parallel_line)}")

print("\n18. perpendicular_through(point) - Perpendicular Line Through Point")
p_perp = Point(0, 0)
perp_line = line1.perpendicular_through(p_perp)
print(f"    Line(2, -3, 6).perpendicular_through(Point(0, 0)) = {perp_line}")
print(f"    Is perpendicular? {line1.is_perpendicular(perp_line)}")

# ==================== SUMMARY ====================
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print("\nPoint Class Methods Called: 21")
print("  - Special methods: __init__, __repr__, __eq__, __add__, __sub__, __neg__, __mul__, __rmul__")
print("  - Instance methods: to_tuple, from_tuple, copy, distance_to, distance_from_origin,")
print("                      magnitude, normalize, dot, cross, angle_between, rotate, midpoint")
print("  - Aliases: length")

print("\nLine Class Methods Called: 18")
print("  - Special methods: __init__, __repr__")
print("  - Class method: from_points")
print("  - Instance methods: as_coeffs, slope, is_vertical, is_horizontal, contains_point,")
print("                      shortest_distance_to_point, is_parallel, is_perpendicular,")
print("                      intersection_with, project_point, angle, unit_normal, offset,")
print("                      parallel_through, perpendicular_through")

print("\nTotal Methods Demonstrated: 39")
print("=" * 80)
