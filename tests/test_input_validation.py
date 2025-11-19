"""Tests for input validation functions."""
import sys
from unittest.mock import patch
import pytest

# Add parent directory to path for imports
sys.path.insert(0, "/home/user/Sum")

from demos.summing_methods import parse_numbers


class TestParseNumbers:
    """Test the parse_numbers function from demos.summing_methods."""

    def test_parse_single_integer(self):
        """Test parsing a single integer."""
        with patch('builtins.input', return_value='42'):
            result = parse_numbers("Enter: ", allow_float=False)
            assert result == [42.0]

    def test_parse_multiple_integers(self):
        """Test parsing multiple space-separated integers."""
        with patch('builtins.input', return_value='10 20 30'):
            result = parse_numbers("Enter: ", allow_float=False)
            assert result == [10.0, 20.0, 30.0]

    def test_parse_single_float(self):
        """Test parsing a single float."""
        with patch('builtins.input', return_value='3.14'):
            result = parse_numbers("Enter: ", allow_float=True)
            assert result == [3.14]

    def test_parse_multiple_floats(self):
        """Test parsing multiple floats."""
        with patch('builtins.input', return_value='1.5 2.7 3.9'):
            result = parse_numbers("Enter: ", allow_float=True)
            assert result == [1.5, 2.7, 3.9]

    def test_parse_negative_numbers(self):
        """Test parsing negative numbers."""
        with patch('builtins.input', return_value='-5 -10 15'):
            result = parse_numbers("Enter: ", allow_float=False)
            assert result == [-5.0, -10.0, 15.0]

    def test_parse_mixed_positive_negative_floats(self):
        """Test parsing mixed positive and negative floats."""
        with patch('builtins.input', return_value='-3.5 4.25 0 -1.75'):
            result = parse_numbers("Enter: ", allow_float=True)
            assert result == [-3.5, 4.25, 0.0, -1.75]

    def test_parse_zero(self):
        """Test parsing zero."""
        with patch('builtins.input', return_value='0'):
            result = parse_numbers("Enter: ", allow_float=False)
            assert result == [0.0]

    def test_parse_large_numbers(self):
        """Test parsing large numbers."""
        with patch('builtins.input', return_value='1000000 2000000'):
            result = parse_numbers("Enter: ", allow_float=False)
            assert result == [1000000.0, 2000000.0]

    def test_parse_scientific_notation(self):
        """Test parsing scientific notation (only with allow_float=True)."""
        with patch('builtins.input', return_value='1e10 3.5e-2'):
            result = parse_numbers("Enter: ", allow_float=True)
            assert result == [1e10, 3.5e-2]

    def test_reject_float_when_not_allowed(self):
        """Test that floats are rejected when allow_float=False."""
        # First attempt with float (invalid), then valid input
        with patch('builtins.input', side_effect=['3.14', '3']):
            with patch('builtins.print') as mock_print:
                result = parse_numbers("Enter: ", allow_float=False)
                assert result == [3.0]
                # Verify error message was printed
                mock_print.assert_called()

    def test_retry_on_invalid_input(self):
        """Test retry behavior on invalid input."""
        # First attempt invalid, second attempt valid
        with patch('builtins.input', side_effect=['abc', '42']):
            with patch('builtins.print') as mock_print:
                result = parse_numbers("Enter: ", allow_float=False)
                assert result == [42.0]
                # Verify error message was printed
                mock_print.assert_called()

    def test_retry_on_empty_input(self):
        """Test retry behavior on empty input."""
        with patch('builtins.input', side_effect=['', '10 20']):
            with patch('builtins.print') as mock_print:
                result = parse_numbers("Enter: ", allow_float=False)
                assert result == [10.0, 20.0]
                # Verify prompt was shown
                mock_print.assert_called()

    def test_reject_nan_in_integer_mode(self):
        """Test that 'nan' is rejected in integer mode."""
        with patch('builtins.input', side_effect=['nan', '42']):
            with patch('builtins.print') as mock_print:
                result = parse_numbers("Enter: ", allow_float=False)
                assert result == [42.0]
                mock_print.assert_called()

    def test_reject_inf_in_integer_mode(self):
        """Test that 'inf' is rejected in integer mode."""
        with patch('builtins.input', side_effect=['inf', '42']):
            with patch('builtins.print') as mock_print:
                result = parse_numbers("Enter: ", allow_float=False)
                assert result == [42.0]
                mock_print.assert_called()

    def test_accept_inf_in_float_mode(self):
        """Test that 'inf' is accepted in float mode."""
        with patch('builtins.input', return_value='inf'):
            result = parse_numbers("Enter: ", allow_float=True)
            assert result[0] == float('inf')

    def test_whitespace_handling(self):
        """Test handling of extra whitespace."""
        with patch('builtins.input', return_value='  10   20  30  '):
            result = parse_numbers("Enter: ", allow_float=False)
            assert result == [10.0, 20.0, 30.0]

    def test_leading_zeros(self):
        """Test handling of leading zeros."""
        with patch('builtins.input', return_value='007 0123'):
            result = parse_numbers("Enter: ", allow_float=False)
            assert result == [7.0, 123.0]

    def test_negative_zero(self):
        """Test parsing negative zero."""
        with patch('builtins.input', return_value='-0'):
            result = parse_numbers("Enter: ", allow_float=True)
            assert result == [-0.0]


# Tests for get_number function from other modules would go here
# Note: get_number is defined in multiple files with slight variations
# We'll test the pattern in the integration tests
