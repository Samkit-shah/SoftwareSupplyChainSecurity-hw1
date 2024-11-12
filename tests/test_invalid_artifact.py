 
import subprocess

import main

def test_incorrect_input():
    result = subprocess.run(
        ['python', 'main.py', '--inclusion', '133040969', '--artifact', 'util.py'],
        capture_output=True,
        text=True
    ) 
    assert "Signature Verification Failed" in result.stdout