 
import subprocess

import main

def test_consistency():
    result = subprocess.run(
        ['python', 'main.py', '--consistency', '--tree-id', '1193050959916656506', '--tree-size', '26382788', '--root-hash', 'c38cb903f820524de4107e820d63e6a6b68f6d9e459464f867f90aa6c9305f1b'],
 
        capture_output=True,
        text=True
    ) 

    assert "Consistency Verified" in result.stdout