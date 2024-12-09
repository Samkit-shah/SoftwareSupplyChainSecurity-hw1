import subprocess


def test_inclusion_non_integer_log_index():
    result = subprocess.run(
        ['python', './py_rekor_monitor_ss17542_sscs/main.py', '--inclusion', 'invalid', '--artifact', 'sample_artifact.json'],
        capture_output=True,
        text=True
    )
    assert "invalid int value" in result.stderr
    assert result.returncode != 0
