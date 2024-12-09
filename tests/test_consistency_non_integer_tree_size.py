import subprocess


def test_consistency_non_integer_tree_size():
    result = subprocess.run(
        [
            'python', './py_rekor_monitor_ss17542_sscs/main.py', '--consistency', '--tree-id', '1193050959916656506',
            '--tree-size', 'not_a_number', '--root-hash', '82eff362e3315d76088793041b0da0165de02f010da049c74b77242c38a08190'
        ],
        capture_output=True,
        text=True
    )
    assert "invalid int value:" in result.stderr.lower() 
    assert result.returncode != 0
