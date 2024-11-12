import subprocess

def test_checkpoint_command():
    result = subprocess.run(
        ['python', 'main.py', '--checkpoint'],
        capture_output=True,
        text=True
    )
    assert "inactiveshards" in result.stdout.lower() 
