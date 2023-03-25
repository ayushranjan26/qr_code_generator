from flask import Flask, request, render_template
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    text_input = request.form['text_input']
    img = qrcode.make(text_input)
    img.save("static/qr_image.jpg")
    return render_template('image.html')

if __name__ == '__main__':
    app.run(debug=True)
