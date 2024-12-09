import subprocess

def test_main_run(): 
    result = subprocess.run(
        ['python', './py_rekor_monitor_ss17542_sscs/main.py', '--help'],
        capture_output=True,
        text=True
    )
    output = result.stdout 
    
    assert "Obtain latest checkpoint" in output 
