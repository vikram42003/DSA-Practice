"""
Debug runner script for CSES problems.
Redirects stdin from input.txt and executes the target file.
Allows debugger to step through the actual code.
"""

import sys
import os
import runpy

if len(sys.argv) < 2:
    print("Usage: debug_runner.py <python_file>")
    sys.exit(1)

target_file = sys.argv[1]
target_dir = os.path.dirname(target_file)
input_file = os.path.join(target_dir, "input.txt")

# Redirect stdin from input.txt if it exists
if os.path.exists(input_file):
    sys.stdin = open(input_file, "r")

# Change to target directory
os.chdir(target_dir)

# Run the target file with proper debugger support
runpy.run_path(target_file, run_name="__main__")
