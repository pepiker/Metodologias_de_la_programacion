#Portada: IKER MISAEL ZAPATA ORTEGA
#Matriculation: 2530077
# Group: IM 1-3

"""
Resumen ejecutivo:
- A for loop iterates a known number of times, useful for processing sequences or ranges.
- A while loop continues until a condition changes, ideal when iterations depend on runtime data (e.g., sentinel or attempts).
- A counter tracks occurrences (initialized before loop and incremented), an accumulator aggregates values (sum).
- Defining a clear exit condition avoids infinite loops; always update loop control variables in while loops.
- This file contains 6 problems (with descriptions, inputs, outputs, validations and tests) that illustrate for/while usage,
  plus conclusions and references at the end.

Principles and good practices (short):
- Use for when the number of iterations is known (for i in range(...)).
- Use while when iterations depend on a condition (e.g., read until "EXIT").
- Initialize counters and accumulators before loops.
- Update loop-control variables in while loops to avoid infinite loops.
- Keep loop bodies small; extract logic to functions when needed.

Diagrams / tables (optional):
- "Flowchart Problem 3: (Start) -> Read value -> If sentinel? -> Yes: compute average -> No: add to sum and continue"
- "Table of test cases: Problem#, CaseType, Input, ExpectedOutput (described beside each problem below)"

References:
1. "Python 3 Documentation", docs.python.org
2. "Automate the Boring Stuff with Python", Al Sweigart
3. "Think Python", Allen B. Downey
4. "Introduction to Algorithms", Cormen et al. (for algorithmic thinking)
5. "Clean Code", Robert C. Martin (for best practices in code structure)
6. Additional online tutorials and course notes (local materials)
"""


# Problem 1: Sum of range with for
# Description:
#   Compute the sum of integers from 1 to n (inclusive) and the sum of even numbers in that range.
#
# Inputs:
#   - n (int)
#
# Outputs:
#   - "Sum 1..n:" <total_sum>
#   - "Even sum 1..n:" <even_sum>
#
# Validations:
#   - n must be convertible to int
#   - n >= 1
#   - On invalid input print "Error: invalid input"
#
# Test cases:
#   1) Normal: n = 10  -> Sum 1..10: 55 ; Even sum: 30
#   2) Border: n = 1   -> Sum 1..1: 1  ; Even sum: 0
#   3) Error: n = 0    -> "Error: invalid input"
# -----------------------------------------------------------------------------

def problem1_sum_range(n_input):
    """
    Sum 1..n and sum of even numbers in range using for with range().
    Returns tuple (success:bool, message:str).
    """
    try:
        n = int(n_input)
    except Exception:
        return False, "Error: invalid input"

    if n < 1:
        return False, "Error: invalid input"

    total_sum = 0
    even_sum = 0
    # for ... in range(...)
    for i in range(1, n + 1):
        total_sum = total_sum + i
        if i % 2 == 0:
            even_sum = even_sum + i

    result_msg = f"Sum 1..n: {total_sum}\nEven sum 1..n: {even_sum}"
    return True, result_msg

# Problem 1 - automated test runner
def test_problem1():
    cases = [
        ("Normal", 10, True, "Sum 1..n: 55"),
        ("Border", 1, True, "Sum 1..n: 1"),
        ("Error", 0, False, "Error: invalid input"),
    ]
    print("=== Problem 1 Tests ===")
    for name, inp, expected_ok, expected_contains in cases:
        ok, msg = problem1_sum_range(inp)
        print(f"Case: {name} | Input: {inp} | OK: {ok}")
        print(msg)
        assert ok == expected_ok, f"Expected ok={expected_ok} got {ok}"
        assert expected_contains in msg, f"Expected message to contain '{expected_contains}'"
    print()

# Problem 2: Multiplication table with for
# Description:
#   Generate multiplication table for a base from 1..m.
#
# Inputs:
#   - base (int)
#   - m (int)
#
# Outputs:
#   - lines like "5 x 1 = 5"
#
# Validations:
#   - base and m convertible to int
#   - m >= 1
#   - On invalid input print "Error: invalid input"
#
# Test cases:
#   1) Normal: base=5, m=4  -> lines 5x1..5x4
#   2) Border: base=3, m=1  -> one line "3 x 1 = 3"
#   3) Error: base=2, m=0   -> "Error: invalid input"
# -----------------------------------------------------------------------------

def problem2_multiplication_table(base_input, m_input):
    """
    Prints multiplication table lines and returns (success, list_of_lines_or_error).
    Uses: for i in range(1, m+1)
    """
    try:
        base = int(base_input)
        m = int(m_input)
    except Exception:
        return False, ["Error: invalid input"]

    if m < 1:
        return False, ["Error: invalid input"]

    lines = []
    for i in range(1, m + 1):
        product = base * i
        lines.append(f"{base} x {i} = {product}")
    return True, lines

def test_problem2():
    cases = [
        ("Normal", 5, 4, True, "5 x 4 = 20"),
        ("Border", 3, 1, True, "3 x 1 = 3"),
        ("Error", 2, 0, False, "Error: invalid input"),
    ]
    print("=== Problem 2 Tests ===")
    for name, base, m, expected_ok, expected_contains in cases:
        ok, out = problem2_multiplication_table(base, m)
        print(f"Case: {name} | base={base} m={m} | OK: {ok}")
        if ok:
            for line in out:
                print(line)
            assert expected_contains in out[-1], "Unexpected last line"
        else:
            print(out[0])
            assert out[0] == expected_contains
    print()

# Problem 3: Average of numbers with while and sentinel
# Description:
#   Read numbers until sentinel_value (-1). Compute count and average of valid numbers.
#
# Inputs:
#   - sequence of numbers provided (simulated as a list in tests)
#   - sentinel_value fixed as -1
#
# Outputs:
#   - "Count:" <count>
#   - "Average:" <average_value>
#   - If no valid data: "Error: no data"
#
# Validations:
#   - each input convertible to float
#   - ignore sentinel in calculations
#
# Test cases:
#   1) Normal: [10, 20, -1] -> Count:2 Average:15.0
#   2) Border: [-1]         -> Error: no data
#   3) Error: [10, "abc", -1] -> Should treat "abc" as invalid -> Error message for invalid input
# -----------------------------------------------------------------------------

SENTINEL_VALUE = -1.0

def problem3_average_with_sentinel(input_sequence):
    """
    Simulates reading floats until sentinel. Returns (success, message).
    If any input in sequence that is not convertible to float (and not sentinel), return error.
    """
    total = 0.0
    count = 0
    index = 0
    while True:
        if index >= len(input_sequence):
            # If sequence ended without sentinel, treat that as end (but allowed)
            break
        raw = input_sequence[index]
        index = index + 1
        # Try convert
        try:
            value = float(raw)
        except Exception:
            return False, "Error: invalid input"

        if value == SENTINEL_VALUE:
            break
        total = total + value
        count = count + 1

    if count == 0:
        return False, "Error: no data"
    average_value = total / count
    msg = f"Count: {count}\nAverage: {average_value}"
    return True, msg

def test_problem3():
    cases = [
        ("Normal", [10, 20, -1], True, "Count: 2"),
        ("Border", [-1], False, "Error: no data"),
        ("Error", [10, "abc", -1], False, "Error: invalid input"),
    ]
    print("=== Problem 3 Tests ===")
    for name, seq, expected_ok, expected_contains in cases:
        ok, msg = problem3_average_with_sentinel(seq)
        print(f"Case: {name} | Input: {seq} | OK: {ok}")
        print(msg)
        assert ok == expected_ok
        assert expected_contains in msg
    print()

# Problem 4: Password attempts with while
# Description:
#   Simple password check with MAX_ATTEMPTS attempts.
#
# Inputs:
#   - user_password attempts (simulated list in tests)
#
# Outputs:
#   - "Login success" or "Account locked"
#
# Validations:
#   - MAX_ATTEMPTS > 0 (constant)
#   - Count attempts correctly
#
# Test cases:
#   1) Normal: correct on 2nd attempt -> "Login success"
#   2) Border: correct on 1st attempt  -> "Login success"
#   3) Error: all wrong until exhausted -> "Account locked"
# -----------------------------------------------------------------------------

MAX_ATTEMPTS = 3
CORRECT_PASSWORD = "admin123"

def problem4_password_attempts(attempts_sequence):
    """
    Simulate password attempts using while loop.
    attempts_sequence: list of strings representing attempts.
    Returns (success, message).
    """
    if MAX_ATTEMPTS <= 0:
        return False, "Error: invalid system configuration"

    attempts = 0
    index = 0
    while attempts < MAX_ATTEMPTS:
        if index >= len(attempts_sequence):
            # No more user inputs; treat as failure
            break
        user_password = attempts_sequence[index]
        index = index + 1
        attempts = attempts + 1
        if user_password == CORRECT_PASSWORD:
            return True, "Login success"
        # else continue
    return False, "Account locked"

def test_problem4():
    cases = [
        ("Normal", ["wrong", "admin123"], True, "Login success"),
        ("Border", ["admin123"], True, "Login success"),
        ("Error", ["a", "b", "c"], False, "Account locked"),
    ]
    print("=== Problem 4 Tests ===")
    for name, seq, expected_ok, expected_contains in cases:
        ok, msg = problem4_password_attempts(seq)
        print(f"Case: {name} | Attempts: {seq} | OK: {ok}")
        print(msg)
        assert ok == expected_ok
        assert expected_contains in msg
    print()

# Problem 5: Simple menu with while
# Description:
#   Text menu that repeats until user selects exit (0).
#
# Inputs:
#   - option (int simulated in a sequence for tests)
#
# Outputs:
#   - "Hello!" for option 1
#   - "Counter:" <counter_value> for option 2
#   - "Counter incremented" for option 3
#   - "Bye!" for exit 0
#   - "Error: invalid option" for invalid options
#
# Validations:
#   - options must be convertible to int
#   - accept only 0,1,2,3 as valid
#
# Test cases:
#   1) Normal: [1,3,2,0] -> shows greeting, increments, shows counter then exit
#   2) Border: [0]       -> immediate exit, prints "Bye!"
#   3) Error: ["x", 0]   -> invalid option then exit
# -----------------------------------------------------------------------------

def problem5_simple_menu(option_sequence):
    """
    Simulate menu interactions. option_sequence is a list of inputs.
    Returns a list of output messages generated during the session.
    """
    outputs = []
    counter = 0
    index = 0
    while True:
        # Get option from sequence or break
        if index >= len(option_sequence):
            # No more inputs; exit gracefully
            outputs.append("Bye!")
            break
        raw_option = option_sequence[index]
        index = index + 1
        try:
            option = int(raw_option)
        except Exception:
            outputs.append("Error: invalid option")
            continue

        if option == 0:
            outputs.append("Bye!")
            break
        elif option == 1:
            outputs.append("Hello!")
        elif option == 2:
            outputs.append(f"Counter: {counter}")
        elif option == 3:
            counter = counter + 1
            outputs.append("Counter incremented")
        else:
            outputs.append("Error: invalid option")
    return outputs

def test_problem5():
    cases = [
        ("Normal", [1,3,2,0], ["Hello!", "Counter incremented", "Counter: 1", "Bye!"]),
        ("Border", [0], ["Bye!"]),
        ("Error", ["x", 0], ["Error: invalid option", "Bye!"]),
    ]
    print("=== Problem 5 Tests ===")
    for name, seq, expected in cases:
        out = problem5_simple_menu(seq)
        print(f"Case: {name} | Input: {seq}")
        for line in out:
            print(line)
        # Check that expected sequence is a prefix of output (for robustness)
        assert out == expected, f"Expected {expected} but got {out}"
    print()

# Problem 6: Pattern printing with nested loops
# Description:
#   Print right-angled triangle of '*' for n rows and optionally inverted pattern.
#
# Inputs:
#   - n (int)
#
# Outputs:
#   - lines with 1..n asterisks
#   - optional inverted pattern lines with n-1..1 asterisks (documented)
#
# Validations:
#   - n convertible to int
#   - n >= 1
#
# Test cases:
#   1) Normal: n=4 -> "*", "**", "***", "****"
#   2) Border: n=1 -> "*"
#   3) Error: n=0  -> "Error: invalid input"
# -----------------------------------------------------------------------------

def problem6_pattern_triangle(n_input, inverted=False):
    """
    Return list of pattern lines or error message.
    Uses nested loops logic (conceptually) but uses string repetition for simplicity.
    """
    try:
        n = int(n_input)
    except Exception:
        return False, ["Error: invalid input"]

    if n < 1:
        return False, ["Error: invalid input"]

    lines = []
    # Using for i in range(1, n+1)
    for i in range(1, n + 1):
        # build a line of i stars; this simulates inner loop of concatenation
        line = "*" * i
        lines.append(line)

    if inverted:
        # optional inverted pattern
        for i in range(n - 1, 0, -1):
            lines.append("*" * i)

    return True, lines

def test_problem6():
    cases = [
        ("Normal", 4, True, "*\n**\n***\n****"),
        ("Border", 1, True, "*"),
        ("Error", 0, False, "Error: invalid input"),
    ]
    print("=== Problem 6 Tests ===")
    for name, n, expected_ok, expected_contains in cases:
        ok, out = problem6_pattern_triangle(n, inverted=False)
        print(f"Case: {name} | n={n} | OK: {ok}")
        if ok:
            for line in out:
                print(line)
            combined = "\\n".join(out)
            assert expected_contains in combined
        else:
            print(out[0])
            assert out[0] == expected_contains
    print()

if __name__ == "__main__":
    # Run all problem tests sequentially
    test_problem1()
    test_problem2()
    test_problem3()
    test_problem4()
    test_problem5()
    test_problem6()
    print("All tests completed successfully.")