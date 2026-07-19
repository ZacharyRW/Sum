# Sum

An educational Python summation tutorial. The maintained lesson is
`demos/summing_methods.py`; the other scripts are runnable historical
AI-assisted iterations retained for comparison and provenance.

## Files

| File | Description |
|---|---|
| `demos/summing_methods.py` | Canonical reusable summation lesson and interactive demo |
| `SumImprovedbyChatGPT.py` | Historical ChatGPT entry point that runs the canonical lesson |
| `Sum.py` | Historical original two-number CLI example |
| `SumImprovedbyClaudeCode.py` | Historical Claude v1 integer-input demonstration |
| `SumImprovedbyClaudeCodev2.py` | Historical Claude v2 float and multiple-number demonstration |
| `SumImprovedbyClaudeCodev3.py` | Historical Claude v3 menu and sign-analysis demonstration |
| `SumImprovedbyChatGPTv2.py` | Historical pytest snapshot; not part of the active test suite |

## Summation Methods Demonstrated

- Direct addition: `a + b`
- Built-in: `sum([a, b])`
- Manual loop accumulation
- Functional: `reduce(operator.add, nums, 0)`
- High precision: `math.fsum(nums)`

## Input Behavior

- Integer prompts accept whole numbers and preserve their exact Python `int`
  value, including values above `2**53`.
- Float prompts accept finite values only; `nan`, `inf`, and `-inf` are
  rejected.
- Closing standard input ends the current demo with a friendly message instead
  of a traceback.
- The count-based Claude v2/v3 examples accept from 1 to 100 values per run.

## Tests

The repository includes a pytest suite covering core summation behavior, input validation, edge cases, and integration paths. `tests/test_summation_methods.py` is the single active core arithmetic suite; `SumImprovedbyChatGPTv2.py` is retained only as a historical test snapshot. The project requires Python 3.9 or later. Current test totals and coverage are not claimed until CI-generated results are available.

```bash
# Install the declared development toolchain
python -m pip install -r requirements-dev.txt

# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run the configured linter
ruff check .
```

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
