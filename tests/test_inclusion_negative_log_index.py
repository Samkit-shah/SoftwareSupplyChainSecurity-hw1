import subprocess

def test_inclusion_negative_log_index():
    result = subprocess.run(
        ['python', 'main.py', '--inclusion', '-1', '--artifact', 'sample_artifact.json'],
        capture_output=True,
        text=True
    )
    output = result.stdout
    assert "invalid log index" in output.lower() or "error" in output.lower()
