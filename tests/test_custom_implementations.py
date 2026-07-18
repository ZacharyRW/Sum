"""Direct tests for the extracted Claude custom-sum helpers."""

import pytest

from SumImprovedbyClaudeCodev2 import custom_sum as custom_sum_v2
from SumImprovedbyClaudeCodev3 import custom_sum as custom_sum_v3


@pytest.mark.parametrize("numbers", [[], [5], [1, 2, 3], [-5, 2, 3], [1.5, 2.5]])
@pytest.mark.parametrize("custom_sum", [custom_sum_v2, custom_sum_v3])
def test_custom_sum_uses_source_implementations(custom_sum, numbers):
    assert custom_sum(numbers) == sum(numbers)
