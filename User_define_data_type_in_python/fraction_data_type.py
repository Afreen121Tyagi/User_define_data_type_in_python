from math import gcd
from typing import Union


class FractionDataType:
    """A complete Fraction data type supporting arithmetic, comparisons, and conversions.
    
    Fractions are stored in reduced form with denominator always positive.
    Example: FractionDataType(3, 4) represents 3/4.
    """

    def __init__(self, num: Union[int, float], den: Union[int, float] = 1):
        """Initialize a fraction with numerator and denominator.
        
        Args:
            num: Numerator (int or float)
            den: Denominator (int or float, default 1)
            
        Raises:
            ValueError: If denominator is zero
        """
        num = int(num) if isinstance(num, float) and num.is_integer() else num
        den = int(den) if isinstance(den, float) and den.is_integer() else den
        
        if den == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Convert to integers if both are integers
        if isinstance(num, (int, float)) and isinstance(den, (int, float)):
            num, den = int(num), int(den)
        
        # Normalize: make denominator always positive
        if den < 0:
            num, den = -num, -den
        
        # Reduce to simplest form using GCD
        g = gcd(abs(num), abs(den))
        self.num = num // g
        self.den = den // g

    def __repr__(self) -> str:
        """Return formal string representation."""
        return f"FractionDataType({self.num}, {self.den})"

    def __str__(self) -> str:
        """Return readable fraction string."""
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    # ============ Arithmetic Operations ============
    def __add__(self, other: 'FractionDataType') -> 'FractionDataType':
        """Add two fractions: a/b + c/d = (ad + bc)/bd."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return FractionDataType(new_num, new_den)

    def __radd__(self, other):
        """Right addition for int + Fraction."""
        return self.__add__(other)

    def __sub__(self, other: 'FractionDataType') -> 'FractionDataType':
        """Subtract two fractions: a/b - c/d = (ad - bc)/bd."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return FractionDataType(new_num, new_den)

    def __rsub__(self, other):
        """Right subtraction for int - Fraction."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        return other.__sub__(self)

    def __mul__(self, other: 'FractionDataType') -> 'FractionDataType':
        """Multiply two fractions: (a/b) * (c/d) = ac/bd."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        new_num = self.num * other.num
        new_den = self.den * other.den
        return FractionDataType(new_num, new_den)

    def __rmul__(self, other):
        """Right multiplication for int * Fraction."""
        return self.__mul__(other)

    def __truediv__(self, other: 'FractionDataType') -> 'FractionDataType':
        """Divide two fractions: (a/b) / (c/d) = ad/bc."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        if other.num == 0:
            raise ValueError("Cannot divide by zero")
        return FractionDataType(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other):
        """Right division for int / Fraction."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        return other.__truediv__(self)

    def __floordiv__(self, other: 'FractionDataType') -> int:
        """Floor division: (a/b) // (c/d) = floor(ad/bc)."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        if other.num == 0:
            raise ValueError("Cannot divide by zero")
        return (self.num * other.den) // (self.den * other.num)

    def __mod__(self, other: 'FractionDataType') -> 'FractionDataType':
        """Modulo: a % b = a - b * floor(a/b)."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        quotient = self // other
        return self - other * quotient

    def __pow__(self, exponent: int) -> 'FractionDataType':
        """Raise fraction to a power: (a/b)^n = a^n / b^n."""
        if not isinstance(exponent, int):
            raise TypeError("Exponent must be an integer")
        if exponent < 0:
            return FractionDataType(self.den ** (-exponent), self.num ** (-exponent))
        return FractionDataType(self.num ** exponent, self.den ** exponent)

    def __neg__(self) -> 'FractionDataType':
        """Negate a fraction: -a/b."""
        return FractionDataType(-self.num, self.den)

    def __pos__(self) -> 'FractionDataType':
        """Positive: +a/b."""
        return FractionDataType(self.num, self.den)

    def __abs__(self) -> 'FractionDataType':
        """Absolute value: |a/b|."""
        return FractionDataType(abs(self.num), self.den)

    # ============ Comparison Operations ============
    def __eq__(self, other) -> bool:
        """Check equality of two fractions."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        return self.num == other.num and self.den == other.den

    def __ne__(self, other) -> bool:
        """Check inequality."""
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other) -> bool:
        """Less than: a/b < c/d iff ad < bc."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        return self.num * other.den < other.num * self.den

    def __le__(self, other) -> bool:
        """Less than or equal."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        return self.num * other.den <= other.num * self.den

    def __gt__(self, other) -> bool:
        """Greater than."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        return self.num * other.den > other.num * self.den

    def __ge__(self, other) -> bool:
        """Greater than or equal."""
        if isinstance(other, int):
            other = FractionDataType(other, 1)
        if not isinstance(other, FractionDataType):
            return NotImplemented
        return self.num * other.den >= other.num * self.den

    # ============ Type Conversions ============
    def __float__(self) -> float:
        """Convert fraction to float."""
        return self.num / self.den

    def __int__(self) -> int:
        """Convert fraction to integer (truncates)."""
        return self.num // self.den

    def __hash__(self) -> int:
        """Hash for use in sets and dicts."""
        return hash((self.num, self.den))

    # ============ Utility Methods ============
    def simplify(self) -> 'FractionDataType':
        """Return simplified (reduced) fraction. Already done in __init__, but explicit for clarity."""
        return FractionDataType(self.num, self.den)

    def reciprocal(self) -> 'FractionDataType':
        """Return reciprocal (inverse): 1/(a/b) = b/a."""
        if self.num == 0:
            raise ValueError("Cannot take reciprocal of zero")
        return FractionDataType(self.den, self.num)

    def as_mixed_number(self) -> tuple:
        """Return (whole, numerator, denominator) for mixed number representation.
        
        Example: FractionDataType(7, 3) -> (2, 1, 3) meaning 2 1/3
        """
        whole = self.num // self.den
        remainder = abs(self.num) % self.den
        return (whole, remainder, self.den)

    def is_proper(self) -> bool:
        """Check if fraction is proper (|numerator| < denominator)."""
        return abs(self.num) < self.den

    def is_improper(self) -> bool:
        """Check if fraction is improper (|numerator| >= denominator)."""
        return abs(self.num) >= self.den

    @classmethod
    def from_float(cls, f: float, max_denominator: int = 10000) -> 'FractionDataType':
        """Create a fraction from a decimal approximation.
        
        Args:
            f: Float value
            max_denominator: Maximum denominator to use
            
        Returns:
            FractionDataType approximation of the float
        """
        from fractions import Fraction
        frac = Fraction(f).limit_denominator(max_denominator)
        return cls(frac.numerator, frac.denominator)

    @classmethod
    def from_mixed(cls, whole: int, num: int, den: int) -> 'FractionDataType':
        """Create fraction from mixed number: whole num/den.
        
        Example: from_mixed(2, 1, 3) creates 7/3
        """
        return cls(whole * den + num, den)


# ============ Demo ============
if __name__ == "__main__":
    print("=== Fraction Data Type Demo ===\n")
    
    # Basic creation and display
    f1 = FractionDataType(3, 4)
    f2 = FractionDataType(2, 5)
    print(f"f1 = {f1}")
    print(f"f2 = {f2}\n")
    
    # Arithmetic
    print("=== Arithmetic ===")
    print(f"{f1} + {f2} = {f1 + f2}")
    print(f"{f1} - {f2} = {f1 - f2}")
    print(f"{f1} * {f2} = {f1 * f2}")
    print(f"{f1} / {f2} = {f1 / f2}\n")
    
    # Mixed with integers
    print("=== Mixed with Integers ===")
    print(f"{f1} + 2 = {f1 + 2}")
    print(f"3 - {f1} = {3 - f1}")
    print(f"2 * {f1} = {2 * f1}\n")
    
    # Comparisons
    print("=== Comparisons ===")
    print(f"{f1} == {FractionDataType(6, 8)} : {f1 == FractionDataType(6, 8)}")
    print(f"{f1} < {f2} : {f1 < f2}")
    print(f"{f1} > {f2} : {f1 > f2}\n")
    
    # Conversions
    print("=== Conversions ===")
    print(f"float({f1}) = {float(f1)}")
    print(f"int({f1}) = {int(f1)}\n")
    
    # Utilities
    print("=== Utilities ===")
    print(f"reciprocal({f1}) = {f1.reciprocal()}")
    print(f"{f1} as mixed number: {f1.as_mixed_number()}")
    f_improper = FractionDataType(7, 3)
    print(f"{f_improper} as mixed number: {f_improper.as_mixed_number()}")
    print(f"from_float(0.75) = {FractionDataType.from_float(0.75)}")
    print(f"from_mixed(2, 1, 3) = {FractionDataType.from_mixed(2, 1, 3)}\n")
    
    # Special operations
    print("=== Special Operations ===")
    print(f"-{f1} = {-f1}")
    print(f"|{FractionDataType(-3, 4)}| = {abs(FractionDataType(-3, 4))}")
    print(f"{f1}^2 = {f1 ** 2}")
    print(f"{f1}^-1 = {f1 ** -1}")
