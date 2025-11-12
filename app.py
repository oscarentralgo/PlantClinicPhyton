from flask import Flask, render_template, request
from faq import obtener_faqs
from diagnósticos import obtener_diagnosticos
from consejos import obtener_consejos

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        result = f"Simulación: Diagnóstico para '{user_prompt}' generado por IA."
    return render_template("index.html", result=result)

@app.route("/faq")
def faq():
    faqs = obtener_faqs()
    return render_template("faq.html", faqs=faqs)

@app.route("/diagnosticos")
def diagnosticos():
    diags = obtener_diagnosticos()
    return render_template("diagnósticos.html", diagnosticos=diags)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/consejos")
def consejos():
    cons = obtener_consejos()
    return render_template("consejos.html", consejos=cons)

if __name__ == "__main__":
    app.run(debug=True)

