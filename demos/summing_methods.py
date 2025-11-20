# file: demos/summing_methods.py
from __future__ import annotations

import math
import operator
from functools import reduce
from typing import Iterable, List


def parse_numbers(prompt: str, allow_float: bool = False) -> List[float]:
    """
    Reads a line like:  "10  20  30.5"
    Returns list[float] if allow_float else validates integers only.
    Retries on invalid input to keep demo smooth.
    """
    while True:  # why: interactive demo should not crash on bad input
        raw = input(prompt).strip()
        if not raw:
            print("Please enter one or more numbers separated by spaces.")
            continue
        parts = raw.split()
        try:
            if allow_float:
                return [float(p) for p in parts]
            # validate integers strictly (no 3.0)
            nums: List[float] = []
            for p in parts:
                if p.count(".") or p.lower() in {"nan", "inf", "+inf", "-inf"}:
                    raise ValueError("floats not allowed in integer mode")
                nums.append(float(int(p)))
            return nums
        except ValueError as exc:
            print(f"Invalid input ({exc}). Try again.")


# --- Two-number sum variants -------------------------------------------------

def add_plus(a: float, b: float) -> float:
    """Direct addition with +."""
    return a + b

def add_sum(a: float, b: float) -> float:
    """Built-in sum over a fixed-size tuple."""
    return sum((a, b))

def add_operator(a: float, b: float) -> float:
    """operator.add function."""
    return operator.add(a, b)

# --- N-number sum variants ---------------------------------------------------

def sum_builtin(nums: Iterable[float]) -> float:
    """Built-in sum; fast for numeric lists."""
    return sum(nums)

def sum_reduce(nums: Iterable[float]) -> float:
    """reduce + operator.add; educational."""
    return reduce(operator.add, nums, 0)

def sum_fsum(nums: Iterable[float]) -> float:
    """math.fsum; better numeric stability for floats."""
    return math.fsum(nums)


def show_two_number_demo() -> None:
    a, b = parse_numbers("Enter two integers (e.g., 3 5): ", allow_float=False)[:2]
    print("\nTwo-number methods:")
    print(f"  a + b               -> {add_plus(a, b)}")
    print(f"  sum((a, b))         -> {add_sum(a, b)}")
    print(f"  operator.add(a, b)  -> {add_operator(a, b)}")


def show_many_number_demo() -> None:
    nums = parse_numbers("Enter one or more numbers (floats ok): ", allow_float=True)
    print("\nMany-number methods:")
    print(f"  sum(nums)           -> {sum_builtin(nums)}")
    print(f"  reduce(add, nums)   -> {sum_reduce(nums)}")
    print(f"  math.fsum(nums)     -> {sum_fsum(nums)}")


def main() -> None:
    print("== Summing in Python: multiple approaches ==")
    show_two_number_demo()
    show_many_number_demo()


if __name__ == "__main__":
    main()
