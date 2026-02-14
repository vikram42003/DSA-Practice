# This is a powershell script I created to create a python file for the leetcode problem in the file naming scheme I'm using

# Check for incorrect usage
if ($args.Length -lt 1) {
  Write-Output "Usage - .\lc.ps1 <leetcode problem's full title>";
  return;
}

$arr = $args
if ($args.Length -eq 1) {
  $arr = $args[0].ToString().Split(" ");
}

# Remove the dot after question code
$arr[0] = $arr[0] -replace '\.$', ''

# Create the filename
$str = "";
for ($i = 0; $i -lt $arr.Length; $i++) {
  $str += "_" + $arr[$i];
}
$str += ".py";

# Remove any invalid filename characters
$str = $str -replace '[<>:"/\\|?*]', ''

$filepath = ".\Leetcode\python\$($str)";

# Prevent overwriting files
if (Test-Path $filepath) {
  Write-Output "`n$($str) already exists!`n";
  return;
}

# Create the actual file
New-Item $filepath -ItemType File | Out-Null;

Write-Output "`n$($filepath) created successfully`n";