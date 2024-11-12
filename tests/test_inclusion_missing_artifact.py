import subprocess

def test_inclusion_missing_artifact():
    result = subprocess.run(
        ['python', 'main.py', '--inclusion', '1'],
        capture_output=True,
        text=True
    )
    output = result.stdout
    assert "artifact filepath" in output.lower() or "error" in output.lower()
