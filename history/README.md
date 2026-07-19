# Historical Examples

This directory preserves the runnable AI-assisted and original examples that
led to the canonical tutorial in [`../demos/summing_methods.py`](../demos/summing_methods.py).
They are comparison artifacts, not competing maintained implementations.

Run an example from the repository root as a module, for example:

```bash
python -m history.claude_v3_menu_demo
```

| Current path | Former root-level name | Purpose |
| --- | --- | --- |
| `original_two_number.py` | `Sum.py` | Original two-number CLI example. |
| `claude_v1_integer_demo.py` | `SumImprovedbyClaudeCode.py` | Claude v1 integer-input demonstration. |
| `claude_v2_multiple_numbers.py` | `SumImprovedbyClaudeCodev2.py` | Claude v2 finite-float and multiple-number demonstration. |
| `claude_v3_menu_demo.py` | `SumImprovedbyClaudeCodev3.py` | Claude v3 menu and sign-analysis demonstration. |
| `chatgpt_v1_entrypoint.py` | `SumImprovedbyChatGPT.py` | ChatGPT entry point that delegates to the canonical lesson. |
| `chatgpt_v2_test_snapshot.py` | `SumImprovedbyChatGPTv2.py` | Non-collected historical pytest snapshot. |

The active test suite is in [`../tests/`](../tests/); its single core
arithmetic suite is `tests/test_summation_methods.py`.
