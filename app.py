from flask import Flask, render_template
import json

app = Flask(__name__)

# Cargar datos
def cargar_datos(archivo):
    with open(f'data/{archivo}', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosticos')
def diagnosticos():
    enfermedades = cargar_datos('enfermedades.json')
    return render_template('diagnosticos.html', enfermedades=enfermedades)

@app.route('/enfermedades')
def enfermedades():
    enfermedades_data = cargar_datos('enfermedades.json')
    return render_template('diseases.html', enfermedades=enfermedades_data)

@app.route('/productos')
def productos():
    productos_data = cargar_datos('productos.json')
    return render_template('products.html', productos=productos_data)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/consejos')
def consejos():
    return render_template('consejos.html')

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
