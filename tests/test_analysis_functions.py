"""Direct tests for the v3 sign-breakdown helper."""

import pytest

from history.claude_v3_menu_demo import analyze_numbers


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        (
            [10, -5, 0, 3, -8, 0],
            {
                "total": 0,
                "positive": [10, 3],
                "negative": [-5, -8],
                "zeros": [0, 0],
                "positive_sum": 13,
                "negative_sum": -13,
                "positive_count": 2,
                "negative_count": 2,
                "zero_count": 2,
            },
        ),
        (
            [],
            {
                "total": 0,
                "positive": [],
                "negative": [],
                "zeros": [],
                "positive_sum": 0,
                "negative_sum": 0,
                "positive_count": 0,
                "negative_count": 0,
                "zero_count": 0,
            },
        ),
    ],
)
def test_analyze_numbers_uses_v3_source(numbers, expected):
    assert analyze_numbers(numbers) == expected
