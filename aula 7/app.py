from calculadora import calcular
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculadora.html', etapas = '', resultado = '')

@app.route('/calcular', methods=['POST'])
def calcular_route():
    return calcular()


if __name__ == "__main__":
    app.run(debug=True)