from flask import Flask, request, jsonify
from flask_cors import CORS
from calculadora import calculadora
var_Calculador = calculadora()

app = Flask(__name__)
CORS(app)

@app.route('/calculadora', methods=['POST'])
def calcular():
    if request.method == 'POST':

        response = {}

        operador_aString = request.form.get('operador1')
        operador_a=float(operador_aString)
        operador_bString = request.form.get('operador2')
        operador_b=float(operador_bString)
        operador = request.form.get('op')

        if operador=="suma":
            resultado = var_Calculador.suma(operador_a,operador_b)
        elif operador == "resta":
            resultado = var_Calculador.resta(operador_a,operador_b)
        elif operador == "multiplicacion":
            resultado = var_Calculador.multiplicar(operador_a,operador_b)
        elif operador == "division":
            resultado = var_Calculador.dividir(operador_a,operador_b)
        elif operador == "potencia":
            resultado = var_Calculador.potencia(operador_a,operador_b)
        elif operador == "raiz":
            resultado = var_Calculador.raiz(operador_a,operador_b)
        
        if resultado is not False:
            response['resultado'] = resultado
            response['estado'] = 1

            return response
        
        response['estado'] = 0
        return response


@app.route("/")
def index():
    return "<h1>Bienvenido</h1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)