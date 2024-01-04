# final code

from flask import Flask, request, jsonify, send_file, send_from_directory
from PIL import Image
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

def compress_image(file_path, save_folder, target_size_kb=1024, target_size_reduction=50, max_width=800, max_height=800):
    img = Image.open(file_path)

    # Resize the image to reduce dimensions
    img.thumbnail((max_width, max_height))

    # Convert the image to RGB mode (remove alpha channel)
    img = img.convert("RGB")

    # Starting quality
    quality = 90  # Starting quality, you can adjust this based on your preference
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    compressed_image_name = f"{current_date}_compressed_image.jpeg"
    compressed_image_path = os.path.join(save_folder, compressed_image_name)
    while True:
        # Save the image in JPEG format with the current quality setting
        img.save(compressed_image_path, format="jpeg", quality=quality)

        # Check the file size
        compressed_size_kb = os.path.getsize(compressed_image_path) / 1024

        # Calculate the target quality for the next iteration
        quality_reduction = target_size_reduction / 2  # Divide by 2 as it's a heuristic adjustment
        quality = int(max(quality * (1 - quality_reduction / 100), 1))  # Ensure quality does not go below 1

        # Break the loop if the file size is below the target
        if compressed_size_kb <= target_size_kb:
            break

    return compressed_image_name

@app.route('/compress_image', methods=['POST'])
def compress_image_api():
    try:
        # Assuming the client sends a file in the request
        file = request.files['file']

        # Use the compression function
        save_folder = "images"  # Folder where the compressed image will be saved
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # Set the target size in KB (e.g., 500 KB)
        target_size_kb = 500

        # Set the target size reduction percentage (e.g., 50%)
        target_size_reduction = 50

        # Maximum width and height for resizing
        max_width = 800
        max_height = 800

        # Save the received file temporarily
        temp_path = "temp_image.png"  # Assuming the input image has an alpha channel (e.g., PNG)
        file.save(temp_path)

        # Get the final quality setting
        final_quality = compress_image(temp_path, save_folder, target_size_kb, target_size_reduction, max_width, max_height)

        return jsonify(final_quality)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/images/<path:image_name>', methods=['GET'])
def images(image_name):
    try:
        directory = "images"  # Update this with the correct directory path
        return send_from_directory(directory, image_name)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


# original algorithm
    
# from PIL import Image
# from tkinter.filedialog import askopenfilename, asksaveasfilename

# file_path = askopenfilename()
# img = Image.open(file_path)
# myWidth, myHeight = img.size

# # Resize the image
# img = img.resize((myWidth, myHeight), Image.BICUBIC)

# # Ask the user for the output file path
# save_path = asksaveasfilename()

# # Save the image in WebP format with reduced quality to decrease file size
# img.save(save_path + "_compressed.webp", format="WEBP", quality=85) 
