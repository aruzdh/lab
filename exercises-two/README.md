# exercises-one

A C project with solutions to algorithmic problems: converting integers to/from Roman numerals, finding the longest common prefix, and identifying missing/repeated values in a matrix. Includes unit tests using the Unity framework.

## Project Structure

- **`include/`**: Header files (`int_to_roman.h`, `longest_common_prefix.h`, etc.).
- **`src/`**: Source files (`int_to_roman.c`, `longest_common_prefix.c`, etc.).
- **`test/`**: Test files (`test_int_to_roman.c`, etc.).
- **`unity/`**: Unity testing framework files (`unity.c`, `unity.h`, `unity_internals.h`).
- **`build/`**: Generated directory for compiled test executables.
- **`makefile`**: For compiling and running tests.

## Prerequisites

- **GCC** (C compiler):
- **Make**: Usually bundled with GCC.

## Libraries

- **Unity Testing Framework**: Already included in `unity/`. No installation needed.

## Compilation

Use the `makefile` to compile. Executables are placed in `build/`.

- Compile all tests:

  ```bash
  make all
  ```

## Running Tests

- Run all test

  ```bash
  make run
  ```

- Run specific tests:
  - Roman to Integer: `make run_roman_to_int`
  - Integer to Roman: `make run_int_to_roman`
  - Longest Common Prefix: `make run_longest_common_prefix`
  - Missing and Repeated Value: `make run_missing_and_repeated_value`

## Cleaning Up

Remove compiled files:

```bash
make clean
```
