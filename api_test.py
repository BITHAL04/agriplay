"""
Test API endpoints with PowerShell's Invoke-RestMethod
"""
import subprocess
import json
import sys

def run_powershell(command):
    """Run a PowerShell command and return the result"""
    try:
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "", "Timeout", 1

def test_health():
    """Test health endpoint"""
    print("🏥 Testing health endpoint...")
    
    command = '''
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/" -Method GET
        Write-Host "SUCCESS: $($response)"
    } catch {
        Write-Host "ERROR: $($_.Exception.Message)"
    }
    '''
    
    stdout, stderr, code = run_powershell(command)
    print(f"Response: {stdout}")
    if stderr:
        print(f"Error: {stderr}")
    return code == 0

def test_registration():
    """Test registration endpoint"""
    print("\n📝 Testing registration endpoint...")
    
    command = '''
    $body = @{
        username = "testuser456"
        email = "test456@example.com"
        password = "testpass123"
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/api/auth/register" -Method POST -Body $body -ContentType "application/json"
        Write-Host "SUCCESS: $($response | ConvertTo-Json -Depth 10)"
    } catch {
        Write-Host "ERROR: $($_.Exception.Message)"
        if ($_.Exception.Response) {
            $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
            $responseBody = $reader.ReadToEnd()
            Write-Host "Response Body: $responseBody"
        }
    }
    '''
    
    stdout, stderr, code = run_powershell(command)
    print(f"Response: {stdout}")
    if stderr:
        print(f"Error: {stderr}")
    return "SUCCESS" in stdout

def test_login():
    """Test login endpoint"""
    print("\n🔑 Testing login endpoint...")
    
    command = '''
    $body = @{
        username = "testuser456"
        password = "testpass123"
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/api/auth/login" -Method POST -Body $body -ContentType "application/json"
        Write-Host "SUCCESS: $($response | ConvertTo-Json -Depth 10)"
    } catch {
        Write-Host "ERROR: $($_.Exception.Message)"
        if ($_.Exception.Response) {
            $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
            $responseBody = $reader.ReadToEnd()
            Write-Host "Response Body: $responseBody"
        }
    }
    '''
    
    stdout, stderr, code = run_powershell(command)
    print(f"Response: {stdout}")
    if stderr:
        print(f"Error: {stderr}")
    return "SUCCESS" in stdout

def test_stages():
    """Test stages endpoint"""
    print("\n📚 Testing stages endpoint...")
    
    command = '''
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:8000/api/stages/" -Method GET
        Write-Host "SUCCESS: Found $($response.Count) stages"
        $response | ForEach-Object { Write-Host "- $($_.title) (Order: $($_.order_number), XP: $($_.xp_reward))" }
    } catch {
        Write-Host "ERROR: $($_.Exception.Message)"
    }
    '''
    
    stdout, stderr, code = run_powershell(command)
    print(f"Response: {stdout}")
    if stderr:
        print(f"Error: {stderr}")
    return "SUCCESS" in stdout

if __name__ == "__main__":
    print("🧪 Testing AgriPlay API Endpoints")
    print("=" * 50)
    
    # Test health
    health_ok = test_health()
    
    if not health_ok:
        print("❌ Health check failed. Is the server running?")
        sys.exit(1)
    
    # Test registration
    reg_ok = test_registration()
    
    # Test login
    login_ok = test_login()
    
    # Test stages
    stages_ok = test_stages()
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print(f"   Health: {'✅' if health_ok else '❌'}")
    print(f"   Registration: {'✅' if reg_ok else '❌'}")
    print(f"   Login: {'✅' if login_ok else '❌'}")
    print(f"   Stages: {'✅' if stages_ok else '❌'}")
    
    if all([health_ok, reg_ok, login_ok, stages_ok]):
        print("\n🎉 All tests passed! Backend is working correctly.")
    else:
        print("\n⚠️ Some tests failed. Check the output above for details.")
