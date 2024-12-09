import subprocess 

def test_checkpoint_command():
    result = subprocess.run(
        ['python', './py_rekor_monitor_ss17542_sscs/main.py', '--checkpoint'],
        capture_output=True,
        text=True
    )
    assert "inactiveshards" in result.stdout.lower() 
