import subprocess
import sys
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

def show_input_box(prompt):
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("Input", prompt)
    root.destroy()
    return user_input

def save_image_stub(image_data, filename):
    # This is a stub for image generation. Replace with actual image generation logic.
    os.makedirs('downloads/ai 1.02/images', exist_ok=True)
    path = os.path.join('downloads/ai 1.02/images', filename)
    with open(path, 'wb') as f:
        f.write(image_data)
    return path

def main():
    os.system('title ai')
    print("                                      hello")
    while True:
        cmd = input("Type a command (gencode | gentext | genimage | exit): ").strip()
        if cmd == "exit":
            break
        elif cmd == "gencode":
            code = show_input_box("Generate your code:")
            print(f"Generated code:\n{code}")
        elif cmd == "gentext":
            text = show_input_box("Generate your text:")
            print(f"Generated text:\n{text}")
        elif cmd == "genimage":
            desc = show_input_box("Generate your image:")
            # Stub: just save a blank file as an example
            filename = f"{desc.replace(' ', '_')}.png"
            image_path = save_image_stub(b'', filename)
            print(f"Image saved to: {image_path}")
        else:
            print("what the atual fuck did you do")

if __name__ == "__main__":
    main()