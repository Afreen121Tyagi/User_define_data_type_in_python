import math
from fraction_data_type import FractionDataType


def test_fraction_initialization():
    """Test Fraction creation."""
    f = FractionDataType(3, 4)
    assert f.num == 3
    assert f.den == 4
    
    # Default denominator
    f2 = FractionDataType(5)
    assert f2.num == 5
    assert f2.den == 1
    
    print("✓ Fraction initialization")


def test_fraction_gcd_reduction():
    """Test automatic GCD reduction."""
    f = FractionDataType(6, 8)
    assert f.num == 3
    assert f.den == 4
    
    f2 = FractionDataType(10, 5)
    assert f2.num == 2
    assert f2.den == 1
    
    f3 = FractionDataType(0, 5)
    assert f3.num == 0
    assert f3.den == 1
    
    print("✓ Fraction GCD reduction")


def test_fraction_negative_handling():
    """Test negative sign normalization."""
    f1 = FractionDataType(-3, 4)
    assert f1.num == -3
    assert f1.den == 4
    
    f2 = FractionDataType(3, -4)
    assert f2.num == -3
    assert f2.den == 4
    
    f3 = FractionDataType(-3, -4)
    assert f3.num == 3
    assert f3.den == 4
    
    print("✓ Fraction negative handling")


def test_fraction_zero_denominator():
    """Test division by zero check."""
    try:
        FractionDataType(1, 0)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert "zero" in str(e).lower()
    
    print("✓ Fraction zero denominator check")


def test_fraction_representation():
    """Test string representations."""
    f1 = FractionDataType(3, 4)
    assert str(f1) == "3/4"
    assert "3" in repr(f1) and "4" in repr(f1)
    
    # Integer representation
    f2 = FractionDataType(6, 1)
    assert str(f2) == "6"
    
    print("✓ Fraction representation")


def test_fraction_addition():
    """Test fraction addition."""
    f1 = FractionDataType(1, 2)
    f2 = FractionDataType(1, 3)
    
    result = f1 + f2
    assert result == FractionDataType(5, 6)
    
    # With integer
    result2 = f1 + 1
    assert result2 == FractionDataType(3, 2)
    
    # Commutative with int
    result3 = 1 + f1
    assert result3 == FractionDataType(3, 2)
    
    print("✓ Fraction addition")


def test_fraction_subtraction():
    """Test fraction subtraction."""
    f1 = FractionDataType(3, 4)
    f2 = FractionDataType(1, 4)
    
    result = f1 - f2
    assert result == FractionDataType(1, 2)
    
    # With integer
    result2 = f1 - 1
    assert result2 == FractionDataType(-1, 4)
    
    # Right subtraction
    result3 = 2 - f1
    assert result3 == FractionDataType(5, 4)
    
    print("✓ Fraction subtraction")


def test_fraction_multiplication():
    """Test fraction multiplication."""
    f1 = FractionDataType(2, 3)
    f2 = FractionDataType(3, 4)
    
    result = f1 * f2
    assert result == FractionDataType(1, 2)
    
    # With integer
    result2 = f1 * 3
    assert result2 == FractionDataType(2, 1)
    
    # Right multiplication
    result3 = 2 * f1
    assert result3 == FractionDataType(4, 3)
    
    print("✓ Fraction multiplication")


def test_fraction_division():
    """Test fraction division."""
    f1 = FractionDataType(1, 2)
    f2 = FractionDataType(2, 3)
    
    result = f1 / f2
    assert result == FractionDataType(3, 4)
    
    # With integer
    result2 = f1 / 2
    assert result2 == FractionDataType(1, 4)
    
    # Right division
    result3 = 2 / FractionDataType(1, 2)
    assert result3 == FractionDataType(4, 1)
    
    # Division by zero
    try:
        f1 / FractionDataType(0, 1)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    
    print("✓ Fraction division")


def test_fraction_floor_division():
    """Test floor division."""
    f1 = FractionDataType(7, 2)
    f2 = FractionDataType(3, 2)
    
    result = f1 // f2
    assert result == 2  # (7/2) / (3/2) = 7/3 = 2.33.. => floor = 2
    
    # With integer
    result2 = f1 // 2
    assert result2 == 1  # (7/2) / 2 = 7/4 = 1.75 => floor = 1
    
    print("✓ Fraction floor division")


def test_fraction_modulo():
    """Test modulo operation."""
    f1 = FractionDataType(7, 2)
    f2 = FractionDataType(3, 2)
    
    result = f1 % f2
    # 7/2 = 3 * (3/2) + 1/2, so remainder is 1/2
    assert result == FractionDataType(1, 2)
    
    print("✓ Fraction modulo")


def test_fraction_power():
    """Test power operation."""
    f = FractionDataType(2, 3)
    
    # Positive exponent
    result = f ** 2
    assert result == FractionDataType(4, 9)
    
    result2 = f ** 3
    assert result2 == FractionDataType(8, 27)
    
    # Negative exponent (reciprocal power)
    result3 = f ** -1
    assert result3 == FractionDataType(3, 2)
    
    result4 = f ** -2
    assert result4 == FractionDataType(9, 4)
    
    # Zero exponent
    result5 = f ** 0
    assert result5 == FractionDataType(1, 1)
    
    print("✓ Fraction power")


def test_fraction_unary_operators():
    """Test unary operators: negation, positive, absolute."""
    f = FractionDataType(3, 4)
    
    # Negation
    neg = -f
    assert neg == FractionDataType(-3, 4)
    
    # Positive
    pos = +f
    assert pos == f
    
    # Absolute value
    abs_neg = abs(FractionDataType(-3, 4))
    assert abs_neg == FractionDataType(3, 4)
    
    print("✓ Fraction unary operators")


def test_fraction_equality():
    """Test equality comparison."""
    f1 = FractionDataType(3, 4)
    f2 = FractionDataType(6, 8)
    f3 = FractionDataType(1, 2)
    
    assert f1 == f2  # Equal (both reduce to 3/4)
    assert not (f1 == f3)
    assert f1 != f3
    
    # With integers
    f4 = FractionDataType(4, 1)
    assert f4 == 4
    assert 4 == f4
    
    print("✓ Fraction equality")


def test_fraction_less_than():
    """Test less than comparison."""
    f1 = FractionDataType(1, 3)
    f2 = FractionDataType(1, 2)
    
    assert f1 < f2
    assert not (f2 < f1)
    assert not (f1 < f1)
    
    # With integers
    assert f1 < 1
    assert not (f2 < 0)
    
    print("✓ Fraction less than")


def test_fraction_comparisons():
    """Test all comparison operators."""
    f1 = FractionDataType(1, 2)
    f2 = FractionDataType(3, 4)
    
    # Less than or equal
    assert f1 <= f2
    assert f1 <= f1
    assert not (f2 <= f1)
    
    # Greater than
    assert f2 > f1
    assert not (f1 > f2)
    
    # Greater than or equal
    assert f2 >= f1
    assert f1 >= f1
    
    print("✓ Fraction comparisons (<=, >, >=)")


def test_fraction_float_conversion():
    """Test conversion to float."""
    f = FractionDataType(3, 4)
    assert float(f) == 0.75
    
    f2 = FractionDataType(1, 3)
    assert abs(float(f2) - 0.333333) < 0.0001
    
    f3 = FractionDataType(-5, 2)
    assert float(f3) == -2.5
    
    print("✓ Fraction to float conversion")


def test_fraction_int_conversion():
    """Test conversion to int (floor division)."""
    f1 = FractionDataType(7, 3)
    assert int(f1) == 2  # 7/3 = 2.33.. => 2
    
    f2 = FractionDataType(-7, 3)
    assert int(f2) == -3  # -7/3 = -2.33.. => -3 (floor division)
    
    f3 = FractionDataType(8, 2)
    assert int(f3) == 4
    
    print("✓ Fraction to int conversion")


def test_fraction_hash():
    """Test hash function for use in sets/dicts."""
    f1 = FractionDataType(3, 4)
    f2 = FractionDataType(6, 8)  # Same as f1 when reduced
    f3 = FractionDataType(1, 2)
    
    # Same fractions should have same hash
    assert hash(f1) == hash(f2)
    
    # Can use in sets
    s = {f1, f2, f3}
    assert len(s) == 2  # f1 and f2 are same
    
    # Can use as dict keys
    d = {f1: "three-fourths", f3: "one-half"}
    assert d[f2] == "three-fourths"  # f2 and f1 are same key
    
    print("✓ Fraction hash")


def test_fraction_simplify():
    """Test simplify method."""
    f = FractionDataType(12, 16)
    simplified = f.simplify()
    assert simplified == FractionDataType(3, 4)
    
    print("✓ Fraction simplify")


def test_fraction_reciprocal():
    """Test reciprocal."""
    f = FractionDataType(3, 4)
    recip = f.reciprocal()
    assert recip == FractionDataType(4, 3)
    
    # Product should be 1
    result = f * recip
    assert result == FractionDataType(1, 1)
    
    # Reciprocal of zero raises error
    try:
        FractionDataType(0, 1).reciprocal()
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    
    print("✓ Fraction reciprocal")


def test_fraction_as_mixed_number():
    """Test mixed number representation."""
    f = FractionDataType(7, 3)
    whole, num, den = f.as_mixed_number()
    assert whole == 2
    assert num == 1
    assert den == 3
    # Represents 2 1/3
    
    # Proper fraction
    f2 = FractionDataType(3, 4)
    whole2, num2, den2 = f2.as_mixed_number()
    assert whole2 == 0
    assert num2 == 3
    assert den2 == 4
    
    # Negative
    f3 = FractionDataType(-7, 3)
    whole3, num3, den3 = f3.as_mixed_number()
    assert whole3 == -3  # -7//3 = -3, remainder = abs(-7) % 3 = 1
    assert num3 == 1
    assert den3 == 3
    
    print("✓ Fraction as mixed number")


def test_fraction_is_proper():
    """Test proper fraction check."""
    f1 = FractionDataType(3, 4)
    assert f1.is_proper()
    
    f2 = FractionDataType(7, 3)
    assert not f2.is_proper()
    
    f3 = FractionDataType(-3, 4)
    assert f3.is_proper()
    
    f4 = FractionDataType(4, 4)
    assert not f4.is_proper()
    
    print("✓ Fraction is proper")


def test_fraction_is_improper():
    """Test improper fraction check."""
    f1 = FractionDataType(7, 3)
    assert f1.is_improper()
    
    f2 = FractionDataType(3, 4)
    assert not f2.is_improper()
    
    f3 = FractionDataType(4, 4)
    assert f3.is_improper()
    
    f4 = FractionDataType(-7, 3)
    assert f4.is_improper()
    
    print("✓ Fraction is improper")


def test_fraction_from_float():
    """Test creating fraction from float."""
    f = FractionDataType.from_float(0.75)
    assert f == FractionDataType(3, 4)
    
    f2 = FractionDataType.from_float(0.5)
    assert f2 == FractionDataType(1, 2)
    
    f3 = FractionDataType.from_float(0.333333, max_denominator=100)
    # Should be close to 1/3
    assert abs(float(f3) - 1/3) < 0.01
    
    print("✓ Fraction from float")


def test_fraction_from_mixed():
    """Test creating fraction from mixed number."""
    f = FractionDataType.from_mixed(2, 1, 3)
    assert f == FractionDataType(7, 3)
    
    f2 = FractionDataType.from_mixed(1, 1, 2)
    assert f2 == FractionDataType(3, 2)
    
    f3 = FractionDataType.from_mixed(0, 3, 4)
    assert f3 == FractionDataType(3, 4)
    
    print("✓ Fraction from mixed")


def test_fraction_mixed_arithmetic():
    """Test arithmetic mixing fractions and integers."""
    f = FractionDataType(1, 2)
    
    # All combinations
    assert f + 2 == FractionDataType(5, 2)
    assert 2 + f == FractionDataType(5, 2)
    
    assert f - 1 == FractionDataType(-1, 2)
    assert 1 - f == FractionDataType(1, 2)
    
    assert f * 3 == FractionDataType(3, 2)
    assert 3 * f == FractionDataType(3, 2)
    
    assert f / 2 == FractionDataType(1, 4)
    assert 2 / f == FractionDataType(4, 1)
    
    print("✓ Fraction mixed arithmetic")


def test_fraction_chained_operations():
    """Test chained operations."""
    f1 = FractionDataType(1, 2)
    f2 = FractionDataType(1, 3)
    f3 = FractionDataType(1, 4)
    
    result = f1 + f2 - f3
    # 1/2 + 1/3 - 1/4 = 6/12 + 4/12 - 3/12 = 7/12
    assert result == FractionDataType(7, 12)
    
    result2 = f1 * f2 / f3
    # (1/2) * (1/3) / (1/4) = (1/6) / (1/4) = 4/6 = 2/3
    assert result2 == FractionDataType(2, 3)
    
    result3 = (f1 + f2) * f3
    # (1/2 + 1/3) * 1/4 = (5/6) * 1/4 = 5/24
    assert result3 == FractionDataType(5, 24)
    
    print("✓ Fraction chained operations")


def test_fraction_edge_cases():
    """Test edge cases."""
    # Zero numerator
    f0 = FractionDataType(0, 5)
    assert f0.num == 0
    assert f0.den == 1
    assert f0 == 0
    assert float(f0) == 0
    
    # One
    f1 = FractionDataType(5, 5)
    assert f1 == 1
    
    # Large numbers
    f_large = FractionDataType(1000000, 2000000)
    assert f_large == FractionDataType(1, 2)
    
    print("✓ Fraction edge cases")


def test_fraction_comparison_with_zero():
    """Test comparisons with zero."""
    f_pos = FractionDataType(1, 2)
    f_neg = FractionDataType(-1, 2)
    f_zero = FractionDataType(0, 1)
    
    assert f_pos > f_zero
    assert f_zero > f_neg
    assert f_pos > f_neg
    
    assert f_zero >= 0
    assert f_zero <= 0
    assert f_zero == 0
    
    print("✓ Fraction comparison with zero")


def test_fraction_negative_operations():
    """Test operations with negative fractions."""
    f_pos = FractionDataType(3, 4)
    f_neg = FractionDataType(-3, 4)
    
    # Addition
    assert f_pos + f_neg == 0
    
    # Multiplication
    assert f_pos * f_neg == FractionDataType(-9, 16)
    
    # Double negation
    assert -(-f_neg) == f_neg
    
    print("✓ Fraction negative operations")


if __name__ == "__main__":
    print("Running Fraction Data Type Tests...\n")
    
    # Basic tests
    test_fraction_initialization()
    test_fraction_gcd_reduction()
    test_fraction_negative_handling()
    test_fraction_zero_denominator()
    test_fraction_representation()
    
    # Arithmetic operations
    test_fraction_addition()
    test_fraction_subtraction()
    test_fraction_multiplication()
    test_fraction_division()
    test_fraction_floor_division()
    test_fraction_modulo()
    test_fraction_power()
    test_fraction_unary_operators()
    
    # Comparisons
    test_fraction_equality()
    test_fraction_less_than()
    test_fraction_comparisons()
    
    # Conversions
    test_fraction_float_conversion()
    test_fraction_int_conversion()
    test_fraction_hash()
    
    # Utility methods
    test_fraction_simplify()
    test_fraction_reciprocal()
    test_fraction_as_mixed_number()
    test_fraction_is_proper()
    test_fraction_is_improper()
    test_fraction_from_float()
    test_fraction_from_mixed()
    
    # Complex tests
    test_fraction_mixed_arithmetic()
    test_fraction_chained_operations()
    test_fraction_edge_cases()
    test_fraction_comparison_with_zero()
    test_fraction_negative_operations()
    
    print("\n✅ All tests passed!")
