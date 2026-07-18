# Sum

An educational Python repository demonstrating various approaches to summing numbers, showcasing iterative improvement patterns across multiple implementations contributed by different AI assistants and developers.

## Files

| File | Description |
|---|---|
| `Sum.py` | Original basic implementation |
| `SumImprovedbyClaudeCode.py` | v1: Input validation and error handling |
| `SumImprovedbyClaudeCodev2.py` | v2: Float support and multiple number summation |
| `SumImprovedbyClaudeCodev3.py` | v3: Interactive menu system with analysis (most complete) |
| `SumImprovedbyChatGPT.py` | Type-annotated implementation using `demos.summing_methods` |
| `SumImprovedbyChatGPTv2.py` | Test-driven variant with pytest integration |
| `demos/summing_methods.py` | Shared module with canonical summation implementations |

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

The repository includes a pytest suite covering core summation behavior, input validation, edge cases, and integration paths. Current test totals and coverage are not claimed until the project has a declared toolchain and CI-generated results.

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v
```

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
