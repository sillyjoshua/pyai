import os
import sys
import subprocess
from pathlib import Path

def open_cmd():
    if sys.platform.startswith('win'):
        subprocess.Popen('start cmd', shell=True)
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', '-a', 'Terminal'])
    else:
        subprocess.Popen(['x-terminal-emulator'])

def generate_code(code_str, filename):
    with open(filename, 'w') as f:
        f.write(code_str)
    print(f"Code saved to {filename}")

def generate_text(text_str, filename):
    with open(filename, 'w') as f:
        f.write(text_str)
    print(f"Text saved to {filename}")

def generate_image(image_bytes, filename):
    images_dir = Path.home() / 'Downloads' / 'ai' / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)
    image_path = images_dir / filename
    with open(image_path, 'wb') as f:
        f.write(image_bytes)
    print(f"Image saved to {image_path}")

if __name__ == "__main__":
    open_cmd()
    # Example usage:
    # generate_code('print("Hello World")', 'hello.py')
    # generate_text('This is a sample text.', 'sample.txt')
    # generate_image(b'\x89PNG\r\n\x1a\n...', 'sample.png')  # Replace with real image bytes