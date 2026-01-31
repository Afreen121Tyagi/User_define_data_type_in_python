import math
from cordination_geo import Point, Line


def test_point_initialization():
    """Test Point creation and representation."""
    p = Point(3, 4)
    assert p.x == 3.0
    assert p.y == 4.0
    assert str(p) == "(3.0, 4.0)"
    print("✓ Point initialization")


def test_point_equality():
    """Test Point equality with floating-point tolerance."""
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(1, 2.0000000001)
    assert p1 == p2
    assert p1 == p3  # Within tolerance
    assert not (p1 == Point(1, 3))
    print("✓ Point equality")


def test_point_arithmetic():
    """Test Point addition, subtraction, negation."""
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    
    # Addition
    p3 = p1 + p2
    assert p3.x == 4 and p3.y == 6
    
    # Subtraction
    p4 = p1 - p2
    assert p4.x == 2 and p4.y == 2
    
    # Negation
    p5 = -p1
    assert p5.x == -3 and p5.y == -4
    
    print("✓ Point arithmetic (add, sub, neg)")


def test_point_scalar_multiplication():
    """Test Point scalar multiplication."""
    p = Point(2, 3)
    
    # Left multiplication
    p2 = p * 2
    assert p2.x == 4 and p2.y == 6
    
    # Right multiplication
    p3 = 3 * p
    assert p3.x == 6 and p3.y == 9
    
    # Fractional
    p4 = p * 0.5
    assert p4.x == 1 and p4.y == 1.5
    
    print("✓ Point scalar multiplication")


def test_point_distance():
    """Test distance calculations."""
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # Distance between points
    assert math.isclose(p1.distance_to(p2), 5)
    
    # Distance from origin
    assert math.isclose(p2.distance_from_origin(), 5)
    
    # Same point
    assert math.isclose(p1.distance_to(p1), 0)
    
    print("✓ Point distance")


def test_point_magnitude_and_normalization():
    """Test magnitude and normalize."""
    p = Point(3, 4)
    
    # Magnitude
    assert math.isclose(p.magnitude(), 5)
    assert math.isclose(p.magnitude(), 5)  # length is alias
    
    # Normalize
    n = p.normalize()
    assert math.isclose(n.magnitude(), 1.0)
    assert math.isclose(n.x, 0.6)
    assert math.isclose(n.y, 0.8)
    
    # Zero vector raises error
    try:
        Point(0, 0).normalize()
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    
    print("✓ Point magnitude and normalization")


def test_point_dot_product():
    """Test dot product."""
    p1 = Point(1, 0)
    p2 = Point(0, 1)
    p3 = Point(2, 3)
    
    # Orthogonal vectors
    assert math.isclose(p1.dot(p2), 0)
    
    # Dot with itself
    assert math.isclose(p3.dot(p3), 13)
    
    # Commutative
    assert math.isclose(p1.dot(p3), p3.dot(p1))
    
    print("✓ Point dot product")


def test_point_cross_product():
    """Test 2D cross product."""
    p1 = Point(1, 0)
    p2 = Point(0, 1)
    p3 = Point(2, 3)
    
    # Cross product properties
    assert math.isclose(p1.cross(p2), 1)
    assert math.isclose(p2.cross(p1), -1)
    assert math.isclose(p1.cross(p1), 0)
    
    # General test
    assert math.isclose(p3.cross(Point(1, 2)), 1)  # 2*2 - 3*1 = 1
    
    print("✓ Point cross product")


def test_point_angle_between():
    """Test angle between vectors."""
    p1 = Point(1, 0)
    p2 = Point(0, 1)
    
    # Right angle (pi/2)
    angle = p1.angle_between(p2)
    assert math.isclose(angle, math.pi / 2, abs_tol=1e-9)
    
    # Opposite direction (pi)
    angle2 = p1.angle_between(Point(-1, 0))
    assert math.isclose(abs(angle2), math.pi, abs_tol=1e-9)
    
    print("✓ Point angle between")


def test_point_rotation():
    """Test point rotation."""
    p = Point(1, 0)
    
    # Rotate 90 degrees (pi/2)
    p_rotated = p.rotate(math.pi / 2)
    assert math.isclose(p_rotated.x, 0, abs_tol=1e-9)
    assert math.isclose(p_rotated.y, 1, abs_tol=1e-9)
    
    # Rotate 180 degrees around origin
    p2 = Point(1, 1)
    p2_rotated = p2.rotate(math.pi)
    assert math.isclose(p2_rotated.x, -1, abs_tol=1e-9)
    assert math.isclose(p2_rotated.y, -1, abs_tol=1e-9)
    
    # Rotate around different origin
    origin = Point(1, 0)
    p3 = Point(2, 0)
    p3_rotated = p3.rotate(math.pi / 2, origin)
    assert math.isclose(p3_rotated.x, 1, abs_tol=1e-9)
    assert math.isclose(p3_rotated.y, 1, abs_tol=1e-9)
    
    print("✓ Point rotation")


def test_point_midpoint():
    """Test midpoint calculation."""
    p1 = Point(0, 0)
    p2 = Point(4, 6)
    
    mid = p1.midpoint(p2)
    assert math.isclose(mid.x, 2) and math.isclose(mid.y, 3)
    
    # Midpoint with itself
    mid2 = p1.midpoint(p1)
    assert math.isclose(mid2.x, 0) and math.isclose(mid2.y, 0)
    
    print("✓ Point midpoint")


def test_point_tuple_conversion():
    """Test tuple conversion."""
    p = Point(3, 4)
    t = p.to_tuple()
    assert t == (3.0, 4.0)
    
    p2 = Point.from_tuple(t)
    assert p2 == p
    
    print("✓ Point tuple conversion")


def test_point_copy():
    """Test point copying."""
    p1 = Point(3, 4)
    p2 = p1.copy()
    
    assert p2 == p1
    assert p2 is not p1  # Different objects
    
    p2.x = 10
    assert p1.x == 3  # Original unchanged
    
    print("✓ Point copy")


def test_line_initialization():
    """Test Line creation and representation."""
    line = Line(2, -3, 6)
    assert line.A == 2
    assert line.B == -3
    assert line.C == 6
    print("✓ Line initialization")


def test_line_from_points():
    """Test creating line from two points."""
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    
    line = Line.from_points(p1, p2)
    
    # Check both points are on the line
    assert line.contains_point(p1)
    assert line.contains_point(p2)
    
    print("✓ Line from points")


def test_line_coefficients():
    """Test getting line coefficients."""
    line = Line(1, 2, 3)
    A, B, C = line.as_coeffs()
    assert A == 1 and B == 2 and C == 3
    print("✓ Line coefficients")


def test_line_slope():
    """Test slope calculation."""
    # Non-vertical line: 2x - 4y + 6 = 0 => y = 0.5x + 1.5
    line = Line(2, -4, 6)
    assert math.isclose(line.slope(), 0.5)
    
    # Vertical line: x = 5 => 1x + 0y - 5 = 0
    line_vert = Line(1, 0, -5)
    assert line_vert.slope() is None
    assert line_vert.is_vertical()
    
    # Horizontal line: y = 3 => 0x + 1y - 3 = 0
    line_horiz = Line(0, 1, -3)
    assert math.isclose(line_horiz.slope(), 0)
    assert line_horiz.is_horizontal()
    
    print("✓ Line slope and properties")


def test_line_contains_point():
    """Test point containment on line."""
    line = Line(1, -1, 0)  # x - y = 0 => y = x
    
    assert line.contains_point(Point(0, 0))
    assert line.contains_point(Point(5, 5))
    assert not line.contains_point(Point(1, 2))
    
    print("✓ Line contains point")


def test_line_distance_to_point():
    """Test perpendicular distance from point to line."""
    # Line: 3x + 4y - 12 = 0
    line = Line(3, 4, -12)
    p = Point(2, 3)
    
    # Distance = |3*2 + 4*3 - 12| / sqrt(9+16) = |6+12-12| / 5 = 6/5 = 1.2
    dist = line.shortest_distance_to_point(p)
    assert math.isclose(dist, 1.2)
    
    # Point on line has distance 0
    p2 = Point(0, 3)
    assert math.isclose(line.shortest_distance_to_point(p2), 0)
    
    print("✓ Line distance to point")


def test_line_parallel_perpendicular():
    """Test parallelism and perpendicularity."""
    line1 = Line(2, 3, 5)
    line2 = Line(4, 6, 10)  # Parallel to line1
    line3 = Line(3, -2, 7)  # Perpendicular to line1 (2*3 + 3*(-2) = 0)
    line4 = Line(1, 1, 0)   # Neither
    
    # Parallel
    assert line1.is_parallel(line2)
    assert line2.is_parallel(line1)
    
    # Perpendicular
    assert line1.is_perpendicular(line3)
    assert line3.is_perpendicular(line1)
    
    # Not parallel/perpendicular
    assert not line1.is_parallel(line4)
    assert not line1.is_perpendicular(line4)
    
    print("✓ Line parallel and perpendicular")


def test_line_intersection():
    """Test line intersection."""
    line1 = Line(1, -1, 0)  # x - y = 0
    line2 = Line(1, 1, -4)  # x + y - 4 = 0
    
    # Intersection at (2, 2)
    inter = line1.intersection_with(line2)
    assert inter is not None
    assert math.isclose(inter.x, 2)
    assert math.isclose(inter.y, 2)
    
    # Parallel lines
    line3 = Line(1, -1, 5)  # x - y + 5 = 0 (parallel to line1)
    inter2 = line1.intersection_with(line3)
    assert inter2 is None
    
    print("✓ Line intersection")


def test_line_project_point():
    """Test point projection onto line."""
    line = Line(1, 0, -5)  # x - 5 = 0 (vertical line x=5)
    p = Point(2, 3)
    
    # Project (2,3) onto x=5 gives (5,3)
    proj = line.project_point(p)
    assert math.isclose(proj.x, 5)
    assert math.isclose(proj.y, 3)
    
    # Project point already on line
    p2 = Point(5, 3)
    proj2 = line.project_point(p2)
    assert proj2 == p2
    
    print("✓ Line project point")


def test_line_angle():
    """Test line angle."""
    # Horizontal line: A=0, B=1 => direction vector (1, 0) => angle 0
    line_horiz = Line(0, 1, 0)
    assert math.isclose(line_horiz.angle(), 0, abs_tol=1e-9)
    
    # Vertical line: A=1, B=0 => direction vector (0, -1) => angle -pi/2
    line_vert = Line(1, 0, 0)
    angle_vert = line_vert.angle()
    assert math.isclose(abs(angle_vert), math.pi / 2, abs_tol=1e-9)
    
    print("✓ Line angle")


def test_line_unit_normal():
    """Test unit normal vector."""
    line = Line(3, 4, 5)
    normal = line.unit_normal()
    
    # Normal should be (3/5, 4/5)
    assert math.isclose(normal.x, 0.6)
    assert math.isclose(normal.y, 0.8)
    assert math.isclose(normal.magnitude(), 1.0)
    
    print("✓ Line unit normal")


def test_line_offset():
    """Test line offset (parallel shift)."""
    line = Line(1, 0, -5)  # x - 5 = 0 => x = 5
    offset_line = line.offset(3)
    
    # offset by 3 along normal (1, 0) shifts x by 3 (adds to C)
    # New line: x - 8 = 0 => x = 8
    assert offset_line.contains_point(Point(8, 0))
    assert offset_line.contains_point(Point(8, 100))
    assert not offset_line.contains_point(Point(5, 0))
    
    print("✓ Line offset")


def test_line_parallel_through():
    """Test parallel line through point."""
    line = Line(2, 3, 5)
    p = Point(1, 1)
    
    parallel = line.parallel_through(p)
    
    # New line should pass through p
    assert parallel.contains_point(p)
    
    # Should be parallel to original
    assert line.is_parallel(parallel)
    
    print("✓ Line parallel through point")


def test_line_perpendicular_through():
    """Test perpendicular line through point."""
    line = Line(2, -3, 6)
    p = Point(0, 0)
    
    perp = line.perpendicular_through(p)
    
    # New line should pass through p
    assert perp.contains_point(p)
    
    # Should be perpendicular to original
    assert line.is_perpendicular(perp)
    
    print("✓ Line perpendicular through point")


def test_integration_triangle_centroid():
    """Test finding centroid of a triangle."""
    A = Point(0, 0)
    B = Point(4, 0)
    C = Point(0, 3)
    
    # Centroid = ((x1+x2+x3)/3, (y1+y2+y3)/3)
    centroid = Point((A.x + B.x + C.x) / 3, (A.y + B.y + C.y) / 3)
    assert math.isclose(centroid.x, 4/3)
    assert math.isclose(centroid.y, 1)
    
    print("✓ Integration: triangle centroid")


def test_integration_lines_and_distances():
    """Test complex interaction of lines and distances."""
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    line = Line.from_points(p1, p2)
    p_external = Point(3, 0)
    
    # Distance from external point to line
    dist = line.shortest_distance_to_point(p_external)
    
    # Project point to line
    proj = line.project_point(p_external)
    
    # Distance from point to projection should equal shortest distance
    assert math.isclose(proj.distance_to(p_external), dist)
    
    print("✓ Integration: lines and distances")


if __name__ == "__main__":
    print("Running Coordinate Geometry Tests...\n")
    
    # Point tests
    test_point_initialization()
    test_point_equality()
    test_point_arithmetic()
    test_point_scalar_multiplication()
    test_point_distance()
    test_point_magnitude_and_normalization()
    test_point_dot_product()
    test_point_cross_product()
    test_point_angle_between()
    test_point_rotation()
    test_point_midpoint()
    test_point_tuple_conversion()
    test_point_copy()
    
    # Line tests
    test_line_initialization()
    test_line_from_points()
    test_line_coefficients()
    test_line_slope()
    test_line_contains_point()
    test_line_distance_to_point()
    test_line_parallel_perpendicular()
    test_line_intersection()
    test_line_project_point()
    test_line_angle()
    test_line_unit_normal()
    test_line_offset()
    test_line_parallel_through()
    test_line_perpendicular_through()
    
    # Integration tests
    test_integration_triangle_centroid()
    test_integration_lines_and_distances()
    
    print("\n✅ All tests passed!")
