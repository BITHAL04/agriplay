# PowerShell script to verify and upload to GitHub
Set-Location "D:\farmverse\game"

Write-Host "Current directory: $(Get-Location)"
Write-Host "Checking Git status..."

if (Test-Path ".git") {
    Write-Host "Git repository exists"
    git status
    Write-Host "`nRemote repositories:"
    git remote -v
    Write-Host "`nPushing to GitHub..."
    git push origin main
} else {
    Write-Host "No Git repository found. Initializing..."
    git init
    git config user.email "bithal04@example.com"
    git config user.name "BITHAL04"
    git add .
    git commit -m "Initial commit: AgriPlay gamified agriculture learning platform"
    git branch -M main
    git remote add origin https://github.com/BITHAL04/agriplay.git
    git push -u origin main
}

Write-Host "`nFinal status:"
git status
git remote -v
