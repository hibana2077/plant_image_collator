import base64
from PIL import Image
from io import BytesIO

# Specify the path to the image file
image_path = "./test.jpg"

# Open the image file
with Image.open(image_path) as image:
    # Create a buffer to hold the bytes
    buffer = BytesIO()
    
    # Save the image as JPEG to the buffer
    image.save(buffer, format="JPEG")
    
    # Retrieve the bytes from the buffer
    image_bytes = buffer.getvalue()
    
    # Convert the bytes to base64
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # Print the base64 code
    print(image_base64)

print("done")
