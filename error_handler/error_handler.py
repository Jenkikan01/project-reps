#!/usr/bin/env python3

print("=== SOC Error Handler ===\n")

print("--- Safe Division ---")
try:
    divisor = int(input("Enter divisor: "))
    dividend =int(input("Enter dividend: "))
    quotient = divisor / dividend
    print(f"Result: {divisor} / {dividend} = {quotient:.2f}")

except ValueError:
    print("ERROR: Value entered is invalid.")
except ZeroDivisionError:
    print(f"ERROR: {divisor} cannot be divided by {dividend}.")

print()

print("--- Safe File Read (.readlines()) ---")
try:
    filename = input("Enter filename here (Try 'soc_logs.txt' or 'missing.txt'): ")
    with open(filename, "r") as f:
        contents = f.readlines()
        for i, contents in enumerate(contents, start=1):
            contents = contents.strip()
            print(f"  {i}: {contents}")
        print(f"Total lines: {len(contents)}\n")

except FileNotFoundError:
    print(f"ERROR: {filename} doesnt exist.")
except PermissionError:
    print(f"ERROR: {filename} dont have a read permission.")

print()

print("--- Combined Safe + Calculate ---")
try:
    filename = input("Enter a file with a number(Try 'soc_logs.txt' or 'missing.txt'): ")
    with open(filename, "r") as file:
        contents = file.readlines()
    divisor = len(contents)
    num_to_divide = int(input("Enter number to divide: "))
    line_division = divisor / num_to_divide
    print(f"{divisor} lines / {num_to_divide} = {line_division:.2f}\n")
    print()
    print("Program ran successfully. No crashes!")
except ValueError:
    print("ERROR: Value entered is invalid.")
except ZeroDivisionError:
    print(f"ERROR: {divisor} can't be divided by {num_to_divide}.")
except FileNotFoundError:
    print(f"ERROR: {filename} does'nt exist.")
except Exception as e:
    print(f"ERROR: Unexpected {e}.")


