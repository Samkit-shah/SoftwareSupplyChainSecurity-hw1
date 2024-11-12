import subprocess

def test_main_run(): 
    result = subprocess.run(
        ['python', 'main.py', '--help'],
        capture_output=True,
        text=True
    )
    output = result.stdout 
    
    assert "Obtain latest checkpoint" in output 
