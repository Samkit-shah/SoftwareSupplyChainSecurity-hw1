import subprocess

def test_debug_mode_inclusion():
    result = subprocess.run(
        ['python', 'main.py', '--debug'],
        capture_output=True,
        text=True
    )
    assert "enabled debug mode" in result.stdout.lower() 
