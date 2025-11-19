"""Shared pytest fixtures and configuration for Sum repository tests."""
import sys
import pytest

# Add parent directory to path for imports
sys.path.insert(0, "/home/user/Sum")


# ==================== Number Fixtures ====================

@pytest.fixture
def small_positive_integers():
    """Small positive integers for testing."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def small_negative_integers():
    """Small negative integers for testing."""
    return [-1, -2, -3, -4, -5]


@pytest.fixture
def mixed_integers():
    """Mixed positive and negative integers."""
    return [10, -5, 3, -8, 7, -2, 15]


@pytest.fixture
def small_floats():
    """Small floating point numbers."""
    return [1.5, 2.7, 3.2, 0.6]


@pytest.fixture
def mixed_floats():
    """Mixed positive and negative floats."""
    return [3.5, -2.7, 1.2, -0.8, 4.1]


@pytest.fixture
def numbers_with_zeros():
    """Numbers including zeros."""
    return [5, 0, -3, 0, 2, 0, -1]


@pytest.fixture
def large_integers():
    """Large integer values."""
    return [1_000_000, 2_000_000, 3_000_000, 500_000]


@pytest.fixture
def very_large_list():
    """Very large list for performance testing."""
    return list(range(10_000))


@pytest.fixture
def empty_list():
    """Empty list."""
    return []


@pytest.fixture
def single_element():
    """Single element list."""
    return [42]


# ==================== Expected Results Fixtures ====================

@pytest.fixture
def small_positive_sum():
    """Expected sum of small positive integers."""
    return 15  # 1+2+3+4+5


@pytest.fixture
def small_negative_sum():
    """Expected sum of small negative integers."""
    return -15  # -1-2-3-4-5


@pytest.fixture
def mixed_integers_sum():
    """Expected sum of mixed integers."""
    return 20  # 10-5+3-8+7-2+15


# ==================== Special Values Fixtures ====================

@pytest.fixture
def infinity_values():
    """Lists containing infinity."""
    return {
        'positive_inf': [float('inf'), 1, 2],
        'negative_inf': [float('-inf'), 1, 2],
        'both_inf': [float('inf'), float('-inf')],
    }


@pytest.fixture
def nan_values():
    """Lists containing NaN."""
    return [1, 2, float('nan'), 3, 4]


@pytest.fixture
def tiny_floats():
    """Very small floating point numbers."""
    return [1e-10, 2e-10, 3e-10]


@pytest.fixture
def huge_floats():
    """Very large floating point numbers."""
    return [1e100, 2e100, 3e100]


# ==================== Test Case Data Fixtures ====================

@pytest.fixture
def two_number_test_cases():
    """Test cases for two-number addition."""
    return [
        (0, 0, 0),
        (1, 2, 3),
        (5, 10, 15),
        (-5, 7, 2),
        (-5, -10, -15),
        (3.5, 4.25, 7.75),
        (1_000_000, 2_000_000, 3_000_000),
    ]


@pytest.fixture
def n_number_test_cases():
    """Test cases for n-number summation."""
    return [
        ([], 0),
        ([0], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5], 15),
        ([-1, -2, -3, -4, -5], -15),
        ([10, -5, 3, -8], 0),
        ([3.5, 4.25, -1.75], 6.0),
    ]


# ==================== Function Fixtures ====================

@pytest.fixture
def sum_functions():
    """Import and return all sum functions."""
    from demos.summing_methods import sum_builtin, sum_reduce, sum_fsum
    return {
        'builtin': sum_builtin,
        'reduce': sum_reduce,
        'fsum': sum_fsum,
    }


@pytest.fixture
def two_number_functions():
    """Import and return all two-number addition functions."""
    from demos.summing_methods import add_plus, add_sum, add_operator
    return {
        'plus': add_plus,
        'sum': add_sum,
        'operator': add_operator,
    }


# ==================== Mock Data Fixtures ====================

@pytest.fixture
def mock_user_inputs():
    """Mock user input sequences for testing."""
    return {
        'valid_integers': '10 20 30',
        'valid_floats': '1.5 2.5 3.5',
        'invalid_then_valid': ['abc', '10 20'],
        'empty_then_valid': ['', '5 10'],
        'mixed_signs': '-5 10 -3 7',
    }


# ==================== Parametrize Helpers ====================

@pytest.fixture
def edge_case_numbers():
    """Edge case numbers for comprehensive testing."""
    return [
        0,
        -0.0,
        1,
        -1,
        sys.maxsize,
        -sys.maxsize,
        1e308,  # Near max float
        1e-308,  # Near min positive float
        float('inf'),
        float('-inf'),
        float('nan'),
    ]


# ==================== Precision Testing Fixtures ====================

@pytest.fixture
def precision_test_case():
    """Numbers that test floating point precision."""
    return {
        'simple': [0.1, 0.2, 0.3],
        'repeated': [0.1] * 100,
        'catastrophic': [1e16, 1.0, -1e16],
        'tiny_accumulation': [1e-16] * 1000,
    }


# ==================== Real-World Scenario Fixtures ====================

@pytest.fixture
def shopping_cart_prices():
    """Simulated shopping cart prices."""
    return [19.99, 29.99, 9.99, 14.99, 39.99]


@pytest.fixture
def temperature_readings():
    """Simulated temperature readings."""
    return [72.5, 73.1, 71.9, 72.3, 73.5, 72.8, 73.0]


@pytest.fixture
def account_transactions():
    """Simulated account transactions (positive=credit, negative=debit)."""
    return [100.0, -25.50, -10.00, 50.00, -15.75, 200.00]


@pytest.fixture
def test_scores():
    """Simulated test scores."""
    return [85, 90, 78, 92, 88, 95, 82, 91]


# ==================== Pytest Configuration ====================

def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "performance: marks tests as performance tests"
    )
    config.addinivalue_line(
        "markers", "edge_case: marks tests for edge cases"
    )


# ==================== Utility Functions ====================

@pytest.fixture
def assert_close():
    """Helper to assert floating point values are close."""
    def _assert_close(actual, expected, tolerance=1e-10):
        assert abs(actual - expected) < tolerance, \
            f"Expected {expected}, got {actual} (diff: {abs(actual - expected)})"
    return _assert_close


@pytest.fixture
def assert_all_equal():
    """Helper to assert all values in a list are equal."""
    def _assert_all_equal(values):
        assert len(set(values)) == 1, \
            f"Not all values are equal: {values}"
    return _assert_all_equal
