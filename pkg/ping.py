import subprocess

def run(host):
  try:
    command = ['ping', '-c', '4', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout  # Return the output if successful
  except subprocess.CalledProcessError as e:
    return f"Kesalahan eksekusi: {e}\nPrint: {e.output}"
  except Exception as e:
    return f"Kesalahan tindakan: {e}"