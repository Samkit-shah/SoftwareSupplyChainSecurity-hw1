 
import subprocess 

def test_consistency_missing_tree_id():
    result = subprocess.run(
        ['python', 'main.py', '--consistency', '--tree-size', '26381176', '--root-hash', '82eff362e3315d76088793041b0da0165de02f010da049c74b77242c38a08190'],
        capture_output=True,
        text=True
    )
    output = result.stdout
    assert "specify tree id" in output.lower()
