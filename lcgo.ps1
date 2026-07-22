# Creates a Go solution file + matching _test.go file for a LeetCode problem,
# using the raw problem number as a leading filename token (no "p" prefix,
# no zero-padding, no leading underscore since Go's toolchain ignores
# files/dirs starting with "_" or ".").
#
# Usage: .\lcgo.ps1 <problem number> <problem title...>
# Example: .\lcgo.ps1 217 Contains Duplicate

if ($args.Length -lt 1) {
  Write-Output "Usage - .\lcgo.ps1 <problem number> <problem title...>";
  Write-Output "Example - .\lcgo.ps1 217 Contains Duplicate";
  return;
}

$arr = @()
foreach ($arg in $args) {
  foreach ($part in ($arg -split '\s+')) {
    if ($part) {
      $arr += $part
    }
  }
}

if ($arr.Length -lt 2) {
  Write-Output "`nPlease provide both a problem number and a title, e.g. .\lcgo.ps1 217 Contains Duplicate`n";
  return;
}

$arr[0] = $arr[0] -replace '\.$', ''

if ($arr[0] -notmatch '^\d+$') {
  Write-Output "`nFirst argument must be the numeric problem number (e.g. 217)`n";
  return;
}

$number = $arr[0]
$titleWords = $arr[1..($arr.Length - 1)]
$titleDisplay = $titleWords -join ' '

$cleanWords = @()
foreach ($word in $titleWords) {
  $clean = $word -replace '[^a-zA-Z0-9]', ''
  if ($clean) {
    $cleanWords += $clean
  }
}

if ($cleanWords.Length -eq 0) {
  Write-Output "`nProblem title must contain at least one alphanumeric word`n";
  return;
}

$slug = ($cleanWords | ForEach-Object { $_.ToLower() }) -join '_'
$funcName = ($cleanWords | ForEach-Object { $_.Substring(0,1).ToUpper() + $_.Substring(1).ToLower() }) -join ''

# No "p" prefix, no padding - raw number, e.g. 217_contains_duplicate
$baseName = "${number}_${slug}"
$goDir = ".\Leetcode\go"
$solutionPath = "$goDir\$($baseName).go"
$testPath = "$goDir\$($baseName)_test.go"

if ((Test-Path $solutionPath) -or (Test-Path $testPath)) {
  Write-Output "`n$($baseName) already exists!`n";
  return;
}

$goModPath = "$goDir\go.mod"
if (-not (Test-Path $goModPath)) {
  Write-Output "`nNo go.mod found in $goDir - running 'go mod init leetcode'...`n";
  Push-Location $goDir
  go mod init leetcode
  Pop-Location
}

$solutionTemplate = @"
package leetcode

func $funcName(/* TODO: params */) /* TODO: return type */ {
	// TODO: implement
}
"@

$testTemplate = @"
package leetcode

import "testing"

func Test$funcName(t *testing.T) {
	tests := []struct {
		name string
		// TODO: input field(s)
		// TODO: expected field(s)
	}{
		{
			name: "Example 1",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// TODO: call $funcName(...) and compare against expected
		})
	}
}
"@

Set-Content -Path $solutionPath -Value $solutionTemplate
Set-Content -Path $testPath -Value $testTemplate

Write-Output "`nCreated:`n  $solutionPath`n  $testPath`n";
Write-Output "Run this problem's test with:`n  go test -v -run Test$funcName`n";