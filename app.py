from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template("index.html")

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']
    genero = request.form['genero']
    print(f"Nombre: {nombre}, Email: {email}, Género: {genero}")
    return "¡Registro exitoso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
