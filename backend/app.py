from flask import Flask, request, jsonify
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def compress_image(file_path, save_path):
    img = Image.open(file_path)
    myWidth, myHeight = img.size

    # Resize the image
    img = img.resize((myWidth, myHeight), Image.BICUBIC)

    # Save the image in WebP format with reduced quality to decrease file size
    img.save(save_path + "_compressed.webp", format="WEBP", quality=85)

@app.route('/compress_image', methods=['POST'])
def compress_image_api():
    try:
        print("111111111")
        # Assuming the client sends a file in the request
        file = request.files['file']
        
        # Save the received file temporarily
        temp_path = "temp_image.jpg"
        file.save(temp_path)

        # Use the compression function
        save_path = asksaveasfilename()  # You may want to replace this with a predefined path
        compress_image(temp_path, save_path)

        return jsonify({"message": "Image compressed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def enhance():
    return 'Server Is Running'

if __name__ == '__main__':
    app.run(debug=True)


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
