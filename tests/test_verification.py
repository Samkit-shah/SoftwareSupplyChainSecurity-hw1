


import subprocess

def test_verification():
    result = subprocess.run( 
        ["python3", "./py_rekor_monitor_ss17542_sscs/main.py", "--inclusion", "148286913", "--artifact", "artifact.md"],
        capture_output=True,
        text=True
    )
    assert "Inclusion Verified" in result.stdout
