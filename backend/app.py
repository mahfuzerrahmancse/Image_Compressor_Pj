# from flask import Flask, request, jsonify
# from PIL import Image
# from io import BytesIO
# from base64 import b64encode
# from tkinter.filedialog import askopenfilename

# app = Flask(__name__)

# def compress_image(input_path, quality=85):
#     img = Image.open(input_path)

#     # Resize the image
#     img = img.resize(img.size, Image.BICUBIC)

#     # Save the compressed image to BytesIO
#     output_buffer = BytesIO()
#     img.save(output_buffer, format="WEBP", quality=quality)
    
#     # Convert the BytesIO object to a base64-encoded string
#     compressed_image_base64 = b64encode(output_buffer.getvalue()).decode('utf-8')

#     return compressed_image_base64

# @app.route('/compress', methods=['POST'])
# def compress_image_api():
#     try:
#         # Open file dialog to choose an image file
#         file_path = askopenfilename()

#         # Check if a file was selected
#         if not file_path:
#             return jsonify({"error": "No file selected."}), 400

#         # Compress the image and get the base64-encoded string
#         compressed_image_base64 = compress_image(file_path)

#         return jsonify({"compressed_image": compressed_image_base64}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask
# from PIL import Image
# from tkinter.filedialog import askopenfilename, asksaveasfilename

# app = Flask(__name__)

# @app.route('/',methods=['POST'])
# def img_compress():

#     file_path = askopenfilename()
#     img = Image.open(file_path)
#     myWidth, myHeight = img.size

#     img = img.resize((myWidth, myHeight), Image.BICUBIC)

#     save_path = asksaveasfilename()
#     img.save(save_path + "_compressed.jpg" , format="WEBP", quality=85)
    
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

app = Flask(__name__)

@app.route('/img_compress', methods=['POST'])
def img_compress():
    try:
        # Get the file from the request
        file = request.files['file']
        
        # Save the file to a temporary location
        file_path = '/tmp/input_image.jpg'
        file.save(file_path)

        # Open the image file
        img = Image.open(file_path)
        myWidth, myHeight = img.size

        # Resize the image
        img = img.resize((myWidth, myHeight), Image.BICUBIC)

        # Save the compressed image to a temporary location
        compressed_path = '/tmp/compressed_image.jpg'
        img.save(compressed_path, format="JPEG", quality=85)

        # Read the compressed image as binary data
        with open(compressed_path, 'rb') as f:
            compressed_data = f.read()

        return jsonify({"compressed_image": compressed_data.decode('latin-1')})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

