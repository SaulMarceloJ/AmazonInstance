from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta segura

@app.route('/')
def index():
    if 'user' in session:
        return f'Bienvenido {session["user"]} <br><a href="/logout">Cerrar sesión</a>'
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    password = request.form['password']
    if user == "admin" and password == "1234":
        session['user'] = user
        return redirect(url_for('index'))
    return "Credenciales inválidas"

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
