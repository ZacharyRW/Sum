# file: demos/summing_methods.py
from __future__ import annotations

import math
import operator
from functools import reduce
from typing import Iterable, List, Optional, Union

Number = Union[int, float]


def parse_numbers(
    prompt: str, allow_float: bool = False
) -> Optional[List[Number]]:
    """
    Read a space-separated line of finite numbers.

    Integer mode returns exact ``int`` values. Float mode accepts only finite
    ``float`` values. Returns ``None`` after an EOF so callers can exit cleanly.
    """
    while True:
        try:
            raw = input(prompt).strip()
        except EOFError:
            print("Input closed. Exiting this demo.")
            return None

        if not raw:
            print("Please enter one or more numbers separated by spaces.")
            continue

        parts = raw.split()
        try:
            if allow_float:
                numbers = [float(part) for part in parts]
                if not all(math.isfinite(number) for number in numbers):
                    raise ValueError("numbers must be finite")
                return numbers
            return [int(part) for part in parts]
        except ValueError as exc:
            print(f"Invalid input ({exc}). Try again.")


# --- Two-number sum variants -------------------------------------------------

def add_plus(a: Number, b: Number) -> Number:
    """Direct addition with +."""
    return a + b

def add_sum(a: Number, b: Number) -> Number:
    """Built-in sum over a fixed-size tuple."""
    return sum((a, b))

def add_operator(a: Number, b: Number) -> Number:
    """operator.add function."""
    return operator.add(a, b)

# --- N-number sum variants ---------------------------------------------------

def sum_builtin(nums: Iterable[Number]) -> Number:
    """Built-in sum; fast for numeric lists."""
    return sum(nums)

def sum_reduce(nums: Iterable[Number]) -> Number:
    """reduce + operator.add; educational."""
    return reduce(operator.add, nums, 0)

def sum_fsum(nums: Iterable[Number]) -> float:
    """math.fsum; better numeric stability for floats."""
    return math.fsum(nums)


def show_two_number_demo() -> bool:
    """Show the two-number lesson and report whether input remained open."""
    while True:
        numbers = parse_numbers(
            "Enter exactly two integers (e.g., 3 5): ", allow_float=False
        )
        if numbers is None:
            return False
        if len(numbers) == 2:
            a, b = numbers
            break
        print("Please enter exactly two integers separated by spaces.")

    print("\nTwo-number methods:")
    print(f"  a + b               -> {add_plus(a, b)}")
    print(f"  sum((a, b))         -> {add_sum(a, b)}")
    print(f"  operator.add(a, b)  -> {add_operator(a, b)}")
    return True


def show_many_number_demo() -> bool:
    """Show the many-number lesson and report whether input remained open."""
    nums = parse_numbers("Enter one or more numbers (floats ok): ", allow_float=True)
    if nums is None:
        return False
    print("\nMany-number methods:")
    print(f"  sum(nums)           -> {sum_builtin(nums)}")
    print(f"  reduce(add, nums)   -> {sum_reduce(nums)}")
    print(f"  math.fsum(nums)     -> {sum_fsum(nums)}")
    return True


def main() -> None:
    print("== Summing in Python: multiple approaches ==")
    if not show_two_number_demo():
        return
    show_many_number_demo()


if __name__ == "__main__":
    main()
