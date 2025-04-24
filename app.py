from flask import Flask, request, send_file, render_template
import qrcode
import qrcode.constants
import os

app = Flask(__name__)

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['link']
    file_name = request.form['file_name']
    file_path = f"static/{file_name}.png"
    generate_qr_code(data, file_path)
    return f'''
    <h2>QR Code Gerado!</h2>
    <img src="/{file_path}" alt="QR Code"><br>
    <a href="/{file_path}" download>Baixar QR Code</a><br>
    <a href="/">Voltar</a>
    '''

if __name__ == '__main__':
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
