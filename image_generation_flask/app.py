from flask import Flask, render_template, request, redirect, url_for
import openai
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure OpenAI API (leave empty for now)
openai.api_key = ""  # here is the API key

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            try:
                # Call DALL·E API to generate an image
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,  # Number of images to generate
                    size="512x512",  # Image size (256x256, 512x512, or 1024x1024)
                )
                
                # Get the image URL from the response
                image_url = response['data'][0]['url']
                
                return render_template("index.html", image_url=image_url, prompt=prompt)
            
            except Exception as e:
                error = f"Error generating image: {str(e)}"
                return render_template("index.html", error=error)
        
        return redirect(url_for("home"))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)