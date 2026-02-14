import os
import sys

# Set the file paths and variables to fallback first
CSES_DIR_PATH = "./cses"
CSES_LANGUAGE = "python"
CSES_BASE_URL = "https://cses.fi/problemset/task/"

# Update file paths to whats stored in the dotfile if the key matches
if os.path.exists("./.cses-script-preferences"):
    with open("./.cses-script-preferences") as f:
        for line in f:
            key, val = line.split("=")
            match key.strip():
                case "CSES_DIR_PATH":
                    CSES_DIR_PATH = val.strip()
                case "CSES_LANGUAGE":
                    CSES_LANGUAGE = val.strip()

# Change dir to the CSES_DIR_PATH
os.chdir(CSES_DIR_PATH)
# Change dir again based on the chosen programming language (create dir if it does not exist)
if not os.path.exists(CSES_LANGUAGE):
    print(f"Directory '{CSES_LANGUAGE}' did not exist so it was created")
    os.mkdir(CSES_LANGUAGE)
os.chdir(CSES_LANGUAGE)

cli_args = sys.argv[1:]
if len(cli_args) < 1:
    print("Incorrect usage! The correct syntax for this script is 'cses.py <cses_problem_code>")
    print("Example - For problem 'Weird Algorithm' you'll see the url https://cses.fi/problemset/task/1068/ and thus it's code is 1068")







# Now lets do a quick pwd to test where we at
print(os.getcwd())
