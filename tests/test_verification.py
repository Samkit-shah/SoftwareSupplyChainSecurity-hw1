


import subprocess

def test_verification():
    result = subprocess.run( 
        ["python3", "main.py", "--inclusion", "148286913", "--artifact", "artifact.md"],
        capture_output=True,
        text=True
    )
    assert "Inclusion Verified" in result.stdout
