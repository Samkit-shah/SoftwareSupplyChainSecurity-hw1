import subprocess


def test_consistency_missing_root_hash():
    result = subprocess.run(
        [
            'python', 'main.py', '--consistency', '--tree-id', '1193050959916656506', '--tree-size', '26381176'
        ],
        capture_output=True,
        text=True
    )
    assert "please specify root hash" in result.stdout.lower() 
