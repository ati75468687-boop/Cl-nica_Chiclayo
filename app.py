from flask import Flask, jsonify, request
from dotenv import load_dotenv
from modelo import RegistroTriaje
import os

# Cargar variables del archivo .env
load_dotenv()

# Crear aplicacion Flask
app = Flask(__name__)

# Historial temporal de pacientes
historial = []


# RUTA PRINCIPAL
@app.route("/", methods=["GET"])
def inicio():

    return jsonify({
        "empresa": os.getenv("CLINICA_NOMBRE"),
        "sistema": os.getenv("SISTEMA_NOMBRE"),
        "entorno": os.getenv("ENTORNO"),
        "version": os.getenv("API_VERSION"),
        "estado": "Servidor funcionando correctamente"
    }), 200


# REGISTRAR PACIENTES
@app.route("/triaje", methods=["POST"])
@app.route("/endpoint", methods=["POST"])
def registrar_paciente():

    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({
            "error": "Debe enviar un objeto JSON valido."
        }), 400

    campos_obligatorios = [
        "paciente_dni",
        "temperatura",
        "frecuencia_cardiaca"
    ]

    campos_faltantes = [
        campo for campo in campos_obligatorios
        if campo not in datos
    ]

    if campos_faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios.",
            "campos_faltantes": campos_faltantes
        }), 400

    if not isinstance(datos["paciente_dni"], str):
        return jsonify({
            "error": "El DNI debe ser texto."
        }), 400

    for campo in ["temperatura", "frecuencia_cardiaca"]:

        valor = datos[campo]

        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            return jsonify({
                "error": f"El campo {campo} debe ser numerico."
            }), 400

    try:
        paciente = RegistroTriaje(
            datos["paciente_dni"],
            datos["temperatura"],
            datos["frecuencia_cardiaca"]
        )

        resultado = paciente.obtener_datos()

        historial.append(resultado)

        return jsonify({
            "mensaje": "Paciente registrado correctamente.",
            "registro": resultado
        }), 201

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400


# CONSULTAR HISTORIAL
@app.route("/triaje", methods=["GET"])
@app.route("/endpoint", methods=["GET"])
def consultar_historial():

    return jsonify({
        "total_registros": len(historial),
        "historial": historial
    }), 200


# EJECUTAR SERVIDOR
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )