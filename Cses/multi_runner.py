import sys
import subprocess
import os


def main():
    if len(sys.argv) < 2:
        print("Usage: multi_runner.py <script.py>", file=sys.stderr)
        return

    script_path = sys.argv[1]
    input_path = "input.txt"

    # If no input file, run once with no stdin
    if not os.path.exists(input_path):
        subprocess.run([sys.executable, script_path])
        return

    with open(input_path, "r") as f:
        raw = f.read()

    # Split input into chunks separated by blank lines.
    # Each chunk is one test case's input block.
    # If there are NO blank lines, each non-empty line is its own test case.
    chunks = []
    current = []

    for line in raw.splitlines(keepends=True):
        if line.strip() == "":
            if current:
                chunks.append("".join(current))
                current = []
        else:
            current.append(line)

    if current:
        chunks.append("".join(current))

    if not chunks:
        subprocess.run([sys.executable, script_path])
        return

    results = []

    for i, chunk in enumerate(chunks, 1):
        print(f"--- Run {i} (input: {chunk.strip()!r}) ---", file=sys.stderr)
        sys.stderr.flush()

        result = subprocess.run(
            [sys.executable, script_path],
            input=chunk,
            capture_output=True,
            text=True,
        )

        output = result.stdout
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)

        results.append(f"--- Run {i} ---\n{output}\n")
        # print(output, end="")  # live preview in terminal
        sys.stdout.flush()

    # Write combined results to output.txt
    with open("output.txt", "w") as f:
        f.write("".join(results))


if __name__ == "__main__":
    main()
