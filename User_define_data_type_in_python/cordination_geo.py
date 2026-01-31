import math
from typing import Tuple, Optional


class Point:
    """A 2D Euclidean point with vector-like operations.

    Attributes:
        x (float): x-coordinate
        y (float): y-coordinate

    Supports vector addition, subtraction, scalar multiplication, dot/cross products,
    normalization, rotation, and distance calculations.
    """

    def __init__(self, x: float, y: float):
        """Initialize a Point with x and y coordinates."""
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        """Return string representation of the point."""
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        """Check equality of two points with floating-point tolerance."""
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x, rel_tol=1e-9, abs_tol=1e-9) and math.isclose(self.y, other.y, rel_tol=1e-9, abs_tol=1e-9)

    def __add__(self, other):
        """Add two points (vector addition)."""
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two points (vector subtraction)."""
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """Negate a point (scalar multiplication by -1)."""
        return Point(-self.x, -self.y)

    def __mul__(self, scalar: float):
        """Multiply point by scalar (vector scaling)."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float):
        """Right multiplication for scalar * point."""
        return self.__mul__(scalar)

    def to_tuple(self) -> Tuple[float, float]:
        """Convert point to a tuple (x, y)."""
        return (self.x, self.y)

    @classmethod
    def from_tuple(cls, t: Tuple[float, float]):
        """Create a point from a tuple (x, y)."""
        return cls(t[0], t[1])

    def copy(self):
        """Return a copy of this point."""
        return Point(self.x, self.y)

    def distance_to(self, other: 'Point') -> float:
        """Compute Euclidean distance to another point."""
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point instance")
        return math.hypot(self.x - other.x, self.y - other.y)

    def distance_from_origin(self) -> float:
        """Compute distance from the origin (0, 0)."""
        return math.hypot(self.x, self.y)

    # Vector-like utilities
    def magnitude(self) -> float:
        """Return the magnitude (length) of the vector."""
        return self.distance_from_origin()

    length = magnitude

    def normalize(self) -> 'Point':
        """Return a unit vector in the same direction."""
        m = self.magnitude()
        if m == 0:
            raise ValueError("Cannot normalize zero-length vector")
        return Point(self.x / m, self.y / m)

    def dot(self, other: 'Point') -> float:
        """Compute dot product with another vector."""
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point instance")
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Point') -> float:
        """Compute 2D cross product (scalar) with another vector: self.x*other.y - self.y*other.x."""
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point instance")
        return self.x * other.y - self.y * other.x

    def angle_between(self, other: 'Point') -> float:
        """Compute signed angle (in radians) from self to other."""
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point instance")
        return math.atan2(self.cross(other), self.dot(other))

    def rotate(self, angle_rad: float, origin: Optional['Point'] = None) -> 'Point':
        """Rotate point by angle (in radians) around an origin (default: origin)."""
        if origin is None:
            origin = Point(0, 0)
        # translate
        x = self.x - origin.x
        y = self.y - origin.y
        ca = math.cos(angle_rad)
        sa = math.sin(angle_rad)
        xr = x * ca - y * sa
        yr = x * sa + y * ca
        return Point(xr + origin.x, yr + origin.y)

    def midpoint(self, other: 'Point') -> 'Point':
        """Return the midpoint between this point and another."""
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point instance")
        return Point((self.x + other.x) / 2.0, (self.y + other.y) / 2.0)


class Line:
    """A 2D line represented in implicit form: Ax + By + C = 0.

    Attributes:
        A (float): coefficient of x
        B (float): coefficient of y
        C (float): constant term

    Provides methods for geometric operations including intersection, distance,
    parallelism, perpendicularity, and point projection.

    Note: The normal vector to the line is (A, B).
    """

    def __init__(self, A: float, B: float, C: float):
        """Initialize a Line with coefficients A, B, C."""
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)

    def __repr__(self) -> str:
        """Return string representation of the line equation."""
        # Format coefficients with proper signs
        def format_term(coeff, var, is_first=False):
            if coeff == 0:
                return ""
            abs_coeff = abs(coeff)
            sign = "" if coeff >= 0 and is_first else ("+" if coeff >= 0 else "-")
            if abs_coeff == 1 and var != "":
                return f"{sign} {var}".strip()
            return f"{sign} {abs_coeff}{var}".strip()
        
        terms = []
        if self.A != 0:
            terms.append(format_term(self.A, "x", is_first=True))
        if self.B != 0:
            terms.append(format_term(self.B, "y", is_first=len(terms)==0))
        if self.C != 0:
            terms.append(format_term(self.C, "", is_first=len(terms)==0))
        
        if not terms:
            return "0 = 0"
        return " ".join(terms) + " = 0"

    @classmethod
    def from_points(cls, p1: Point, p2: Point) -> 'Line':
        """Construct a line passing through two points."""
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise ValueError("Arguments must be Point instances")
        # Line through p1(x1,y1) and p2(x2,y2): (y1 - y2)x + (x2 - x1)y + (x1*y2 - x2*y1) = 0
        A = p1.y - p2.y
        B = p2.x - p1.x
        C = p1.x * p2.y - p2.x * p1.y
        return cls(A, B, C)

    def as_coeffs(self) -> Tuple[float, float, float]:
        """Return the coefficients (A, B, C) of the line equation."""
        return (self.A, self.B, self.C)

    def slope(self) -> Optional[float]:
        """Return the slope of the line, or None if vertical."""
        if self.is_vertical():
            return None
        return -self.A / self.B

    def is_vertical(self) -> bool:
        """Check if the line is vertical (B ≈ 0)."""
        return math.isclose(self.B, 0.0, abs_tol=1e-12)

    def is_horizontal(self) -> bool:
        """Check if the line is horizontal (A ≈ 0)."""
        return math.isclose(self.A, 0.0, abs_tol=1e-12)

    def contains_point(self, point: Point) -> bool:
        """Check if a point lies on the line."""
        if not isinstance(point, Point):
            raise ValueError("Argument must be a Point instance")
        return math.isclose(self.A * point.x + self.B * point.y + self.C, 0.0, abs_tol=1e-9)

    def shortest_distance_to_point(self, point: Point) -> float:
        """Compute the perpendicular distance from a point to the line."""
        if not isinstance(point, Point):
            raise ValueError("Argument must be a Point instance")
        numerator = abs(self.A * point.x + self.B * point.y + self.C)
        denominator = math.hypot(self.A, self.B)
        return numerator / denominator

    def is_parallel(self, other: 'Line') -> bool:
        """Check if two lines are parallel."""
        if not isinstance(other, Line):
            raise ValueError("Argument must be a Line instance")
        return math.isclose(self.A * other.B, other.A * self.B, rel_tol=1e-9, abs_tol=1e-12)

    def is_perpendicular(self, other: 'Line') -> bool:
        """Check if two lines are perpendicular."""
        if not isinstance(other, Line):
            raise ValueError("Argument must be a Line instance")
        # normals dot product == 0 means lines are perpendicular
        return math.isclose(self.A * other.A + self.B * other.B, 0.0, abs_tol=1e-9)

    def intersection_with(self, other: 'Line') -> Optional[Point]:
        """Find the intersection point of two lines, or None if parallel."""
        if not isinstance(other, Line):
            raise ValueError("Argument must be a Line instance")
        determinant = self.A * other.B - other.A * self.B
        if math.isclose(determinant, 0.0, abs_tol=1e-12):
            return None
        x = (self.B * other.C - other.B * self.C) / determinant
        y = (other.A * self.C - self.A * other.C) / determinant
        return Point(x, y)

    def project_point(self, point: Point) -> Point:
        """Project a point orthogonally onto the line."""
        if not isinstance(point, Point):
            raise ValueError("Argument must be a Point instance")
        denom = self.A ** 2 + self.B ** 2
        if math.isclose(denom, 0.0):
            raise ValueError("Invalid line coefficients")
        factor = (self.A * point.x + self.B * point.y + self.C) / denom
        x = point.x - self.A * factor
        y = point.y - self.B * factor
        return Point(x, y)

    def angle(self) -> float:
        """Return the angle of the line direction vector (B, -A) in radians."""
        # angle of the line direction vector (B, -A)
        return math.atan2(-self.A, self.B)

    def unit_normal(self) -> Point:
        """Return the unit normal vector (A,B)/||(A,B)|| as a Point."""
        s = math.hypot(self.A, self.B)
        if math.isclose(s, 0.0):
            raise ValueError("Invalid line coefficients")
        return Point(self.A / s, self.B / s)

    def offset(self, distance: float) -> 'Line':
        """Return a parallel line shifted by `distance` along the normal direction.

        Positive `distance` moves the line in the direction of the normal vector (A,B).
        """
        s = math.hypot(self.A, self.B)
        if math.isclose(s, 0.0):
            raise ValueError("Invalid line coefficients")
        # New C' = C - s * distance (derived from translating points along normal)
        return Line(self.A, self.B, self.C - s * distance)

    def parallel_through(self, point: Point) -> 'Line':
        """Return a line parallel to this one that passes through `point`."""
        if not isinstance(point, Point):
            raise ValueError("Argument must be a Point instance")
        C = -(self.A * point.x + self.B * point.y)
        return Line(self.A, self.B, C)

    def perpendicular_through(self, point: Point) -> 'Line':
        """Return the line perpendicular to this one passing through `point`."""
        if not isinstance(point, Point):
            raise ValueError("Argument must be a Point instance")
        # Perpendicular line normal is (B, -A)
        A_p = self.B
        B_p = -self.A
        C_p = -(A_p * point.x + B_p * point.y)
        return Line(A_p, B_p, C_p)


if __name__ == "__main__":
    # Demo usage
    line = Line(2, 6, 6)
    point = Point(1, 2)
    print(line)
    print(point)
    print("Is the point on the line?", line.contains_point(point))
    print("Shortest distance from the point to the line:", line.shortest_distance_to_point(point))
    line2 = Line(1, -6, 12)
    inter = line.intersection_with(line2)
    print("Intersection of line and line2:", inter if inter is not None else "No intersection (parallel)")
