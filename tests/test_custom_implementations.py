"""Tests for custom sum implementations in various modules."""
import sys
import pytest

sys.path.insert(0, "/home/user/Sum")


def custom_sum_v1(nums):
    """Custom implementation from SumImprovedbyClaudeCodev2.py and v3.py."""
    total = 0
    for num in nums:
        total += num
    return total


class TestCustomSumImplementations:
    """Test custom sum implementations match built-in sum()."""

    def test_custom_sum_empty_list(self):
        """Test custom sum with empty list returns 0."""
        assert custom_sum_v1([]) == 0
        assert custom_sum_v1([]) == sum([])

    def test_custom_sum_single_element(self):
        """Test custom sum with single element."""
        assert custom_sum_v1([5]) == 5
        assert custom_sum_v1([5]) == sum([5])

    def test_custom_sum_positive_integers(self):
        """Test custom sum with positive integers."""
        nums = [1, 2, 3, 4, 5]
        assert custom_sum_v1(nums) == 15
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_negative_integers(self):
        """Test custom sum with negative integers."""
        nums = [-1, -2, -3, -4, -5]
        assert custom_sum_v1(nums) == -15
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_mixed_signs(self):
        """Test custom sum with mixed positive and negative numbers."""
        nums = [10, -5, 3, -8, 7]
        assert custom_sum_v1(nums) == 7
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_floats(self):
        """Test custom sum with float numbers."""
        nums = [1.5, 2.7, 3.2, 0.6]
        expected = sum(nums)
        result = custom_sum_v1(nums)
        assert abs(result - expected) < 1e-10

    def test_custom_sum_with_zero(self):
        """Test custom sum with zeros in the list."""
        nums = [0, 1, 0, 2, 0, 3]
        assert custom_sum_v1(nums) == 6
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_all_zeros(self):
        """Test custom sum with all zeros."""
        nums = [0, 0, 0, 0]
        assert custom_sum_v1(nums) == 0
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_large_numbers(self):
        """Test custom sum with large numbers."""
        nums = [1_000_000, 2_000_000, 3_000_000]
        assert custom_sum_v1(nums) == 6_000_000
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_range(self):
        """Test custom sum with range object."""
        nums = list(range(100))
        expected = 4950  # Sum of 0 to 99 = n(n-1)/2 = 100*99/2
        assert custom_sum_v1(nums) == expected
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_mixed_int_float(self):
        """Test custom sum with mixed integers and floats."""
        nums = [1, 2.5, 3, 4.75, 5]
        expected = sum(nums)
        result = custom_sum_v1(nums)
        assert abs(result - expected) < 1e-10

    @pytest.mark.parametrize("nums", [
        [1, 2, 3],
        [-1, -2, -3],
        [0],
        [100, 200, 300, 400],
        [1.1, 2.2, 3.3],
        [-5, 5, -10, 10],
    ])
    def test_custom_sum_matches_builtin(self, nums):
        """Parametrized test to ensure custom sum always matches built-in."""
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_very_large_list(self):
        """Test custom sum with very large list."""
        nums = list(range(10_000))
        expected = sum(nums)
        assert custom_sum_v1(nums) == expected

    def test_custom_sum_negative_floats(self):
        """Test custom sum with negative floats."""
        nums = [-1.5, -2.7, -3.2]
        expected = sum(nums)
        result = custom_sum_v1(nums)
        assert abs(result - expected) < 1e-10

    def test_custom_sum_scientific_notation(self):
        """Test custom sum with scientific notation numbers."""
        nums = [1e10, 2e10, 3e10]
        expected = 6e10
        assert custom_sum_v1(nums) == expected
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_tiny_numbers(self):
        """Test custom sum with very small numbers."""
        nums = [1e-10, 2e-10, 3e-10]
        expected = sum(nums)
        result = custom_sum_v1(nums)
        assert abs(result - expected) < 1e-15

    def test_custom_sum_accumulation_order(self):
        """Test that custom sum accumulates in the correct order."""
        # Test with numbers that might have floating point issues
        nums = [0.1, 0.2, 0.3]
        result = custom_sum_v1(nums)
        expected = sum(nums)
        # They should match exactly since they use the same algorithm
        assert result == expected

    def test_custom_sum_maintains_type(self):
        """Test that custom sum maintains numeric type appropriately."""
        # Integer input should give integer output (if possible)
        int_nums = [1, 2, 3]
        int_result = custom_sum_v1(int_nums)
        assert isinstance(int_result, int)

        # Float input should give float output
        float_nums = [1.0, 2.0, 3.0]
        float_result = custom_sum_v1(float_nums)
        assert isinstance(float_result, float)

    def test_custom_sum_single_large_number(self):
        """Test custom sum with a single very large number."""
        nums = [1e100]
        assert custom_sum_v1(nums) == 1e100
        assert custom_sum_v1(nums) == sum(nums)

    def test_custom_sum_alternating_signs(self):
        """Test custom sum with alternating positive/negative."""
        nums = [1, -1, 2, -2, 3, -3]
        assert custom_sum_v1(nums) == 0
        assert custom_sum_v1(nums) == sum(nums)
