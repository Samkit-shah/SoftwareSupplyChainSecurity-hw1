import subprocess


def test_inclusion_with_artifact():
    result = subprocess.run(
        ['python', './py_rekor_monitor_ss17542_sscs/main.py', '--inclusion', '1', '--artifact', 'sample_artifact.json'],
        capture_output=True,
        text=True
    )
    assert "Inclusion Verified" in result.stdout or "Verification Failed" in result.stdout
    assert result.returncode == 0
