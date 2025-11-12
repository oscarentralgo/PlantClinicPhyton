from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# --- Utilidad para cargar datos JSON ---
def cargar_json(filename):
    ruta = os.path.join('data', filename)
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

# --- Rutas principales ---

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnostico = None
    if request.method == "POST":
        consulta = request.form.get('consulta')
        if consulta:
            # Aquí puedes conectar IA real en el futuro
            diagnostico = f'Simulación: Diagnóstico para \'{consulta}\' generado por IA.'
    return render_template('index.html', diagnostico=diagnostico)

@app.route('/diagnosticos')
def diagnosticos():
    enfermedades = cargar_json('enfermedades.json')
    return render_template('diagnosticos.html', enfermedades=enfermedades)

@app.route('/enfermedades')
def enfermedades():
    enfermedades = cargar_json('enfermedades.json')
    return render_template('diseases.html', enfermedades=enfermedades)

@app.route('/productos')
def productos():
    productos = cargar_json('productos.json')
    return render_template('products.html', productos=productos)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/consejos')
def consejos():
    return render_template('consejos.html')

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('about.html')

# --- Opcional: manejo de errores 404 ---
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("404.html"), 404

# --- Lanzador ---
if __name__ == '__main__':
    app.run(debug=True)
