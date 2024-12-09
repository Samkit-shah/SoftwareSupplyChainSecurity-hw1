import subprocess

def test_invalid_command_argument():
    result = subprocess.run(
        ['python', './py_rekor_monitor_ss17542_sscs/main.py', '--RANDOM'],
        capture_output=True,
        text=True
    )
    assert "usage" in result.stderr.lower() or "error" in result.stderr.lower()
    assert result.returncode != 0