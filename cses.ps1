# This is a powershell script I created to create a python file for the cses problem in the file naming scheme I'm using

# Check for incorrect usage
if ($args.Length -lt 1) {
  Write-Output "Usage - .\cses.ps1 <cses problem code> <cses problem title>";
  Write-Output "Example - For problem 'Weird Algorithm' you'll see the url https://cses.fi/problemset/task/1068/ and thus it's code is 1068";
  return;
}

$arr = $args
if ($args.Length -eq 1) {
  $arr = $args[0].ToString().Split(" ");
}

# Remove the dot after the question code, incase I enter it
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
$folderpath = ".\Cses\python\$($str)";
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

Write-Output "`n$($filepath) created successfully`n";