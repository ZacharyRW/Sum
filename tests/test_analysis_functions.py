"""Tests for number analysis and breakdown functions."""
import sys
import pytest
from pathlib import Path

# Add repository root to path - conftest.py does this too, but this ensures
# the test can run standalone if needed
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))


def analyze_numbers(numbers):
    """
    Analyze a list of numbers and break them down into positive, negative, and zeros.
    Returns a dictionary with analysis results.

    This implements the logic from method_positive_negative_demo in SumImprovedbyClaudeCodev3.py
    """
    positive_nums = [n for n in numbers if n > 0]
    negative_nums = [n for n in numbers if n < 0]
    zero_nums = [n for n in numbers if n == 0]

    return {
        'total': sum(numbers),
        'positive': positive_nums,
        'negative': negative_nums,
        'zeros': zero_nums,
        'positive_sum': sum(positive_nums) if positive_nums else 0,
        'negative_sum': sum(negative_nums) if negative_nums else 0,
        'positive_count': len(positive_nums),
        'negative_count': len(negative_nums),
        'zero_count': len(zero_nums),
    }


class TestAnalyzeNumbers:
    """Test number analysis and breakdown functionality."""

    def test_all_positive_numbers(self):
        """Test analysis with all positive numbers."""
        nums = [1, 2, 3, 4, 5]
        result = analyze_numbers(nums)

        assert result['total'] == 15
        assert result['positive'] == [1, 2, 3, 4, 5]
        assert result['negative'] == []
        assert result['zeros'] == []
        assert result['positive_sum'] == 15
        assert result['negative_sum'] == 0
        assert result['positive_count'] == 5
        assert result['negative_count'] == 0
        assert result['zero_count'] == 0

    def test_all_negative_numbers(self):
        """Test analysis with all negative numbers."""
        nums = [-1, -2, -3, -4, -5]
        result = analyze_numbers(nums)

        assert result['total'] == -15
        assert result['positive'] == []
        assert result['negative'] == [-1, -2, -3, -4, -5]
        assert result['zeros'] == []
        assert result['positive_sum'] == 0
        assert result['negative_sum'] == -15
        assert result['positive_count'] == 0
        assert result['negative_count'] == 5
        assert result['zero_count'] == 0

    def test_mixed_positive_negative(self):
        """Test analysis with mixed positive and negative numbers."""
        nums = [10, -5, 3, -8, 7, -2]
        result = analyze_numbers(nums)

        assert result['total'] == 5
        assert result['positive'] == [10, 3, 7]
        assert result['negative'] == [-5, -8, -2]
        assert result['zeros'] == []
        assert result['positive_sum'] == 20
        assert result['negative_sum'] == -15
        assert result['positive_count'] == 3
        assert result['negative_count'] == 3
        assert result['zero_count'] == 0

    def test_with_zeros(self):
        """Test analysis with zeros included."""
        nums = [5, 0, -3, 0, 2, 0]
        result = analyze_numbers(nums)

        assert result['total'] == 4
        assert result['positive'] == [5, 2]
        assert result['negative'] == [-3]
        assert result['zeros'] == [0, 0, 0]
        assert result['positive_sum'] == 7
        assert result['negative_sum'] == -3
        assert result['positive_count'] == 2
        assert result['negative_count'] == 1
        assert result['zero_count'] == 3

    def test_all_zeros(self):
        """Test analysis with all zeros."""
        nums = [0, 0, 0, 0]
        result = analyze_numbers(nums)

        assert result['total'] == 0
        assert result['positive'] == []
        assert result['negative'] == []
        assert result['zeros'] == [0, 0, 0, 0]
        assert result['positive_sum'] == 0
        assert result['negative_sum'] == 0
        assert result['positive_count'] == 0
        assert result['negative_count'] == 0
        assert result['zero_count'] == 4

    def test_single_positive(self):
        """Test analysis with a single positive number."""
        nums = [42]
        result = analyze_numbers(nums)

        assert result['total'] == 42
        assert result['positive'] == [42]
        assert result['negative'] == []
        assert result['zeros'] == []
        assert result['positive_count'] == 1
        assert result['negative_count'] == 0
        assert result['zero_count'] == 0

    def test_single_negative(self):
        """Test analysis with a single negative number."""
        nums = [-42]
        result = analyze_numbers(nums)

        assert result['total'] == -42
        assert result['positive'] == []
        assert result['negative'] == [-42]
        assert result['zeros'] == []
        assert result['positive_count'] == 0
        assert result['negative_count'] == 1
        assert result['zero_count'] == 0

    def test_single_zero(self):
        """Test analysis with a single zero."""
        nums = [0]
        result = analyze_numbers(nums)

        assert result['total'] == 0
        assert result['positive'] == []
        assert result['negative'] == []
        assert result['zeros'] == [0]
        assert result['zero_count'] == 1

    def test_empty_list(self):
        """Test analysis with empty list."""
        nums = []
        result = analyze_numbers(nums)

        assert result['total'] == 0
        assert result['positive'] == []
        assert result['negative'] == []
        assert result['zeros'] == []
        assert result['positive_sum'] == 0
        assert result['negative_sum'] == 0
        assert result['positive_count'] == 0
        assert result['negative_count'] == 0
        assert result['zero_count'] == 0

    def test_floats_positive_negative(self):
        """Test analysis with floating point numbers."""
        nums = [3.5, -2.7, 1.2, -0.8, 0.0]
        result = analyze_numbers(nums)

        assert abs(result['total'] - 1.2) < 1e-10
        assert result['positive'] == [3.5, 1.2]
        assert result['negative'] == [-2.7, -0.8]
        assert result['zeros'] == [0.0]
        assert abs(result['positive_sum'] - 4.7) < 1e-10
        assert abs(result['negative_sum'] - (-3.5)) < 1e-10
        assert result['positive_count'] == 2
        assert result['negative_count'] == 2
        assert result['zero_count'] == 1

    def test_large_numbers(self):
        """Test analysis with large numbers."""
        nums = [1_000_000, -500_000, 250_000, -750_000]
        result = analyze_numbers(nums)

        assert result['total'] == 0
        assert result['positive'] == [1_000_000, 250_000]
        assert result['negative'] == [-500_000, -750_000]
        assert result['positive_sum'] == 1_250_000
        assert result['negative_sum'] == -1_250_000

    def test_balanced_positive_negative(self):
        """Test when positive and negative sums cancel out."""
        nums = [5, -5, 10, -10, 3, -3]
        result = analyze_numbers(nums)

        assert result['total'] == 0
        assert result['positive_sum'] == 18
        assert result['negative_sum'] == -18

    def test_mostly_positive(self):
        """Test with mostly positive numbers."""
        nums = [100, 50, 25, 10, -5]
        result = analyze_numbers(nums)

        assert result['total'] == 180
        assert result['positive_count'] == 4
        assert result['negative_count'] == 1
        assert result['positive_sum'] == 185
        assert result['negative_sum'] == -5

    def test_mostly_negative(self):
        """Test with mostly negative numbers."""
        nums = [-100, -50, -25, -10, 5]
        result = analyze_numbers(nums)

        assert result['total'] == -180
        assert result['positive_count'] == 1
        assert result['negative_count'] == 4
        assert result['positive_sum'] == 5
        assert result['negative_sum'] == -185

    @pytest.mark.parametrize("nums,expected_positive,expected_negative,expected_zero", [
        ([1, 2, 3], 3, 0, 0),
        ([-1, -2, -3], 0, 3, 0),
        ([0, 0, 0], 0, 0, 3),
        ([1, -1, 0], 1, 1, 1),
        ([5, -3, 0, 2, -1, 0], 2, 2, 2),
    ])
    def test_count_distribution(self, nums, expected_positive, expected_negative, expected_zero):
        """Parametrized test for count distribution."""
        result = analyze_numbers(nums)
        assert result['positive_count'] == expected_positive
        assert result['negative_count'] == expected_negative
        assert result['zero_count'] == expected_zero

    def test_negative_zero(self):
        """Test that negative zero is treated as zero."""
        nums = [-0.0, 0.0]
        result = analyze_numbers(nums)

        # Both should be treated as zero
        assert result['zero_count'] == 2
        assert result['positive_count'] == 0
        assert result['negative_count'] == 0

    def test_very_small_positive_negative(self):
        """Test with very small positive and negative numbers."""
        nums = [1e-10, -1e-10, 2e-10, -3e-10]
        result = analyze_numbers(nums)

        assert result['positive_count'] == 2
        assert result['negative_count'] == 2
        assert result['positive'] == [1e-10, 2e-10]
        assert result['negative'] == [-1e-10, -3e-10]
