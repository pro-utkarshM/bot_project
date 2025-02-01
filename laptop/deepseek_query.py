import subprocess

def get_deepseek_command(distance):
    # Query the deepseek model (running locally via Ollama)
    query = f"Obstacle distance: {distance} cm. What should the robot do?"
    response = subprocess.run(
        ["ollama", "run", "deepseek-r1:1.5b", query],
        capture_output=True, text=True
    )
    command = response.stdout.strip()  # Extract command from deepseek output
    return command
