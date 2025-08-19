import os
from PIL import Image, ImageDraw, ImageFont
import random
import string

IMAGES_DIR = os.path.expanduser("~/Desktop/ai/images")

def generate_image(filename="generated_image.png", text="Hello, AI!"):
    os.makedirs(IMAGES_DIR, exist_ok=True)
    img = Image.new('RGB', (400, 200), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except IOError:
        font = ImageFont.load_default()
    d.text((10, 80), text, font=font, fill=(255, 255, 0))
    img.save(os.path.join(IMAGES_DIR, filename))
    print(f"Image saved to {os.path.join(IMAGES_DIR, filename)}")

def generate_text(length=100):
    letters = string.ascii_letters + string.digits + " "
    return ''.join(random.choice(letters) for _ in range(length))

def generate_code():
    code = [
        "def hello_world():",
        "    print('Hello, world!')",
        "",
        "hello_world()"
    ]
    return "\n".join(code)

if __name__ == "__main__":
    # Generate image
    generate_image(filename="sample.png", text="AI Generated Image")
    # Generate text
    text = generate_text(50)
    print("Generated Text:\n", text)
    # Generate code
    code = generate_code()
    print("Generated Code:\n", code)