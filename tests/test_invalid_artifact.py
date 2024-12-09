 
import subprocess

import main

def test_incorrect_input():
    result = subprocess.run(
        ['python', './py_rekor_monitor_ss17542_sscs/main.py', '--inclusion', '133040969', '--artifact', './py_rekor_monitor_ss17542_sscs/util.py'],
        capture_output=True,
        text=True
    ) 
    assert "Signature Verification Failed" in result.stdout