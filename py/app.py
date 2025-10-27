from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola Mundo', 200

@app.route('/startup', methods=['GET'])
def startup():
    # Aquí podrías agregar verificaciones iniciales
    return 'Startup OK', 200

@app.route('/readiness', methods=['GET'])
def readiness():
    # Aquí podrías validar conexión a BD, etc.
    return 'Ready', 200

@app.route('/health', methods=['GET'])
def health():
    # Aquí podrías validar estado general del servicio
    return 'Healthy', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
