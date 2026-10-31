# This is a powershell script to create a python file for a Codeforces problem in the file naming scheme I'm using

# Check for incorrect usage
if ($args.Length -lt 1) {
  Write-Output "Usage - .\cf.ps1 <contest+letter> <problem title>";
  Write-Output "Example - For problem 'Riddle' at https://codeforces.com/contest/1845/problem/A you'd run: .\cf.ps1 1845A Riddle";
  return;
}

$arr = $args
if ($args.Length -eq 1) {
  $arr = $args[0].ToString().Split(" ");
}

# Remove the dot after the problem code, in case I enter it
$arr[0] = $arr[0] -replace '\.$', ''

# Create the filename
$str = "";
for ($i = 0; $i -lt $arr.Length; $i++) {
  $str += "_" + $arr[$i];
}
# Remove leading underscore
$str = $str.TrimStart("_")

# Remove any invalid filename characters
$str = $str -replace '[<>:"/\\|?*]', '';

# create a folder for the problem first, only if it doesnt exist
$folderpath = ".\Codeforces\python\$($str)";
if (Test-Path $folderpath) {
  Write-Output "`n$($folderpath) already exists!`n";
  return;
}
New-Item $folderpath -ItemType Directory | Out-Null;

# create the file for the problem, only if it doesnt exist
$str += ".py";
$filepath = "$($folderpath)\$($str)";
if (Test-Path $filepath) {
  Write-Output "`n$($str) already exists!`n";
  return;
}
New-Item $filepath -ItemType File | Out-Null;

# ---------------- PYTHON TEMPLATE ----------------

$template = @"
import sys

input = sys.stdin.readline
write = sys.stdout.write

def solve():
    # ------------------ INPUT ------------------
    pass

    # ------------------ LOGIC ------------------
    

    # ------------------ OUTPUT ------------------
    

def solution():
    # Default: single test case per run (multi_runner handles multiple cases separated by blank lines in input.txt)
    solve()

    # If the problem statement specifies 't' test cases in a single run (standard CF contests), swap with:
    # t = int(input())
    # for _ in range(t):
    #     solve()

if __name__ == "__main__":
    solution()
"@

Set-Content -Path $filepath -Value $template

New-Item -Path $folderpath -Name "input.txt" -ItemType File | Out-Null
New-Item -Path $folderpath -Name "output.txt" -ItemType File | Out-Null

Write-Output "`n$($filepath) created successfully`n";

